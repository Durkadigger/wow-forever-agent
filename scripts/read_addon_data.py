#!/usr/bin/env python3
"""
read_addon_data.py — Read what the WFATest addon saved and analyse it OUTSIDE the game.

  python scripts/read_addon_data.py                 summary of the newest saved file
  python scripts/read_addon_data.py --verdict       plain-English answers from a /wfa go run (docs/ingame-theory.md)
  python scripts/read_addon_data.py --watch LABEL   before/after analysis of one /wfa watch run
  python scripts/read_addon_data.py --probe         what the client let the addon read, out of combat vs in combat
  python scripts/read_addon_data.py --session       play-session log: fights, downtime, mana per fight, XP per hour
  python scripts/read_addon_data.py --spells [TEXT] spellbook scans: live tooltips for every known spell (filter by TEXT)
  python scripts/read_addon_data.py --json          dump everything as JSON
  python scripts/read_addon_data.py --file PATH     read a specific WFATest.lua

The addon writes WTF/Account/<account>/SavedVariables/WFATest.lua on /reload or logout.
All arithmetic happens here, never in the addon: WoW Forever gives addons "secret" values
they may not compute on, and nothing in this repo is subject to that. A value recorded as
"SECRET" is reported as secret. It is never treated as zero and never guessed.

Tier for anything learned from this data: in-game observation by the maintainer, tag source-id
`in-game` (add to sources.md on first use). Stdlib only.
"""
import argparse, json, pathlib, re, sys

CANDIDATES = [r"C:\Program Files (x86)\World of Warcraft", r"C:\Program Files\World of Warcraft",
              r"D:\World of Warcraft", r"E:\World of Warcraft", r"D:\Games\World of Warcraft",
              r"E:\Games\World of Warcraft", "/Applications/World of Warcraft"]
FLAVORS = ["_classic_beta_", "_forever_", "_classic_forever_"]
MARKERS = ("SECRET", "SECRET_TABLE", "NIL", "MISSING")


# ---- minimal parser for the Lua table literal WoW writes to SavedVariables -------------
class LuaParser:
    def __init__(self, text):
        self.s, self.i = text, 0

    def ws(self):
        while self.i < len(self.s):
            if self.s[self.i].isspace():
                self.i += 1
            elif self.s.startswith("--", self.i):
                j = self.s.find("\n", self.i)
                self.i = len(self.s) if j < 0 else j
            else:
                break

    def value(self):
        self.ws()
        c = self.s[self.i]
        if c == "{":
            return self.table()
        if c in "\"'":
            return self.string()
        for word, val in (("true", True), ("false", False), ("nil", None)):
            if self.s.startswith(word, self.i):
                self.i += len(word)
                return val
        m = re.compile(r"-?(?:0x[0-9a-fA-F]+|\d+\.?\d*(?:[eE][-+]?\d+)?|\.\d+|inf|nan)").match(self.s, self.i)
        if not m:
            raise ValueError(f"unexpected text at offset {self.i}: {self.s[self.i:self.i+40]!r}")
        self.i = m.end()
        t = m.group(0)
        return float(t) if any(ch in t for ch in ".eEn") and not t.startswith("0x") else int(t, 0)

    def string(self):
        q = self.s[self.i]
        self.i += 1
        out = []
        while self.s[self.i] != q:
            ch = self.s[self.i]
            if ch == "\\":
                self.i += 1
                e = self.s[self.i]
                if e.isdigit():
                    m = re.compile(r"\d{1,3}").match(self.s, self.i)
                    out.append(chr(int(m.group(0))))
                    self.i = m.end()
                    continue
                out.append({"n": "\n", "t": "\t", "r": "\r"}.get(e, e))
            else:
                out.append(ch)
            self.i += 1
        self.i += 1
        return "".join(out).encode("latin-1", "ignore").decode("utf-8", "replace") if any(ord(c) < 256 and ord(c) > 127 for c in out) else "".join(out)

    def table(self):
        self.i += 1
        arr, d = [], {}
        while True:
            self.ws()
            if self.s[self.i] == "}":
                self.i += 1
                break
            if self.s[self.i] == "[":
                self.i += 1
                k = self.value()
                self.ws()
                self.i += 1            # ]
                self.ws()
                self.i += 1            # =
                d[k] = self.value()
            elif re.match(r"[A-Za-z_]\w*\s*=", self.s[self.i:self.i + 80]):
                m = re.match(r"([A-Za-z_]\w*)\s*=", self.s[self.i:])
                self.i += m.end()
                d[m.group(1)] = self.value()
            else:
                arr.append(self.value())
            self.ws()
            if self.s[self.i] in ",;":
                self.i += 1
        if d and not arr and all(isinstance(k, int) for k in d) and sorted(d) == list(range(1, len(d) + 1)):
            return [d[k] for k in sorted(d)]
        if arr and not d:
            return arr
        for n, v in enumerate(arr, 1):
            d[n] = v
        return d


