#!/usr/bin/env python3
"""
wago_diff.py — Snapshot WoW Forever DB2 tables from wago.tools and diff two builds.

Tier-2 source (`wago` in sources.md). Stdlib only.

  python scripts/wago_diff.py --list-products
      Show every product wago.tools tracks with its newest build. Use this to find
      the Forever product slug (look for a new product, or an existing slug flagged
      "new version line"). Builds are sorted by creation time, not version number.

  python scripts/wago_diff.py --snapshot [--product SLUG] [--version X.Y.Z.N]
      Download the tables in TABLES for the product's newest build (or --version)
      into data/wago/<product>/<version>/<Table>.csv and register the build in
      data/builds.json. Product defaults to "wago_product" in data/builds.json.

  python scripts/wago_diff.py --diff [--from VER] [--to VER] [--product SLUG]
      Diff two snapshots (default: the two newest). Writes
      data/wago/diffs/<from>__<to>.md with added / removed / changed spells,
      talents, and races, watchlist names first, and appends a CHANGELOG entry.

  python scripts/wago_diff.py --probe --product SLUG [--version X.Y.Z.N]
      Quick check whether a build looks like Forever (Skyborne race, Shatter Curse,
      Well Rested, Plainsrunning, Bountiful Harvest). Defaults to the newest build.

Rate limit: 1 request/second. Identify as wow-forever-agent.
"""
import argparse, csv, datetime, io, json, pathlib, sys, time, urllib.error, urllib.parse, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
WAGO = DATA / "wago"
BUILDS = DATA / "builds.json"
WATCH = DATA / "watchlist.txt"
CHANGELOG = ROOT / "CHANGELOG.md"
API = "https://wago.tools"
UA = {"User-Agent": "wow-forever-agent/1.0 (guild research tool; github.com/Durkadigger/wow-forever-agent)"}

# Tables that answer the questions we actually ask. Description_lang on Spell is the
# tooltip text; SpellCooldowns answers the racial-cooldown open question; SpellPower is
# mana cost; Talent/TalentTab give tree layout and per-rank spell ids.
TABLES = ["SpellName", "Spell", "SpellEffect", "SpellCooldowns", "SpellPower",
          "SpellCategories", "SpellMisc", "Talent", "TalentTab", "ChrRaces", "ChrClasses",
          # Lookup tables needed to resolve $d (duration), $a (radius), cast time, range,
          # $i (max targets) and $u (stacks) in tooltip text.
          "SpellDuration", "SpellRadius", "SpellCastTimes", "SpellRange",
          "SpellTargetRestrictions", "SpellAuraOptions", "SpellLevels", "SpellClassOptions",
          # Forever stores its talent trees AND the Legacy tree in the modern Trait system.
          # The old Talent/TalentTab tables above are a half-migrated vanilla leftover in
          # 1.60.x (wrong layout, dangling spell ids) - kept only so diffs show if that changes.
          "TraitSystem", "TraitTree", "TraitSubTree", "TraitNode", "TraitNodeEntry",
          "TraitNodeXTraitNodeEntry", "TraitDefinition", "TraitEdge", "TraitNodeGroup",
          "TraitNodeGroupXTraitNode", "TraitCond", "TraitNodeGroupXTraitCond",
          "TraitNodeXTraitCond", "TraitCurrency", "TraitCost", "TraitNodeGroupXTraitCost",
          "TraitTreeXTraitCurrency", "SkillLineXTraitTree",
          # Per-rank values: TraitDefinitionEffectPoints maps (definition, effect) -> Curve;
          # CurvePoint gives rank -> points. Without these, multi-rank numbers are guesses.
          "TraitDefinitionEffectPoints", "Curve", "CurvePoint",
          # Racials: which spells each race gets.
          "SkillLine", "SkillLineAbility", "SkillRaceClassInfo"]

_last = 0.0
def get(url, timeout=90):
    global _last
    wait = 1.0 - (time.time() - _last)
    if wait > 0:
        time.sleep(wait)
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        body = r.read()
    _last = time.time()
    return body


def load_builds():
    return json.loads(BUILDS.read_text(encoding="utf-8")) if BUILDS.exists() else {"wago_product": None, "builds": []}


