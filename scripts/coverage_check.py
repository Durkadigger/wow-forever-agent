#!/usr/bin/env python3
"""
coverage_check.py — Which Blizzard staff posts name a class (or racials) but are
not cited in the matching knowledge file?

Red-team tool added after drill 02 (7 Nov 2026): the 2 Oct Warrior Rage post sat in
data/forum/staff-posts.json for five weeks without reaching talents-warrior.md.

  python scripts/coverage_check.py              # gaps only
  python scripts/coverage_check.py --all        # every (post, class) pair with status
  python scripts/coverage_check.py --since 2026-10-01

Posts listed in data/forum/coverage-ignore.json (url -> reason) are skipped.

A post "names" a class when the class name stands alone on a line (Blizzard's notes
use the class as a heading) or appears as "<Class>s are", "<Class> <ability>" in a
tuning sentence. A post is "cited" in a file when the file contains
`blizz-forum <post date>` anywhere. Citation by date is coarse on purpose: it says
"this refresh read that day's posts", nothing finer. Stdlib only.
"""
import argparse, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
POSTS = ROOT / "data" / "forum" / "staff-posts.json"
KNOW = ROOT / "knowledge"

CLASSES = ["Warrior", "Paladin", "Hunter", "Rogue", "Priest", "Shaman", "Mage", "Warlock", "Druid"]
RACES = ["Orc", "Troll", "Tauren", "Undead", "Skyborne", "Human", "Dwarf", "Gnome", "Night Elf", "racial"]

HEADING = {c: re.compile(rf"^\s*{c}s?\s*$", re.M) for c in CLASSES}
SENTENCE = {c: re.compile(rf"\b{c}s?\b\s+(?:are|is|will|can|now|no longer|players|pets?|reports?|talent|spec)", re.I) for c in CLASSES}
RACE_RX = re.compile(r"\b(" + "|".join(re.escape(r) for r in RACES) + r")s?\b", re.I)


def load_posts():
    data = json.loads(POSTS.read_text(encoding="utf-8"))
    # The store is {"<top key>": {post_id: post}} — descend until the values are posts.
    while isinstance(data, dict) and data and not any("body" in v for v in data.values() if isinstance(v, dict)):
        data = next(iter(data.values()))
    out = []
    for p in data.values():
        body = p.get("body") or ""
        if not body:
            continue
        out.append({
            "date": (p.get("created_at") or "")[:10],
            "title": p.get("topic_title") or "",
            "url": p.get("url") or "",
            "body": body,
            "tag": p.get("tag") or "",
        })
    return sorted(out, key=lambda p: p["date"])


def targets(post):
    hits = []
    for c in CLASSES:
        if HEADING[c].search(post["body"]) or SENTENCE[c].search(post["body"]) or c.lower() in post["title"].lower():
            hits.append(("talents-%s.md" % c.lower(), c))
    if RACE_RX.search(post["body"]) and ("racial" in post["body"].lower() or "racial" in post["title"].lower()):
        hits.append(("racials.md", "Racials"))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--since", default="2026-09-17")
    args = ap.parse_args()

    files = {f.name: f.read_text(encoding="utf-8") for f in KNOW.glob("*.md")}
    ignore_path = ROOT / "data" / "forum" / "coverage-ignore.json"
    ignore = json.loads(ignore_path.read_text(encoding="utf-8")) if ignore_path.exists() else {}
    posts = [p for p in load_posts() if p["date"] >= args.since]
    gaps, seen = [], set()
    for p in posts:
        if any(p["url"] == k or (k.endswith("/") and p["url"].startswith(k)) for k in ignore):
            continue  # exact post url, or a topic prefix ending in "/" (covers every post in that topic)
        for fname, label in targets(p):
            key = (p["date"], fname)
            if key in seen:
                continue
            seen.add(key)
            cited = f"blizz-forum {p['date']}" in files.get(fname, "")
            if args.all or not cited:
                gaps.append((p["date"], label, "cited" if cited else "NOT CITED", p["title"][:70], p["url"]))
    if not gaps:
        print("No uncited class or racial staff posts since", args.since)
        return 0
    for g in gaps:
        print(f"{g[0]}  {g[1]:<9} {g[2]:<9} {g[3]}\n{'':12}{g[4]}")
    n = sum(1 for g in gaps if g[2] == "NOT CITED")
    print(f"\n{n} uncited (post date, file) pair(s) since {args.since}.")
    return 1 if n else 0


if __name__ == "__main__":
    sys.exit(main())