def parse_saved_variables(text, var="WFATestDB"):
    m = re.search(rf"^{var}\s*=\s*", text, re.M)
    if not m:
        raise SystemExit(f"{var} not found in file. Has the addon run and the game been /reload-ed?")
    p = LuaParser(text)
    p.i = m.end()
    return p.value()


# ---- locating the file -----------------------------------------------------------------
def find_files(wow=None):
    roots = [pathlib.Path(wow)] if wow else [pathlib.Path(c) for c in CANDIDATES]
    hits = []
    for r in roots:
        for f in FLAVORS:
            base = r / f / "WTF" / "Account"
            if base.is_dir():
                hits += list(base.glob("*/SavedVariables/WFATest.lua"))
    return sorted(hits, key=lambda p: p.stat().st_mtime, reverse=True)


# ---- analysis --------------------------------------------------------------------------
def num(v):
    return v if isinstance(v, (int, float)) and not isinstance(v, bool) else None


def describe(v):
    if isinstance(v, str) and (v in MARKERS or v.startswith(("ERROR:", "UNSUPPORTED:"))):
        return v
    return v


def summary(db):
    snaps, talents, tips = db.get("snapshots") or [], db.get("talents") or [], db.get("tooltips") or []
    print(f"addon v{db.get('addonVersion')} schema {db.get('schema')}: "
          f"{len(snaps)} snapshots, {len(talents)} talent dumps, {len(tips)} tooltips, "
          f"{len(db.get('probes') or [])} probes, {len(db.get('session') or [])} session records "
          f"(log {'ON' if db.get('auto') else 'OFF'}), {len(db.get('spellbooks') or [])} spellbook scans")
    if not snaps:
        return
    env = snaps[-1].get("env", {})
    print(f"\nClient {env.get('version')} build {env.get('build')}  INTERFACE NUMBER: {env.get('interface')}  "
          f"(put this in addon/WFATest/WFATest.toc)")
    print(f"secret system present: {env.get('hasIsSecretValue')} | restrictions active: {env.get('hasSecretRestrictions')} "
          f"| stats secret: {env.get('unitStatsSecret')} | auras secret: {env.get('aurasSecret')}")
    print(f"restriction types at last snapshot: {env.get('restrictions')}")
    # The key design question: when do stat reads go secret?
    rows = {}
    for s in snaps:
        e, st = s.get("env", {}), s.get("stats", {})
        key = ("in combat" if e.get("inCombat") is True else "out of combat",
               "instance:" + str(e.get("instanceType")) if e.get("inInstance") is True else "open world")
        r = rows.setdefault(key, {"n": 0, "secret": 0})
        r["n"] += 1
        r["secret"] += 1 if st.get("bonusHealing") == "SECRET" else 0
    print("\nWhen did the healing-bonus read come back secret?")
    for (combat, place), r in sorted(rows.items()):
        print(f"  {combat:14s} {place:22s} {r['secret']}/{r['n']} secret")
    labels = []
    for s in snaps:
        base = str(s.get("label", "")).split(":")[0]
        if base not in labels:
            labels.append(base)
    print("\nlabels stored:", ", ".join(labels))


