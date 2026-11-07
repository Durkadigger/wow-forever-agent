#!/usr/bin/env python3
"""
wago_query.py — Read a wago.tools snapshot (made by wago_diff.py --snapshot) and answer
questions from it: talent trees, the Legacy tree, racials, and single-spell lookups, with
tooltip placeholders ($s1, $d, $a1 ...) resolved to real numbers.

Tier-2 source (`wago` in sources.md). Stdlib only. Reads local CSVs; makes no requests.

  python scripts/wago_query.py spell "Blood Fury"          every spell with that name
  python scripts/wago_query.py spell 20572                 one spell id
  python scripts/wago_query.py talents shaman              print the class tree
  python scripts/wago_query.py talents all --write         write every class tree into the
                                                           Overrides block of knowledge/talents-<class>.md
  python scripts/wago_query.py legacy                      print the three Legacy trees
  python scripts/wago_query.py racials                     racial spells per race, with cooldowns

  --version X.Y.Z.N   snapshot to read (default: newest snapshot of wago_product)

WHERE FOREVER KEEPS TALENTS: in the Trait tables (TraitTree / TraitNode / TraitNodeEntry /
TraitDefinition), one tree per class, three PosX clusters = three spec tabs. The old
Talent/TalentTab tables still exist in 1.60.x but hold a half-migrated vanilla layout with
dangling spell ids. Never read talents from them.

RANKS: a multi-rank trait points at ONE spell id. Per-rank numbers come from
TraitDefinitionEffectPoints -> Curve -> CurvePoint (rank -> effect points), NOT from
multiplying rank 1: the spell row itself may hold rank 1, the max-rank total, or 0.
Every rank value this script prints is read from those curves. A multi-rank talent with
no curve is printed with the raw spell value and flagged "no per-rank curve".
"""
import argparse, collections, csv, datetime, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
WAGO = ROOT / "data" / "wago"
BUILDS = ROOT / "data" / "builds.json"
KNOW = ROOT / "knowledge"

CLASS_BY_MASK = {1: "warrior", 2: "paladin", 4: "hunter", 8: "rogue", 16: "priest",
                 64: "shaman", 128: "mage", 256: "warlock", 1024: "druid"}
LEVEL = 60   # character level used for per-level spell scaling
RACE_BITS = {1: "Human", 2: "Orc", 3: "Dwarf", 4: "Night Elf", 5: "Undead", 6: "Tauren", 7: "Gnome", 8: "Troll"}


def build_no(v):
    t = v.rsplit(".", 1)[-1]
    return int(t) if t.isdigit() else 0


