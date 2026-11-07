#!/usr/bin/env python3
"""
forum_scan.py — Pull Blizzard staff posts about WoW Forever from the official forums.

Tier-1 source (`blizz-forum` in sources.md). Only posts by accounts in the Blizzard
staff group count; player posts are tier 5 and are not stored. Stdlib only.

  python scripts/forum_scan.py                 # new staff posts since last run
  python scripts/forum_scan.py --all           # show everything stored, not just new
  python scripts/forum_scan.py --pages 5       # walk further back through the staff feed
  python scripts/forum_scan.py --topic 2350000 # dump the staff posts in one topic
  python scripts/forum_scan.py --categories    # list the WoW: Forever category tree

State: data/forum/staff-posts.json (id → post). Each post records first_seen so the
provenance tag is `[T1 blizz-forum <created_at date>]`, never the scan date.

Read-only. Never posts. 1 request/second.
"""
import argparse, datetime, html, json, pathlib, re, sys, time, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
STATE = ROOT / "data" / "forum" / "staff-posts.json"
BASE = "https://us.forums.blizzard.com/en/wow"
UA = {"User-Agent": "wow-forever-agent/1.0 (guild research tool; github.com/Durkadigger/wow-forever-agent)", "Accept": "application/json"}
FOREVER_ROOT_CATEGORY = 346
# Categories outside the 346 tree that are still Forever. 349 = 'WoW: Forever Beta Discussion',
# opened 17 Sept 2026 under In Development (Kaivax, topic 2352595). Known-issues posts live there.
EXTRA_CATEGORIES = {349: "WoW: Forever Beta Discussion"}
KEYWORDS = re.compile(r"\b(forever|skyborne|legacy (perk|tree)|camping|riverglades|shen'?dralas|hyjal summit|barrow deeps|zephras|realmless|invite-a-friend|name reservation)\b", re.I)

_last = 0.0
def get_json(path):
    global _last
    wait = 1.0 - (time.time() - _last)
    if wait > 0:
        time.sleep(wait)
    req = urllib.request.Request(f"{BASE}/{path}", headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        body = r.read()
    _last = time.time()
    return json.loads(body)


def forever_categories():
    """Return {id: name} for the WoW: Forever category and all its subcategories."""
    d = get_json("categories.json")
    cats = {}
    def walk(lst):
        for c in lst:
            cats[c["id"]] = c
            walk(c.get("subcategory_list") or [])
    walk(d["category_list"]["categories"])
    out = {}
    for cid, c in cats.items():
        p = c
        while p is not None:
            if p["id"] == FOREVER_ROOT_CATEGORY:
                out[cid] = c["name"]; break
            p = cats.get(p.get("parent_category_id"))
    # subcategory_ids may be listed without bodies; keep the ids anyway
    for sid in (cats.get(FOREVER_ROOT_CATEGORY, {}).get("subcategory_ids") or []):
        if sid not in out:
            try:
                out[sid] = get_json(f"c/{sid}/show.json")["category"]["name"]
            except Exception:
                out[sid] = f"subcategory {sid}"
    for cid, name in EXTRA_CATEGORIES.items():
        if cid not in out:
            out[cid] = cats[cid]["name"] if cid in cats else name
            for sub in (cats.get(cid, {}).get("subcategory_ids") or []):
                out.setdefault(sub, f"subcategory {sub} of {cid}")
    return out


def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"posts": {}}