def watch(db, label):
    snaps = [s for s in (db.get("snapshots") or []) if str(s.get("label", "")).split(":")[0] == label]
    if not snaps:
        raise SystemExit(f"No snapshots labelled '{label}'. Run without --watch to list labels.")
    print(f"'{label}': {len(snaps)} samples, {snaps[0].get('date')} to {snaps[-1].get('date')}")
    base_auras = {a.get("spellId") for a in (snaps[0].get("auras") or []) if isinstance(a, dict)}
    fields = [("healing bonus", lambda st: st.get("bonusHealing")),
              ("nature damage bonus", lambda st: (st.get("bonusDamage") or {}).get("nature")),
              ("attack power (base+pos)", lambda st: (num((st.get("attackPower") or {}).get("base")) or 0)
                                                     + (num((st.get("attackPower") or {}).get("pos")) or 0)
               if num((st.get("attackPower") or {}).get("base")) is not None else (st.get("attackPower") or {}).get("base")),
              ("spell haste %", lambda st: st.get("spellHaste")),
              ("melee crit %", lambda st: st.get("meleeCrit"))]
    for name, get in fields:
        series = [get(s.get("stats", {})) for s in snaps]
        secret = sum(1 for v in series if v == "SECRET")
        nums = [v for v in series if num(v) is not None]
        if secret:
            print(f"  {name:26s} SECRET in {secret}/{len(series)} samples. Not analysed (by design).")
            continue
        if not nums:
            print(f"  {name:26s} no numeric reads: {series[0]!r}")
            continue
        lo, hi = min(nums), max(nums)
        if lo == hi:
            print(f"  {name:26s} constant at {lo:g}")
        else:
            pct = (hi / lo - 1) * 100 if lo else float("inf")
            print(f"  {name:26s} {lo:g} -> {hi:g}   (+{pct:.1f}%)   CHANGED during the watch")
    gained = {}
    for s in snaps[1:]:
        for a in s.get("auras") or []:
            if isinstance(a, dict) and a.get("spellId") not in base_auras and a.get("spellId") not in gained:
                gained[a.get("spellId")] = (a.get("name"), s.get("label"))
    if gained:
        print("  buffs gained during the watch:", "; ".join(f"{n} ({i}) at {l}" for i, (n, l) in gained.items()))
    print("\nReading it: if a buff was gained and 'healing bonus' CHANGED by about the buff's size, the buff "
          "affects healing. If the buff was gained and healing stayed constant while damage bonus changed, it does not.")


# ---- probe: what can be logged ------------------------------------------------------------
def _probe_status(r):
    """One probe result -> (status, detail). Status is READABLE, SECRET, EMPTY, MISSING or ERROR."""
    if not isinstance(r, dict):
        r = {i: v for i, v in enumerate(r, 1)} if isinstance(r, list) else {}
    if r.get("missing"):
        return "MISSING", ""
    if "err" in r:
        return ("SECRET" if r["err"] == "SECRET" else "ERROR"), str(r["err"])[:70]
    vals = [r[k] for k in sorted(k for k in r if isinstance(k, int))]
    flat = []
    for v in vals:
        flat += list(v.values()) if isinstance(v, dict) else [v]
    if any(v in ("SECRET", "SECRET_TABLE") for v in flat):
        n = sum(1 for v in flat if v in ("SECRET", "SECRET_TABLE"))
        return "SECRET", f"{n}/{len(flat)} values secret"
    if not vals or all(v == "NIL" for v in vals):
        return "EMPTY", "returned nothing (no target, not casting, no pet...)"
    shown = [("{" + ", ".join(f"{k}={x}" for k, x in list(v.items())[:4]) + "}") if isinstance(v, dict) else str(v)
             for v in vals[:4]]
    return "READABLE", ", ".join(shown)[:90]


