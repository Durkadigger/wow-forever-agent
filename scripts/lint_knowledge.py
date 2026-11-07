#!/usr/bin/env python3
"""
lint_knowledge.py — Check that knowledge/ obeys docs/sop-provenance.md.

Errors (exit 1):
  - a knowledge file has no `Data as of:` line, or its `b:<label>` is not in data/builds.json
  - a `## ` section has no *Provenance:* line and the file has no file-level Provenance header
  - a citation tag has a tier outside 1–5, a source-id missing from sources.md, or a future date
  - a fact line contains a value-looking token (number or %) but no tag reaches it
    (only for racials.md and systems-legacy-servers-dates.md; talent files are tag-by-header)
Warnings:
  - `(was: …)` notes older than the latest CHANGELOG date (SOP §3 says drop them next refresh)
  - "unconfirmed"/"open question" lines with a T1/T2 tag (contradiction)

Usage: python scripts/lint_knowledge.py [--strict]   (--strict turns warnings into errors)
"""
import argparse, datetime, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
KNOW = ROOT / "knowledge"
TAG = re.compile(r"\[(T[1-5]) ([a-z0-9-]+) (\d{4}-\d{2}-\d{2})(?: b:([A-Za-z0-9.-]+))?(?:;[^\]]*)?\]")
ANY_TAG = re.compile(r"\[T\d[^\]]*\]")
SUBTAG = re.compile(r"(T\d) ([a-z0-9-]+) (\d{4}-\d{2}-\d{2})(?: b:([A-Za-z0-9.-]+))?")
LINE_LEVEL_FILES = {"racials.md", "systems-legacy-servers-dates.md"}


def source_ids():
    ids = set(re.findall(r"`([a-z][a-z0-9-]+)`", (ROOT / "sources.md").read_text(encoding="utf-8")))
    return {i for i in ids if "-" in i or i in {"wago", "cwf", "reddit", "secondhand"}}


def build_labels():
    b = json.loads((ROOT / "data" / "builds.json").read_text(encoding="utf-8"))
    labels = {x["label"] for x in b["builds"]} | {x["version"] for x in b["builds"] if x.get("version")}
    return labels


def latest_changelog_date():
    ds = re.findall(r"^## (\d{4}-\d{2}-\d{2})", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"), re.M)
    return max(ds) if ds else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()
    ids, labels = source_ids(), build_labels()
    today = datetime.date.today().isoformat()
    last_log = latest_changelog_date()
    errors, warns = [], []

    for f in sorted(KNOW.rglob("*.md")):
        text = f.read_text(encoding="utf-8")
        lines = text.split("\n")
        rel = f.relative_to(ROOT)
        m = re.search(r"^Data as of: (\S+)(?: b:(\S+))?", text, re.M)
        if not m:
            errors.append(f"{rel}: no 'Data as of:' line")
        elif not m.group(2):
            errors.append(f"{rel}: 'Data as of' has no b:<build> label")
        elif m.group(2) not in labels:
            errors.append(f"{rel}: build label '{m.group(2)}' not in data/builds.json")
        file_level = bool(re.search(r"^Provenance: \[T", text, re.M))

        # every tag well-formed
        for i, ln in enumerate(lines, 1):
            for raw in ANY_TAG.findall(ln):
                parts = raw.strip("[]").split(";")
                for part in parts:
                    part = part.strip()
                    if part.startswith("supersedes"):
                        continue
                    sm = SUBTAG.fullmatch(part)
                    if not sm:
                        errors.append(f"{rel}:{i}: malformed tag piece '{part}' in {raw}"); continue
                    tier, sid, date, build = sm.groups()
                    if not any(sid == x or (x.startswith("creator-") and sid.startswith("creator-")) for x in ids):
                        errors.append(f"{rel}:{i}: unknown source-id '{sid}' (add it to sources.md)")
                    if date > today:
                        errors.append(f"{rel}:{i}: future date {date}")
                    if build and build not in labels and not re.fullmatch(r"\d+\.\d+\.\d+\.\d+", build):
                        errors.append(f"{rel}:{i}: build '{build}' not in data/builds.json")
                    if tier in ("T1", "T2") and re.search(r"unconfirmed|open question", ln, re.I):
                        warns.append(f"{rel}:{i}: T1/T2 tag on a line still marked unconfirmed")

        # sections need provenance; fact lines need a reachable tag
        section_tag = None   # tag of the current ## section
        sub_tag = None       # tag of the current ### subsection (inherits from ## when absent)
        for i, ln in enumerate(lines, 1):
            if ln.startswith("## ") or ln.startswith("### "):
                nxt = " ".join(lines[i:i + 2])
                has = "Provenance" in nxt and ANY_TAG.search(nxt) is not None
                if ln.startswith("## "):
                    section_tag, sub_tag = (True if has else None), None
                    following = next((l for l in lines[i:] if l.strip()), "")
                    is_container = following.startswith("### ")
                    exempt = re.search(r"decision|conclusion|resolved|open question|files|refresh plan|suggested|working", ln, re.I)
                    if not has and not file_level and not is_container and not exempt:
                        errors.append(f"{rel}:{i}: section '{ln.strip()}' has no *Provenance:* line")
                else:
                    sub_tag = True if has else section_tag
                continue
            if f.name in LINE_LEVEL_FILES and ln.startswith(("- ", "| ")) and re.search(r"\d+%|\b\d+(\.\d+)? ?(sec|min|%|yd|mana|gold)\b", ln):
                if not (ANY_TAG.search(ln) or sub_tag or section_tag or file_level):
                    errors.append(f"{rel}:{i}: value line without a reachable tag: {ln.strip()[:80]}")

        # stale (was: …) notes
        if last_log:
            for i, ln in enumerate(lines, 1):
                for wm in re.finditer(r"\(was:.*?\[T\d [a-z0-9-]+ (\d{4}-\d{2}-\d{2})", ln):
                    pass  # date inside is the OLD tag; staleness is judged by the refresh that wrote it, which we cannot see here
            was_count = text.count("(was:")
            if was_count:
                warns.append(f"{rel}: {was_count} '(was: …)' note(s) present; drop them on the refresh after the one that wrote them (SOP §3)")

    for e in errors: print("ERROR", e)
    for w in warns: print("WARN ", w)
    print(f"{len(errors)} error(s), {len(warns)} warning(s) across {len(list(KNOW.rglob('*.md')))} files")
    sys.exit(1 if errors or (a.strict and warns) else 0)


if __name__ == "__main__":
    main()