class Snap:
    def __init__(self, version=None):
        b = json.loads(BUILDS.read_text(encoding="utf-8"))
        self.product = b.get("wago_product")
        if not self.product:
            raise SystemExit("wago_product is not set in data/builds.json. Run wago_diff.py --probe first.")
        base = WAGO / self.product
        snaps = sorted([p.name for p in base.iterdir() if p.is_dir()], key=build_no) if base.exists() else []
        if not snaps:
            raise SystemExit(f"No snapshots under {base}. Run: python scripts/wago_diff.py --snapshot")
        self.version = version or snaps[-1]
        self.dir = base / self.version
        if not self.dir.exists():
            raise SystemExit(f"No snapshot for {self.version}; have {snaps}")
        self._cache = {}

    def rows(self, table):
        if table not in self._cache:
            f = self.dir / f"{table}.csv"
            self._cache[table] = list(csv.DictReader(f.open(encoding="utf-8"))) if f.exists() else []
        return self._cache[table]

    def index(self, table, key="ID"):
        k = (table, key, "idx")
        if k not in self._cache:
            self._cache[k] = {r[key]: r for r in self.rows(table) if r.get(key)}
        return self._cache[k]

    def group(self, table, key):
        k = (table, key, "grp")
        if k not in self._cache:
            g = collections.defaultdict(list)
            for r in self.rows(table):
                g[r.get(key, "")].append(r)
            self._cache[k] = g
        return self._cache[k]

    # ---- spell facts -------------------------------------------------------
    def name(self, sid):
        return self.index("SpellName").get(str(sid), {}).get("Name_lang") or f"spell {sid}"

    def effects(self, sid):
        return sorted(self.group("SpellEffect", "SpellID").get(str(sid), []), key=lambda e: int(e["EffectIndex"]))

    def effect(self, sid, n):
        for e in self.effects(sid):
            if int(e["EffectIndex"]) == n - 1:
                return e
        return None

    def misc(self, sid):
        m = self.group("SpellMisc", "SpellID").get(str(sid), [])
        return m[0] if m else {}

    def duration_ms(self, sid):
        d = self.index("SpellDuration").get(self.misc(sid).get("DurationIndex", ""), {})
        try:
            return int(d.get("Duration", 0))
        except ValueError:
            return 0

    def cooldown_s(self, sid):
        c = self.group("SpellCooldowns", "SpellID").get(str(sid), [])
        if not c:
            return None
        return max(int(c[0]["RecoveryTime"]), int(c[0]["CategoryRecoveryTime"])) / 1000

    def cast_s(self, sid):
        c = self.index("SpellCastTimes").get(self.misc(sid).get("CastingTimeIndex", ""), {})
        try:
            return int(c.get("Base", 0)) / 1000
        except ValueError:
            return 0

    def range_yd(self, sid):
        r = self.index("SpellRange").get(self.misc(sid).get("RangeIndex", ""), {})
        try:
            return float(r.get("RangeMax_0", 0))
        except ValueError:
            return 0

    def cost(self, sid):
        p = self.group("SpellPower", "SpellID").get(str(sid), [])
        if not p:
            return ""
        p = p[0]
        kind = {"0": "mana", "1": "rage", "3": "energy"}.get(p.get("PowerType", "0"), "power")
        if int(float(p.get("ManaCost", 0) or 0)):
            v = int(float(p["ManaCost"]))
            return f"{v // 10 if kind == 'rage' else v} {kind}"
        pct = float(p.get("PowerCostPct", 0) or 0)
        return f"{pct:g}% of base {kind}" if pct else ""

    # ---- tooltip resolution ------------------------------------------------
    def _pts(self, sid, n, pts):
        """Effect points for effect n (1-based). `pts` = {(spell id, 0-based effect index): value}
        per-rank overrides from the trait curves."""
        if pts and (str(sid), n - 1) in pts:
            return abs(pts[(str(sid), n - 1)])
        e = self.effect(sid, n)
        if not e:
            return None
        v = abs(float(e["EffectBasePointsF"]))
        per = float(e.get("EffectRealPointsPerLevel", 0) or 0)
        if per:
            # Average value at LEVEL: base + per-level growth from BaseLevel, capped at MaxLevel.
            lv = (self.group("SpellLevels", "SpellID").get(str(sid)) or [{}])[0]
            base, cap = int(lv.get("BaseLevel", 0) or 0), int(lv.get("MaxLevel", 0) or 0)
            v += per * max(0, (min(LEVEL, cap) if cap else LEVEL) - base)
        return v

    def _variance(self, sid, n):
        e = self.effect(sid, n)
        return float(e.get("Variance", 0) or 0) if e else 0.0

    def _val(self, sid, tok, n, pts=None):
        """Numeric value of one placeholder, or None if we cannot resolve it."""
        t = tok.lower()
        if t in ("s", "m", "w"):
            return self._pts(sid, n or 1, pts)
        if t == "o":
            e, v = self.effect(sid, n or 1), self._pts(sid, n or 1, pts)
            if not e or v is None:
                return None
            per, dur = int(e.get("EffectAuraPeriod", 0) or 0), self.duration_ms(sid)
            return v * (dur // per if per else 1)
        if t == "t":
            e = self.effect(sid, n or 1)
            return int(e.get("EffectAuraPeriod", 0) or 0) / 1000 if e else None
        if t == "a":
            e = self.effect(sid, n or 1)
            if not e:
                return None
            for col in ("EffectRadiusIndex_0", "EffectRadiusIndex_1"):   # either slot may hold it
                r = self.index("SpellRadius").get(e.get(col, ""), {})
                if r.get("Radius") and float(r["Radius"]):
                    return float(r["Radius"])
            return None
        if t == "x":
            e = self.effect(sid, n or 1)
            return float(e.get("EffectChainTargets", 0)) if e else None
        if t == "d":
            ms = self.duration_ms(sid)
            return ms / 1000 if ms else None
        ao = (self.group("SpellAuraOptions", "SpellID").get(str(sid)) or [{}])[0]
        if t == "h":
            return float(ao["ProcChance"]) if ao.get("ProcChance") else None
        if t == "n":
            return float(ao["ProcCharges"]) if ao.get("ProcCharges") else None
        if t == "u":
            return float(ao["CumulativeAura"]) if ao.get("CumulativeAura") else None
        if t == "i":
            tr = (self.group("SpellTargetRestrictions", "SpellID").get(str(sid)) or [{}])[0]
            return float(tr["MaxTargets"]) if tr.get("MaxTargets") else None
        return None

    @staticmethod
    def _fmt(v, places=None):
        if v is None:
            return "?"
        if places is not None:
            return f"{v:.{places}f}"
        return f"{v:.2f}".rstrip("0").rstrip(".") if abs(v - round(v)) > 1e-9 else str(int(round(v)))

    @staticmethod
    def _dur(sec):
        if sec is None:
            return "?"
        if sec >= 3600 and sec % 3600 == 0:
            return f"{int(sec // 3600)} hr"
        if sec >= 60 and sec % 60 == 0:
            return f"{int(sec // 60)} min"
        return f"{Snap._fmt(sec)} sec"

    def resolve(self, sid, text, pts=None):
        """Replace placeholders in tooltip text. `pts` = per-rank effect-point overrides."""
        if not text:
            return ""
        sid = str(sid)
        text = text.replace("\r", "").replace("\n", " ")
        def atom(m):
            div, ref, tok, n = m.group("div"), m.group("ref"), m.group("tok"), m.group("n")
            if ref and ref not in self.index("SpellName"):
                ref = None   # dangling cross-reference (e.g. Berserking -> 26635): fall back to this spell
            v = self._val(ref or sid, tok, int(n) if n else 0, pts)
            if v is None:
                return m.group(0)
            if div:
                v /= float(div)
            var = self._variance(ref or sid, int(n) if n else 1) if tok in ("s", "S") and not div else 0
            if var:   # damage/heal roll: average +/- variance/2, as the in-game tooltip shows it
                return f"{self._fmt(round(v * (1 - var / 2)))}–{self._fmt(round(v * (1 + var / 2)))}"
            if tok.lower() in ("s", "m", "o") and abs(v) >= 20:
                v = round(v)
            return self._dur(v) if tok.lower() == "d" and not div else self._fmt(v)

        ATOM = r"\$(?:/(?P<div>\d+);)?(?P<ref>\d+)?(?P<tok>[smwotaxdhnuiSMWOTAXDHNUI])(?P<n>\d)?(?![A-Za-z])"

        def expr(m):
            body, places = m.group(1), m.group(2)
            def num(a):
                v = self._val(a.group("ref") or sid, a.group("tok"), int(a.group("n")) if a.group("n") else 0, pts)
                return "nan" if v is None else repr(v)
            py = re.sub(ATOM, num, body)
            if not re.fullmatch(r"[0-9eE+\-*/(). nan]+", py):
                return m.group(0)
            try:
                v = abs(eval(py, {"__builtins__": {}}, {"nan": float("nan")}))
            except Exception:
                return m.group(0)
            return m.group(0) if v != v else self._fmt(v, int(places) if places else None)

        text = re.sub(r"\$\{([^{}]+)\}(?:\.(\d))?", expr, text)
        text = re.sub(ATOM, atom, text)
        text = re.sub(r"\$l([^:;]+):([^;]+);", lambda m: m.group(2), text)      # plural forms
        text = re.sub(r"\$g([^:;]+):([^;]+);", lambda m: m.group(1), text)      # gendered forms
        return re.sub(r"\s{2,}", " ", text).strip()

    def tooltip(self, sid, pts=None):
        return self.resolve(sid, self.index("Spell").get(str(sid), {}).get("Description_lang", ""), pts)

    def rank_points(self, definition_id, sid, rank):
        """{(sid, effect index): points} at `rank`, from TraitDefinitionEffectPoints curves."""
        out = {}
        for r in self.group("TraitDefinitionEffectPoints", "TraitDefinitionID").get(str(definition_id), []):
            pts = self.group("CurvePoint", "CurveID").get(r["CurveID"], [])
            hit = [p for p in pts if abs(float(p["Pos_0"]) - rank) < 1e-6]
            if hit:
                out[(str(sid), int(r["EffectIndex"]))] = float(hit[0]["Pos_1"])
        return out

    def header(self, sid):
        """Cost / range / cast / cooldown line for an active ability; '' for passives."""
        bits = [self.cost(sid)]
        coeff = [f"{float(e['EffectBonusCoefficient']):.3g}" for e in self.effects(sid)
                 if e["Effect"] in ("2", "10") or (e["Effect"] == "6" and e["EffectAura"] in ("3", "8"))
                 if float(e.get("EffectBonusCoefficient", 0) or 0) not in (0.0, 1.0)]
        if self.range_yd(sid):
            bits.append(f"{self.range_yd(sid):g} yd")
        if self.cast_s(sid):
            bits.append(f"{self.cast_s(sid):g} sec cast")
        cd = self.cooldown_s(sid)
        if cd:
            bits.append(f"{self._dur(cd)} CD")
        if coeff:
            bits.append(f"spell power coeff {'/'.join(coeff)}; numbers are level {LEVEL} with 0 spell power")
        return ", ".join(b for b in bits if b)

    # ---- trait trees -------------------------------------------------------
    def class_trees(self):
        """{class_name: TraitTreeID} via SkillLineXTraitTree -> SkillRaceClassInfo.ClassMask."""
        mask_by_skill = {}
        for r in self.rows("SkillRaceClassInfo"):
            mask_by_skill.setdefault(r["SkillID"], int(r["ClassMask"]))
        out = {}
        for r in self.rows("SkillLineXTraitTree"):
            cls = CLASS_BY_MASK.get(mask_by_skill.get(r["SkillLineID"], 0))
            if cls:
                out[cls] = r["TraitTreeID"]
        return out

    def tab_names(self, cls):
        mask = next(m for m, c in CLASS_BY_MASK.items() if c == cls)
        tabs = [t for t in self.rows("TalentTab") if int(t["ClassMask"]) == mask]
        return [t["Name_lang"] for t in sorted(tabs, key=lambda t: int(t["OrderIndex"]))]

    def tree(self, tree_id):
        """List of talents: dict(tab, row, col, name, ranks, spell, node, requires)."""
        nodes = [n for n in self.rows("TraitNode") if n["TraitTreeID"] == str(tree_id)]
        if not nodes:
            return []
        n2e = self.group("TraitNodeXTraitNodeEntry", "TraitNodeID")
        ent, de = self.index("TraitNodeEntry"), self.index("TraitDefinition")
        xs = sorted({int(n["PosX"]) for n in nodes})
        ys = sorted({int(n["PosY"]) for n in nodes})
        # Class trees share one fixed grid: tab origins at x=1020 / 5020 / 9080, columns 600
        # apart. Legacy trees (one tab) use the same column step from their own minimum x.
        # 1.60.1 has a Hunter node at x=102800, a data typo for 10280; fold such outliers back.
        fix = lambda x: x // 10 if x > 20000 else x
        if max(fix(x) for x in xs) > 8000:
            origin = lambda x: (9080, 2) if fix(x) > 8000 else (5020, 1) if fix(x) > 4000 else (1020, 0)
        else:
            lo = min(xs)
            origin = lambda x: (lo, 0)
        tab_of = {x: origin(x)[1] for x in xs}
        first_x = {x: origin(x)[0] for x in xs}
        node_name = {}
        out = []
        for n in nodes:
            for link in n2e.get(n["ID"], []):
                e = ent.get(link["TraitNodeEntryID"])
                d = de.get(e["TraitDefinitionID"]) if e else None
                if not d:
                    continue
                sid = d["SpellID"]
                nm = d.get("OverrideName_lang") or self.name(sid)
                node_name[n["ID"]] = nm
                x = int(n["PosX"])
                out.append(dict(tab=tab_of[x], row=ys.index(int(n["PosY"])) + 1,
                                col=round((fix(x) - first_x[x]) / 600) + 1, name=nm,
                                ranks=int(e["MaxRanks"]), spell=sid, node=n["ID"], requires=[], definition=d["ID"],
                                override_desc=d.get("OverrideDescription_lang", "")))
        by_node = {t["node"]: t for t in out}
        for ed in self.rows("TraitEdge"):
            if ed["RightTraitNodeID"] in by_node and ed["LeftTraitNodeID"] in node_name:
                by_node[ed["RightTraitNodeID"]]["requires"].append(node_name[ed["LeftTraitNodeID"]])
        return sorted(out, key=lambda t: (t["tab"], t["row"], t["col"]))

    @staticmethod
    def _merge(texts):
        """Fold per-rank tooltips into one line: numbers that differ become a/b/c."""
        NUM = r"\d+(?:\.\d+)?"
        skel = [re.sub(NUM, "#", t) for t in texts]
        if len(set(skel)) != 1:
            return None
        cols = list(zip(*[re.findall(NUM, t) for t in texts]))
        it = iter(cols)
        return re.sub("#", lambda m: (lambda c: c[0] if len(set(c)) == 1 else "/".join(c))(next(it)), skel[0])

    def talent_line(self, t):
        sid, r = t["spell"], t["ranks"]
        raw = t["override_desc"] or self.index("Spell").get(str(sid), {}).get("Description_lang", "")
        texts = [self.resolve(sid, raw, self.rank_points(t["definition"], sid, k)) for k in range(1, r + 1)]
        has_curve = bool(self.rank_points(t["definition"], sid, 1))
        body = self._merge(texts) or " | ".join(f"R{k}: {x}" for k, x in enumerate(texts, 1))
        line = f"- {t['name']} [{r}] — "
        hdr = self.header(sid)
        if hdr:
            line += hdr + ". "
        line += body or "(no tooltip text in this build)"
        if r > 1 and not has_curve:
            line += " *(no per-rank curve in data; number shown is the raw spell value)*"
        if t["requires"]:
            line += f" *(requires {', '.join(t['requires'])})*"
        return line + f" `id {sid}`"


# ---- commands ---------------------------------------------------------------
def render_class(s, cls, tag):
    tid = s.class_trees().get(cls)
    if not tid:
        raise SystemExit(f"No trait tree mapped to class '{cls}'. Known: {sorted(s.class_trees())}")
    tal, tabs = s.tree(tid), s.tab_names(cls)
    out = [f"*Full datamined tree, TraitTree {tid}. {tag} applies to every line in this block. Values written a/b/c are "
           f"ranks 1/2/3, each read from the client's per-rank curves (TraitDefinitionEffectPoints), not extrapolated.*", ""]
    for i in sorted({t["tab"] for t in tal}):
        mine = [t for t in tal if t["tab"] == i]
        out.append(f"### {tabs[i] if i < len(tabs) else f'Tab {i+1}'} — datamined ({len(mine)} talents, {sum(t['ranks'] for t in mine)} points)")
        row = None
        for t in mine:
            if t["row"] != row:
                row = t["row"]
                out += ["", f"**R{row}**"]
            out.append(s.talent_line(t))
        out.append("")
    return out


def cmd_talents(s, which, write):
    today = datetime.date.today().isoformat()
    tag = f"[T2 wago {today} b:{s.version}]"
    classes = sorted(s.class_trees()) if which == "all" else [which]
    for cls in classes:
        body = render_class(s, cls, tag)
        if not write:
            print(f"\n##### {cls.upper()}  {tag}\n" + "\n".join(body))
            continue
        path = KNOW / f"talents-{cls}.md"
        txt = path.read_text(encoding="utf-8")
        if not re.search(r"<!-- overrides -->.*?<!-- /overrides -->", txt, re.S):
            raise SystemExit(f"{path.name} has no overrides block; not touching it.")
        # Keep hand-written note sections (staff-post notes etc.): any "### " section inside the block
        # whose heading is not a generated "— datamined (" tree section. Re-inserted after the italic header.
        old_block = re.search(r"<!-- overrides -->(.*?)<!-- /overrides -->", txt, re.S).group(1)
        kept = [m.group(0).rstrip() for m in
                re.finditer(r"^### (?![^\n]*— datamined \().*?(?=^### |\Z)", old_block, re.S | re.M)]
        if kept:
            body = body[:2] + [x + "\n" for x in kept] + body[2:]
        block = "\n".join(["<!-- overrides -->", "## Overrides (tier 1–2 values that outrank the generated lines)", *body,
                           "<!-- /overrides -->"])
        txt = re.sub(r"<!-- overrides -->.*?<!-- /overrides -->", lambda m: block, txt, count=1, flags=re.S)
        gen = re.search(r"\[T3 cwf (\d{4}-\d{2}-\d{2}) b:(\S+?)\]", txt)
        gen_label = f"{gen.group(1)} b:{gen.group(2)}" if gen else "2026-09-15 b:blizzcon-demo"
        txt = re.sub(r"^Data as of: .*$",
                     lambda m: f"Data as of: {today} b:{s.version} (Overrides block: datamined, tier 2). Generated lines below the block: "
                     f"{gen_label}, tier 3, superseded wherever the block covers the same talent.",
                     txt, count=1, flags=re.M)
        path.write_text(txt, encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")


def cmd_legacy(s):
    sys45 = [t["ID"] for t in s.rows("TraitTree") if t.get("TraitSystemID") == "45"]
    for tid in sys45:
        tal = s.tree(tid)
        if not tal:
            continue
        print(f"\n## Legacy tree {tid} ({len(tal)} perks, {sum(t['ranks'] for t in tal)} points)")
        for t in tal:
            print(f"R{t['row']}c{t['col']} " + s.talent_line(t)[2:])


def cmd_spell(s, q):
    ids = [q] if q.isdigit() else sorted((i for i, r in s.index("SpellName").items() if r["Name_lang"].lower() == q.lower()), key=int)
    if not ids:
        print(f"No spell named '{q}' in {s.version}.")
    for sid in ids:
        print(f"[{sid}] {s.name(sid)} | {s.header(sid) or 'passive / no cost row'}")
        print(f"    {s.tooltip(sid) or '(no description)'}")
        aura = s.resolve(sid, s.index('Spell').get(sid, {}).get('AuraDescription_lang', ''))
        if aura:
            print(f"    aura: {aura}")
        for e in s.effects(sid):
            print(f"    effect {int(e['EffectIndex'])+1}: Effect={e['Effect']} Aura={e['EffectAura']} points={e['EffectBasePointsF']} "
                  f"misc={e['EffectMiscValue_0']} coeff={e['EffectBonusCoefficient']} trigger={e['EffectTriggerSpell']}")


def cmd_racials(s):
    skill_name = {r["ID"]: r["DisplayName_lang"] for r in s.rows("SkillLine")}
    racial_skills = {}
    for r in s.rows("SkillRaceClassInfo"):
        nm = skill_name.get(r["SkillID"], "")
        if nm.startswith("Racial") or "Racial" in nm:
            racial_skills[r["SkillID"]] = nm
    for sk, nm in sorted(racial_skills.items(), key=lambda kv: kv[1]):
        print(f"\n## {nm} (skill {sk})")
        seen = set()
        for a in s.group("SkillLineAbility", "SkillLine").get(sk, []):
            sid = a["Spell"]
            if sid in seen or sid not in s.index("SpellName"):
                continue
            seen.add(sid)
            hdr = s.header(sid)
            print(f"- {s.name(sid)}{' — ' + hdr if hdr else ''}: {s.tooltip(sid) or '(no text)'} `id {sid}`")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["spell", "talents", "legacy", "racials"])
    ap.add_argument("arg", nargs="?")
    ap.add_argument("--version")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    s = Snap(a.version)
    if a.cmd == "spell":
        if not a.arg:
            ap.error("spell needs a name or id")
        return cmd_spell(s, a.arg)
    if a.cmd == "talents":
        return cmd_talents(s, (a.arg or "all").lower(), a.write)
    if a.cmd == "legacy":
        return cmd_legacy(s)
    return cmd_racials(s)


if __name__ == "__main__":
    main()