def probe_report(db):
    probes = db.get("probes") or []
    if not probes:
        raise SystemExit("No probes stored. In game: /wfa probe, fight one mob, /reload.")
    newest = {}
    for pr in probes:
        kind = "ooc" if pr.get("label") == "ooc" else "combat"
        # a 'combat+3' probe whose env says the fight was already over is not a combat probe
        if kind == "combat" and (pr.get("env") or {}).get("inCombat") is not True:
            continue
        if kind == "combat" and kind in newest and pr.get("label") == "combat+0" and newest[kind].get("label") == "combat+3":
            continue
        newest[kind] = pr
    for kind, pr in newest.items():
        e = pr.get("env") or {}
        print(f"{kind:7s} probe: {pr.get('date')}  {pr.get('class')}  build {e.get('build')}  zone {e.get('zone')}  "
              f"instance={e.get('inInstance')}  statsSecret={e.get('unitStatsSecret')}  aurasSecret={e.get('aurasSecret')}")
        active = [k for k, v in (e.get("restrictions") or {}).items() if v is True]
        print(f"        restriction types active: {', '.join(active) or 'none'}")
    if "combat" not in newest:
        print("\nNo in-combat probe yet: after /wfa probe, fight a mob for at least 3 seconds, then /reload.")
    keys = sorted(set().union(*[set((pr.get("results") or {})) for pr in newest.values()]))
    groups = {}
    print(f"\n{'API call':52s} {'out of combat':14s} {'in combat':14s}")
    for k in keys:
        st = {kind: _probe_status((pr.get("results") or {}).get(k)) for kind, pr in newest.items()}
        o, c = st.get("ooc", ("-", "")), st.get("combat", ("-", ""))
        print(f"{k:52s} {o[0]:14s} {c[0]:14s} {o[1] if o[0] == 'READABLE' else (c[1] or o[1])}")
        groups.setdefault((o[0], c[0]), []).append(k)
    print("\nSUMMARY")
    for (o, c), label in ((("READABLE", "READABLE"), "Loggable all the time"),
                          (("READABLE", "SECRET"), "Loggable only OUT of combat (secret in combat)"),
                          (("SECRET", "SECRET"), "Never loggable (secret even out of combat)"),
                          (("MISSING", "MISSING"), "Not in this build")):
        if groups.get((o, c)):
            print(f"  {label}:\n    " + ", ".join(groups[(o, c)]))
    ns = (newest.get("ooc") or {}).get("namespaces") or {}
    if ns:
        print("\nAPI namespaces on this build (function counts):")
        print("  " + ", ".join(f"{k}={'MISSING' if v == 'MISSING' else len(v.split())}" for k, v in sorted(ns.items())))
        for k in ("C_DamageMeter", "C_CombatLog"):
            if ns.get(k) and ns[k] != "MISSING":
                print(f"  {k}: {ns[k]}")
    print("\nA value that is SECRET in combat is recorded as secret and left alone (docs/addon-feasibility.md §3). "
          "Per-cast combat data comes from the game's own /combatlog file instead.")


# ---- session log --------------------------------------------------------------------------
def _median(xs):
    xs = sorted(xs)
    if not xs:
        return None
    m = len(xs) // 2
    return xs[m] if len(xs) % 2 else (xs[m - 1] + xs[m]) / 2


def _fmt(v, unit="", nd=0):
    return "n/a" if v is None else f"{v:.{nd}f}{unit}"