def save_state(s):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(s, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def strip_html(s):
    """HTML → text, keeping what oneboxes (YouTube embeds, article cards) would otherwise lose."""
    s = s or ""
    vids = re.findall(r'data-video-id="([^"]+)"[^>]*data-video-title="([^"]*)"', s)
    links = re.findall(r'<a[^>]+href="(https?://[^"]+)"[^>]*>(.*?)</a>', s, re.S)
    s = re.sub(r"<br\s*/?>|</p>|</li>|</tr>|</h\d>", "\n", s)
    s = re.sub(r"</t[dh]>", " | ", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    s = re.sub(r"\n{3,}", "\n\n", s).strip()
    extra = [f"[video: {html.unescape(t) or 'untitled'} https://youtu.be/{v}]" for v, t in vids]
    extra += [f"[link: {u}]" for u, _ in links if "forums.blizzard.com" not in u and u not in s]
    return (s + ("\n" + "\n".join(dict.fromkeys(extra)) if extra else "")).strip()


def post_url(p):
    return f"{BASE}/t/{p.get('topic_slug','topic')}/{p['topic_id']}/{p.get('post_number', 1)}"


def is_staff(p):
    return bool(p.get("staff") or p.get("admin") or p.get("moderator") or (p.get("primary_group_name") or "").lower().startswith("blizzard"))


def scan_staff_feed(pages, forever_cats, stop_at_id=None):
    """Blizzard-tracker group feed: every staff post across the WoW forums, newest first.
    Walks at least `pages` pages and keeps going (up to 25) until it reaches stop_at_id, so a
    busy week on the retail forums cannot push Forever posts out of the window."""
    found = []
    before = None
    reached = False
    for page in range(25):
        if page >= pages and (reached or stop_at_id is None):
            break
        path = "groups/blizzard-tracker/posts.json" + (f"?before_post_id={before}" if before else "")
        d = get_json(path)
        posts = d if isinstance(d, list) else d.get("posts", [])
        if not posts:
            break
        for p in posts:
            if stop_at_id is not None and p["id"] <= stop_at_id:
                reached = True
            title = p.get("topic_title") or ""
            body = strip_html(p.get("cooked") or p.get("excerpt") or "")
            in_cat = p.get("category_id") in forever_cats
            if in_cat or KEYWORDS.search(title) or KEYWORDS.search(body[:2000]):
                try:  # the feed carries a truncated excerpt; fetch the full post
                    body = strip_html(get_json(f"posts/{p['id']}.json").get("cooked"))
                except Exception:
                    pass
                found.append(normalise(p, forever_cats, body))
        before = posts[-1]["id"]
    return found


def scan_category_topics(forever_cats):
    """Latest topics in the Forever category; pull staff posts out of each topic that has any."""
    found = []
    seen_topics = set()
    for cid in forever_cats:
        try:
            d = get_json(f"c/{cid}.json")
        except Exception as e:  # subcategory may need slug; skip quietly
            continue
        for t in d.get("topic_list", {}).get("topics", []):
            if t["id"] in seen_topics:
                continue
            seen_topics.add(t["id"])
            # Discourse marks topics with staff participation via posters[].description containing "Blizzard" group, not reliable; check pinned/closed by staff or high views as a cheap filter
            if not (t.get("pinned") or t.get("closed") or t.get("archived") or any("blizzard" in (po.get("description") or "").lower() for po in t.get("posters", []))):
                continue
            found.extend(topic_staff_posts(t["id"], forever_cats))
    return found


def topic_staff_posts(topic_id, forever_cats):
    d = get_json(f"t/{topic_id}.json")
    out = []
    for p in d.get("post_stream", {}).get("posts", []):
        if is_staff(p):
            p.setdefault("topic_title", d.get("title"))
            p.setdefault("topic_slug", d.get("slug"))
            p.setdefault("category_id", d.get("category_id"))
            out.append(normalise(p, forever_cats, strip_html(p.get("cooked"))))
    return out


def normalise(p, forever_cats, body):
    return {
        "id": p["id"],
        "topic_id": p.get("topic_id"),
        "topic_title": p.get("topic_title"),
        "topic_slug": p.get("topic_slug"),
        "post_number": p.get("post_number", 1),
        "username": p.get("username"),
        "created_at": p.get("created_at"),
        "category_id": p.get("category_id"),
        "category": forever_cats.get(p.get("category_id"), "other"),
        "url": post_url(p),
        "body": body[:60000],  # full post; the old 4000-char cap cut long hotfix and dev-notes posts (drill 02, 7 Nov 2026)
        "tag": f"[T1 blizz-forum {(p.get('created_at') or '')[:10]}]",
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--pages", type=int, default=2, help="pages of the staff feed to walk (20 posts each)")
    ap.add_argument("--topic", type=int)
    ap.add_argument("--categories", action="store_true")
    ap.add_argument("--no-topics", action="store_true", help="skip the per-topic scan of the Forever category")
    a = ap.parse_args()

    cats = forever_categories()
    if a.categories:
        for cid, n in sorted(cats.items()):
            print(cid, n)
        return
    if a.topic:
        for p in topic_staff_posts(a.topic, cats):
            print(f"\n{p['tag']} {p['username']} — {p['topic_title']} #{p['post_number']}\n{p['url']}\n{p['body']}")
        return

    state = load_state()
    newest_seen = max((int(k) for k in state["posts"]), default=None)
    found = scan_staff_feed(a.pages, cats, stop_at_id=newest_seen)
    if not a.no_topics:
        found.extend(scan_category_topics(cats))
    today = datetime.date.today().isoformat()
    found = list({p["id"]: p for p in found}.values())
    new = []
    for p in found:
        k = str(p["id"])
        if k not in state["posts"]:
            p["first_seen"] = today
            state["posts"][k] = p
            new.append(p)
        elif state["posts"][k].get("body") != p["body"]:
            state["posts"][k].update(p); state["posts"][k]["edited_seen"] = today
            new.append(p)
    save_state(state)

    show = sorted(state["posts"].values(), key=lambda p: p["created_at"] or "", reverse=True) if a.all else new
    print(f"{len(new)} new/edited staff post(s); {len(state['posts'])} stored. Forever categories: {', '.join(f'{k}={v}' for k, v in sorted(cats.items()))}")
    for p in show:
        print(f"\n{p['tag']} {p['username']} [{p['category']}] — {p['topic_title']} #{p['post_number']}\n{p['url']}\n{p['body'][:600]}{'…' if len(p['body']) > 600 else ''}")


if __name__ == "__main__":
    main()