def save_builds(b):
    BUILDS.write_text(json.dumps(b, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def products():
    d = json.loads(get(f"{API}/api/builds"))
    out = {}
    for prod, lst in d.items():
        if isinstance(lst, list) and lst:
            # wago.tools does NOT guarantee order (it lists by version number, so an old
            # 5.5.0 build sorts above a new 1.60.1 one). Always sort by creation time.
            out[prod] = sorted(lst, key=lambda b: b.get("created_at", ""), reverse=True)
    return out


def build_created(prod, version):
    """created_at date for a specific version, or None if wago does not list it."""
    for b in products().get(prod, []):
        if b.get("version") == version:
            return b["created_at"][:10]
    return None


def build_no(version):
    """Trailing build number. Monotonic across version lines, unlike the dotted version."""
    tail = version.rsplit(".", 1)[-1]
    return int(tail) if tail.isdigit() else 0


def newest_version(prod):
    p = products().get(prod)
    if not p:
        raise SystemExit(f"wago.tools has no product '{prod}'. Run --list-products.")
    full = [b for b in p if not b.get("is_bgdl")] or p  # bgdl = background-download stub, tables may be incomplete
    return full[0]["version"], full[0]["created_at"][:10]


def table_csv(table, version):
    url = f"{API}/db2/{table}/csv?build={urllib.parse.quote(version)}"
    return get(url).decode("utf-8", errors="replace")


def resolve_product(arg):
    prod = arg or load_builds().get("wago_product")
    if not prod:
        raise SystemExit("No Forever product slug confirmed yet. Run --list-products, verify with --probe, "
                         "then set \"wago_product\" in data/builds.json or pass --product.")
    return prod


def cmd_list_products():
    for prod, lst in sorted(products().items(), key=lambda kv: kv[1][0]["created_at"], reverse=True):
        b = lst[0]
        major = lambda v: ".".join(v.split(".")[:2])
        prev = lst[1] if len(lst) > 1 else None
        flag = f"   <-- new version line (was {prev['version']})" if prev and major(prev["version"]) != major(b["version"]) else ""
        if not flag and len(lst) > 2 and major(lst[2]["version"]) != major(b["version"]):
            flag = f"   <-- new version line (was {lst[2]['version']})"
        print(f"{prod:24s} {b['version']:18s} {b['created_at'][:10]}   ({len(lst)} builds known){flag}")
    print("\nForever candidates: a new product slug, OR an existing slug flagged 'new version line'"
          "\n(Blizzard reused wow_classic_beta for Forever 1.60.x on 2026-09-16). Confirm with --probe.")


def cmd_probe(prod, version=None):
    if version:
        ver, created = version, build_created(prod, version) or "date unknown"
        print(f"{prod} build {ver} ({created})")
    else:
        ver, created = newest_version(prod)
        print(f"{prod} newest build {ver} ({created})")
    races = [r.get("Name_lang", "") for r in csv.DictReader(io.StringIO(table_csv("ChrRaces", ver)))]
    names = {r.get("Name_lang", "") for r in csv.DictReader(io.StringIO(table_csv("SpellName", ver)))}
    checks = {
        "Skyborne race": any("skyborne" in r.lower() for r in races),
        "Shatter Curse spell": "Shatter Curse" in names,
        "Well Rested spell": "Well Rested" in names,
        "Plainsrunning spell": "Plainsrunning" in names,
        "Bountiful Harvest spell": "Bountiful Harvest" in names,
    }
    # Lava Burst / Riptide are deliberately NOT checked: they exist in every Wrath-or-later
    # client, so they scored the 2025 Mists Classic beta as half-Forever.
    for k, v in checks.items():
        print(f"  {'YES' if v else 'no ':3s}  {k}")
    score = sum(checks.values())
    print("Verdict:", "looks like Forever" if score >= 4 else "probably NOT Forever" if score <= 1 else "inconclusive")


def cmd_snapshot(prod, version):
    if version:
        ver, created = version, build_created(prod, version) or datetime.date.today().isoformat()
    else:
        ver, created = newest_version(prod)
    dest = WAGO / prod / ver
    dest.mkdir(parents=True, exist_ok=True)
    for t in TABLES:
        f = dest / f"{t}.csv"
        if f.exists():
            print(f"  have {t}")
            continue
        print(f"  fetch {t} ...", end="", flush=True)
        try:
            txt = table_csv(t, ver)
        except urllib.error.HTTPError as e:
            # Not every build ships every table (e.g. TraitSubTree is absent in 1.60.1).
            # A missing optional table must not abort the snapshot.
            print(f" skipped (HTTP {e.code})")
            continue
        f.write_text(txt, encoding="utf-8")
        print(f" {txt.count(chr(10))} rows")
    b = load_builds()
    if not any(x.get("version") == ver and x.get("product") == prod for x in b["builds"]):
        b["builds"].append({"label": f"wago-{ver}", "product": prod, "version": ver, "date": created,
                            "note": "Snapshot via scripts/wago_diff.py", "sources": ["wago"]})
        b["builds"].sort(key=lambda x: x["date"])
        save_builds(b)
        print(f"Registered build {ver} in data/builds.json")
    print(f"Snapshot at {dest.relative_to(ROOT)}")


def read_table(prod, ver, table):
    f = WAGO / prod / ver / f"{table}.csv"
    if not f.exists():
        return {}
    rows = list(csv.DictReader(f.open(encoding="utf-8")))
    return {r["ID"]: r for r in rows if r.get("ID")}


def load_watch():
    if not WATCH.exists():
        return set()
    return {ln.strip().lower() for ln in WATCH.read_text(encoding="utf-8").splitlines() if ln.strip() and not ln.startswith("#")}


def cmd_diff(prod, v_from, v_to):
    snaps = sorted([p.name for p in (WAGO / prod).iterdir() if p.is_dir()], key=build_no) if (WAGO / prod).exists() else []
    if not v_from or not v_to:
        if len(snaps) < 2:
            raise SystemExit(f"Need two snapshots for {prod}; have {snaps}. Run --snapshot (twice, across builds).")
        v_from, v_to = snaps[-2], snaps[-1]
    watch = load_watch()
    names_old, names_new = read_table(prod, v_from, "SpellName"), read_table(prod, v_to, "SpellName")
    name = lambda sid: (names_new.get(sid) or names_old.get(sid) or {}).get("Name_lang", f"spell {sid}")
    out = [f"# Wago diff {prod}: {v_from} → {v_to}", f"Generated {datetime.date.today().isoformat()} by scripts/wago_diff.py. Tier 2 source `wago`. Tag values from this diff as `[T2 wago {datetime.date.today().isoformat()} b:{v_to}]`.", ""]
    changed_names = set()

    # Spells: names, tooltips, cooldowns, costs, effects — keyed to the spell id.
    spell_tables = {"Spell": ("Description_lang", "AuraDescription_lang"),
                    "SpellCooldowns": ("RecoveryTime", "CategoryRecoveryTime", "StartRecoveryTime"),
                    "SpellPower": ("ManaCost", "PowerCostPct", "ManaPerSecond"),
                    "SpellCategories": ("DefenseType", "DispelType", "Mechanic"),
                    "SpellMisc": ("DurationIndex", "RangeIndex", "CastingTimeIndex")}
    sections = {"Added spells": [], "Removed spells": [], "Changed spells": []}
    for sid in sorted(set(names_new) | set(names_old), key=int):
        if sid in names_new and sid not in names_old:
            sections["Added spells"].append((name(sid), f"- **{name(sid)}** (id {sid}): {spell_desc(prod, v_to, sid)}"))
        elif sid in names_old and sid not in names_new:
            sections["Removed spells"].append((name(sid), f"- ~~{name(sid)}~~ (id {sid})"))
    for table, fields in spell_tables.items():
        old, new = read_table(prod, v_from, table), read_table(prod, v_to, table)
        key = "SpellID" if table != "Spell" else "ID"
        by_old = {r.get(key): r for r in old.values()}
        by_new = {r.get(key): r for r in new.values()}
        for sid in set(by_old) & set(by_new):
            diffs = [(f, by_old[sid].get(f, ""), by_new[sid].get(f, "")) for f in fields if by_old[sid].get(f, "") != by_new[sid].get(f, "")]
            if diffs:
                changed_names.add(sid)
                for f, a, b in diffs:
                    sections["Changed spells"].append((name(sid), f"- **{name(sid)}** (id {sid}) {table}.{f}: `{a[:160]}` → `{b[:160]}`"))
    # SpellEffect: keyed by effect ID, group by SpellID
    eo, en = read_table(prod, v_from, "SpellEffect"), read_table(prod, v_to, "SpellEffect")
    for eid in set(eo) & set(en):
        a, b = eo[eid], en[eid]
        fs = [f for f in ("EffectBasePointsF", "EffectBasePoints", "Coefficient", "Variance", "EffectAura", "Effect", "EffectMiscValue_0", "EffectAmplitude", "EffectChainTargets") if a.get(f, "") != b.get(f, "")]
        if fs:
            sid = b.get("SpellID", a.get("SpellID"))
            changed_names.add(sid)
            sections["Changed spells"].append((name(sid), f"- **{name(sid)}** (id {sid}) effect {eid}: " + "; ".join(f"{f} `{a.get(f,'')}`→`{b.get(f,'')}`" for f in fs)))

    # Talents and races
    for table, label in (("Talent", "Talents"), ("ChrRaces", "Races"), ("TalentTab", "Talent tabs")):
        old, new = read_table(prod, v_from, table), read_table(prod, v_to, table)
        lines = []
        for k in sorted(set(old) | set(new), key=int):
            if k not in old:
                lines.append(f"- added {label[:-1].lower()} {k}: {row_summary(new[k], name)}")
            elif k not in new:
                lines.append(f"- removed {label[:-1].lower()} {k}: {row_summary(old[k], name)}")
            else:
                d = {f: (old[k][f], new[k][f]) for f in new[k] if old[k].get(f) != new[k].get(f)}
                if d:
                    lines.append(f"- {label[:-1].lower()} {k} ({row_summary(new[k], name)}): " + "; ".join(f"{f} `{a}`→`{b}`" for f, (a, b) in d.items()))
        sections[f"{label} table"] = [("", l) for l in lines]

    def emit(title, items):
        if not items:
            return
        w = [l for n, l in items if n.lower() in watch]
        rest = [l for n, l in items if n.lower() not in watch]
        out.append(f"## {title} ({len(items)})")
        if w:
            out.append("**Watchlist**"); out.extend(sorted(set(w)))
        if rest:
            if w: out.append("\n**Other**")
            out.extend(sorted(set(rest))[:400])
            if len(rest) > 400: out.append(f"- … {len(rest)-400} more (see CSVs)")
        out.append("")
    for title in ("Changed spells", "Added spells", "Removed spells", "Talents table", "Talent tabs table", "Races table"):
        emit(title, sections.get(title, []))

    (WAGO / "diffs").mkdir(parents=True, exist_ok=True)
    dest = WAGO / "diffs" / f"{v_from}__{v_to}.md"
    dest.write_text("\n".join(out), encoding="utf-8")
    hits = sorted({name(s) for s in changed_names if name(s).lower() in watch})
    with CHANGELOG.open("a", encoding="utf-8") as f:
        f.write(f"\n## {datetime.date.today().isoformat()} — wago diff {v_from} → {v_to}\n- Source: [T2 wago {datetime.date.today().isoformat()} b:{v_to}] — {dest.relative_to(ROOT)}\n"
                f"- Watchlist spells changed: {', '.join(hits) or 'none'}\n- Knowledge files not yet updated from this diff; run forever-refresh step 4.\n")
    print(f"Wrote {dest.relative_to(ROOT)}; watchlist hits: {', '.join(hits) or 'none'}")


def spell_desc(prod, ver, sid):
    sp = read_table(prod, ver, "Spell").get(sid, {})
    return (sp.get("Description_lang") or "").replace("\n", " ")[:200]


def row_summary(r, name):
    if "SpellRank_0" in r:
        return f"{name(r.get('SpellRank_0'))} tab {r.get('TabID')} tier {r.get('TierID')} col {r.get('ColumnIndex')}"
    return r.get("Name_lang") or r.get("ClientPrefix") or ""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list-products", action="store_true")
    ap.add_argument("--probe", action="store_true")
    ap.add_argument("--snapshot", action="store_true")
    ap.add_argument("--diff", action="store_true")
    ap.add_argument("--product")
    ap.add_argument("--version")
    ap.add_argument("--from", dest="v_from")
    ap.add_argument("--to", dest="v_to")
    a = ap.parse_args()
    if a.list_products:
        return cmd_list_products()
    if a.probe:
        return cmd_probe(a.product or resolve_product(None), a.version)
    if a.snapshot:
        return cmd_snapshot(resolve_product(a.product), a.version)
    if a.diff:
        return cmd_diff(resolve_product(a.product), a.v_from, a.v_to)
    ap.print_help()


if __name__ == "__main__":
    main()