def session_report(db):
    recs = db.get("session") or []
    if not recs:
        raise SystemExit("No session records. The log is on by default in v0.3.0; play, then /reload or log out.")
    # split into characters at each 'login' record
    chars, cur = {}, None
    for r in recs:
        if r.get("e") == "login":
            cur = f"{r.get('name')} ({r.get('race')} {r.get('class')})"
        chars.setdefault(cur or "unknown character (log started mid-session)", []).append(r)
    print(f"{len(recs)} session records, {recs[0].get('t')} .. {recs[-1].get('t')} (unix time)\n")
    for who, rs in chars.items():
        print(f"=== {who}: {len(rs)} records ===")
        by_level = {}
        start = None
        prev = None
        last_end_t = None
        for r in rs:
            e, t, lvl = r.get("e"), num(r.get("t")), num(r.get("lvl"))
            L = by_level.setdefault(lvl, {"fights": [], "down": [], "mp": [], "hp": [], "xp_kill": 0, "xp_other": 0,
                                          "deaths": 0, "active": 0, "secret": 0, "targets": {}})
            if prev is not None and t is not None and num(prev.get("t")) is not None:
                gap = t - prev["t"]
                if 0 <= gap <= 300:                       # gaps over 5 min are AFK / logged out, not play time
                    L["active"] += gap
            if e == "combat_start":
                start = r
                if last_end_t is not None and t is not None and 0 <= t - last_end_t <= 300:
                    L["down"].append(t - last_end_t)
                tg = r.get("target")
                if isinstance(tg, dict) and tg.get("name") and not tg.get("player"):
                    key = f"{tg.get('name')} (lvl {tg.get('level')})"
                    L["targets"][key] = L["targets"].get(key, 0) + 1
            elif e in ("combat_end", "after_combat") and start is not None:
                if e == "combat_end":
                    if t is not None and num(start.get("t")) is not None:
                        L["fights"].append(t - start["t"])
                    last_end_t = t
                vals = [start.get("mp"), r.get("mp"), start.get("hp"), r.get("hp")]
                if any(v == "SECRET" for v in vals):
                    # combat_end can still be secret; the after_combat record 2 sec later gets a second try
                    if e == "after_combat":
                        L["secret"] += 1
                        start = None
                elif all(num(v) is not None for v in vals) and num(r.get("mpMax")) and num(r.get("hpMax")):
                    L["mp"].append((start["mp"] - r["mp"]) / r["mpMax"] * 100)
                    L["hp"].append((start["hp"] - r["hp"]) / r["hpMax"] * 100)
                    start = None
                elif e == "after_combat":
                    start = None
            elif e == "dead":
                L["deaths"] += 1
            if e == "xp" and prev is not None and num(r.get("xp")) is not None and num(prev.get("xp")) is not None:
                if num(prev.get("lvl")) == lvl:
                    gain = r["xp"] - prev["xp"]
                else:
                    gain = (num(prev.get("xpMax")) or 0) - prev["xp"] + r["xp"]
                near_fight = r.get("combat") is True or (last_end_t is not None and t is not None and t - last_end_t <= 3)
                if gain > 0:
                    L["xp_kill" if near_fight else "xp_other"] += gain
            prev = r
        print(f"{'lvl':>4s} {'fights':>6s} {'med fight':>9s} {'med downtime':>12s} {'mana/fight':>10s} {'hp/fight':>9s} "
              f"{'kill XP':>8s} {'other XP':>8s} {'XP/hour':>8s} {'deaths':>6s} {'play min':>8s}")
        for lvl in sorted(k for k in by_level if k is not None):
            L = by_level[lvl]
            xp = L["xp_kill"] + L["xp_other"]
            rate = xp / L["active"] * 3600 if L["active"] >= 300 else None
            print(f"{lvl:4d} {len(L['fights']):6d} {_fmt(_median(L['fights']), 's'):>9s} {_fmt(_median(L['down']), 's'):>12s} "
                  f"{_fmt(_median(L['mp']), '%', 1):>10s} {_fmt(_median(L['hp']), '%', 1):>9s} {L['xp_kill']:8d} "
                  f"{L['xp_other']:8d} {_fmt(rate):>8s} {L['deaths']:6d} {L['active'] / 60:8.1f}")
        secret = sum(L["secret"] for L in by_level.values())
        if secret:
            print(f"  {secret} fight records had SECRET health/mana and were skipped for the mana and hp columns.")
        tg = {}
        for L in by_level.values():
            for k, n in L["targets"].items():
                tg[k] = tg.get(k, 0) + n
        if tg:
            top = sorted(tg.items(), key=lambda kv: -kv[1])[:8]
            print("  most-fought targets: " + "; ".join(f"{k} x{n}" for k, n in top))
        print()
    print("mana/fight and hp/fight are medians, as % of max, combat start to combat end (negative = ended higher).\n"
          "XP/hour counts only play time (gaps over 5 min dropped) and needs at least 5 min at that level.\n"
          "'kill XP' = XP that arrived in combat or within 3 sec after it; 'other' = quests and exploration.")


def spells_report(db, text):
    books = db.get("spellbooks") or []
    if not books:
        raise SystemExit("No spellbook scans. In game: /wfa spells (out of combat), then /reload.")
    newest = {}
    for b in books:
        newest[b.get("class")] = b                     # newest scan per class
    want = (text or "").lower()
    for cls, b in newest.items():
        spells = b.get("spells") or []
        e = b.get("env") or {}
        print(f"=== {cls} level {b.get('level')}, {b.get('date')}, build {e.get('build')}: {len(spells)} spells ===")
        if b.get("missing"):
            print("  spellbook API was missing on this build.")
            continue
        for sp in spells:
            lines = [ln.get("left") for ln in (sp.get("lines") or []) if isinstance(ln, dict)
                     and isinstance(ln.get("left"), str) and ln.get("left") not in MARKERS]
            blob = " ".join([str(sp.get("name"))] + lines).lower()
            if want and want not in blob:
                continue
            if want:
                print(f"\n[{sp.get('spellID')}] {sp.get('name')} {sp.get('subName') if sp.get('subName') not in MARKERS else ''}"
                      f" ({sp.get('line')}{', passive' if sp.get('passive') is True else ''})")
                for ln in sp.get("lines") or []:
                    if isinstance(ln, dict):
                        l, r = ln.get("left"), ln.get("right")
                        print("    " + str(l) + (f"    | {r}" if isinstance(r, str) and r not in MARKERS and r else ""))
            else:
                print(f"  {sp.get('spellID'):>8}  {sp.get('name')}" + ("  (passive)" if sp.get("passive") is True else ""))
    if not want:
        print("\nAdd a word to see full tooltips, e.g. --spells fireball")


# ---- verdicts: predictions are written down in docs/ingame-theory.md BEFORE the data exists ----
MIN_BASE = 30      # below this a 10% change is lost in integer rounding
BUFF_PCT = 10.0    # Blood Fury, datamined: auras 166/167/317 at 10 points each


def _series(snaps, get):
    return [get(s.get("stats", {})) for s in snaps]


def _span(series):
    if any(v == "SECRET" for v in series):
        return "secret", None, None
    nums = [v for v in series if num(v) is not None]
    if not nums:
        return "missing", None, None
    return "ok", min(nums), max(nums)


def _ap(st):
    ap = st.get("attackPower") or {}
    b, p = num(ap.get("base")), num(ap.get("pos"))
    return ap.get("base") if b is None else b + (p or 0)


def verdict_blood_fury(db):
    print("1. Does Blood Fury raise healing?  (open question #1)")
    snaps = [s for s in (db.get("snapshots") or []) if str(s.get("label", "")).split(":")[0] == "bloodfury"]
    if not snaps:
        print("   NO DATA. No 'bloodfury' watch stored (needs an Orc and /wfa go).")
        return
    base_auras = {a.get("spellId") for a in (snaps[0].get("auras") or []) if isinstance(a, dict)}
    seen = {a.get("spellId") for s in snaps[1:] for a in (s.get("auras") or []) if isinstance(a, dict)}
    pressed = 20572 in (seen - base_auras)
    h_state, h_lo, h_hi = _span(_series(snaps, lambda st: st.get("bonusHealing")))
    d_state, d_lo, d_hi = _span(_series(snaps, lambda st: (st.get("bonusDamage") or {}).get("nature")))
    a_state, a_lo, a_hi = _span(_series(snaps, _ap))
    if "secret" in (h_state, d_state):
        print("   CANNOT TELL FROM THE ADDON. The stat read came back secret. Use the combat-log method instead.")
        return
    if h_state != "ok":
        print("   NO DATA. Healing bonus was not readable on this client.")
        return
    # Positive control: attack power must move, or the button was never pressed / the aura list is secret.
    ap_moved = a_state == "ok" and a_lo and (a_hi / a_lo - 1) * 100 >= BUFF_PCT * 0.6
    if not pressed and not ap_moved:
        print("   INVALID RUN. Blood Fury (20572) never appeared and attack power did not move. Press it during the watch.")
        return
    if h_lo < MIN_BASE:
        print(f"   INCONCLUSIVE. Healing bonus was {h_lo:g}; 10% of that is under {MIN_BASE/10:g} points and rounds away.")
        print(f"   Re-run with at least {MIN_BASE} healing bonus (better: 100+). Attack power control "
              f"{'moved' if ap_moved else 'did not move'}, so the button press itself registered.")
        return
    h_pct = (h_hi / h_lo - 1) * 100
    d_pct = (d_hi / d_lo - 1) * 100 if d_state == "ok" and d_lo else None
    d_txt = "n/a" if d_pct is None else f"+{d_pct:.1f}%"
    print(f"   healing bonus {h_lo:g} -> {h_hi:g} (+{h_pct:.1f}%) | nature damage bonus {d_txt} | "
          f"attack power {'moved' if ap_moved else 'flat'}")
    if h_pct >= BUFF_PCT * 0.8:
        print("   YES. Healing rose by about the buff's size. Orc moves ahead of Troll for raid healing throughput;")
        print("   check whether the gain applied to ALL of the healing bonus or only part (see theory doc, H1b).")
    elif h_pct <= 1.0 and d_pct is not None and d_pct >= BUFF_PCT * 0.8:
        print("   NO. Spell damage rose and healing did not. Troll stays the raid-healing pick.")
    elif h_pct <= 1.0:
        print("   NO on the stat sheet, but spell damage did not move either, so confirm with the combat-log method.")
    else:
        print("   PARTIAL. Healing rose by less than the buff. Likely only the spell-power part of the healing")
        print("   bonus scales and +healing from gear does not (theory doc, H1b). Record both numbers.")


def verdict_secrecy(db):
    print("\n2. Can the addon read stats in combat and in dungeons?")
    rows = {}
    for s in db.get("snapshots") or []:
        e, st = s.get("env", {}), s.get("stats", {})
        key = ("in combat" if e.get("inCombat") is True else "out of combat",
               "instance" if e.get("inInstance") is True else "open world")
        r = rows.setdefault(key, [0, 0])
        r[0] += 1
        r[1] += 1 if st.get("bonusHealing") == "SECRET" else 0
    want = [("out of combat", "open world"), ("in combat", "open world"), ("out of combat", "instance")]
    for k in want:
        if k not in rows:
            print(f"   {k[0]}, {k[1]}: NOT TESTED")
        else:
            n, sec = rows[k]
            print(f"   {k[0]}, {k[1]}: {'SECRET' if sec == n else 'READABLE' if sec == 0 else 'MIXED'} ({sec}/{n} secret)")
    if rows.get(("in combat", "open world"), [0, 0])[1]:
        print("   -> every stat test must be done out of combat; per-heal numbers come from /combatlog only.")


def verdict_stats(db):
    print("\n3. Are healing and spell damage one stat?")
    snaps = [s for s in (db.get("snapshots") or []) if s.get("label") == "baseline"]
    if not snaps:
        print("   NO DATA.")
        return
    st = snaps[-1].get("stats", {})
    h, d = st.get("bonusHealing"), st.get("bonusDamage") or {}
    if h == "SECRET" or num(h) is None:
        print(f"   NO DATA ({h!r}).")
        return
    dn = {k: v for k, v in d.items() if num(v) is not None}
    print(f"   healing bonus {h:g} | damage bonus by school {dn}")
    if dn and all(v == h for v in dn.values()):
        print("   Identical on this character. Consistent with one Spell Power stat, but only a +healing-only item")
        print("   can prove it: snapshot with and without one (test 1.2).")
    elif dn:
        print("   They differ, so healing and damage are tracked separately, as in Classic. Gear weights must treat")
        print("   '+healing' and 'spell power' as two stats.")


def verdict_tooltips(db):
    print("\n4. Live tooltips captured (the agent compares these with the datamine by hand):")
    tips = db.get("tooltips") or []
    if not tips:
        print("   none")
    for tip in tips:
        print(f"   {tip.get('spellID')} {tip.get('name')}: {str(tip.get('description') or tip.get('text') or '')[:110]}")


def verdict(db):
    verdict_blood_fury(db)
    verdict_secrecy(db)
    verdict_stats(db)
    verdict_tooltips(db)
    print("\nFile results in knowledge/ as [T2 in-game <date> b:<build>] with the method and n in the note.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--file")
    ap.add_argument("--wow")
    ap.add_argument("--watch")
    ap.add_argument("--verdict", action="store_true")
    ap.add_argument("--probe", action="store_true")
    ap.add_argument("--session", action="store_true")
    ap.add_argument("--spells", nargs="?", const="", default=None, metavar="TEXT")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if a.file:
        path = pathlib.Path(a.file)
    else:
        files = find_files(a.wow)
        if not files:
            raise SystemExit("No WFATest.lua found under WTF/Account/*/SavedVariables. Install the addon, "
                             "run a /wfa command in game, then /reload.")
        path = files[0]
    print(f"reading {path}\n")
    db = parse_saved_variables(path.read_text(encoding="utf-8", errors="replace"))
    if a.json:
        print(json.dumps(db, indent=1, default=str))
    elif a.verdict:
        verdict(db)
    elif a.watch:
        watch(db, a.watch)
    elif a.probe:
        probe_report(db)
    elif a.session:
        session_report(db)
    elif a.spells is not None:
        spells_report(db, a.spells)
    else:
        summary(db)


if __name__ == "__main__":
    main()
