# wow-forever-agent — Plague guild edition

A Claude Code agent that keeps a World of Warcraft: Forever knowledge base current and answers race, spec, talent, gear, quest and strategy questions from it. Built for the **Plague** guild (Horde, Normal ruleset) and maintained by the maintainer.

Every fact in `knowledge/` carries a source tag (`[T<tier> <source-id> <date> b:<build>]`), so the agent can tell you what Blizzard confirmed, what was datamined, and what is only a rumour. Talents, racials and Legacy perks are read straight from the game client's data tables on wago.tools; Blizzard forum staff posts are pulled by script.

## Setting it up (guild members)
You need your own Claude Code subscription. Nothing is hosted; the agent runs on your machine.

1. Install [Claude Code](https://claude.com/claude-code) (desktop app, or `npm install -g @anthropic-ai/claude-code`), plus `git` and Python 3.9+. On Windows, `winget install Git.Git GitHub.cli Python.Python.3.12` does it.
2. Clone the repo:
   ```bash
   git clone https://github.com/Durkadigger/wow-forever-agent.git
   ```
3. Download the current game-data snapshot (large, git-ignored, takes a minute):
   ```bash
   python scripts/wago_diff.py --snapshot
   ```
4. Create your personal profile, `CLAUDE.local.md`, in the project folder. It is git-ignored and never leaves your machine. Template:
   ```markdown
   # CLAUDE.local.md — my profile
   - Name / handle: ...
   - Main: <race> <class>, <spec> (e.g. Orc Warrior, Protection). Alts: ...
   - Goals: levelling / dungeons / raiding / PvP
   - Anything else the agent should know (play style, what you forget to press, gold, current weapon)
   ```
5. Open the folder in Claude Code (desktop app) or run `claude` in it. It reads `CLAUDE.md` and your `CLAUDE.local.md` automatically.

On Windows, set `$env:PYTHONIOENCODING='utf-8'` before running the scripts, or they can crash printing arrows.

## Using it
Ask in plain English. Examples:
- "Which race for an Enhancement Shaman?" / "Orc or Troll for Resto?" → runs `forever-theorycraft`
- "Is the knowledge base current?" / "What changed in today's hotfix?" → runs `forever-refresh`
- Paste a screenshot of two item tooltips: "which is better for my Prot Warrior?"
- "Give me a levelling talent order from 10 for Frost Mage"
- "What does Touch of the Grave do now?"

The agent leads with the answer, then the reasoning, then what is unconfirmed, and names the knowledge file it used.

## Contributing
Pull requests only; `main` is maintained by the repo owner (`Durkadigger`).
- Game facts go in `knowledge/`, each with a source tag (rules in `docs/sop-provenance.md`). Personal stuff stays in your `CLAUDE.local.md`.
- Run `python scripts/lint_knowledge.py` before opening a PR; it checks tags, build labels and untagged values.
- Add a dated line to `CHANGELOG.md` saying what changed and from which source.
- Easiest route: ask the agent itself to "commit this on a branch and open a pull request". It knows the rules.

## Scripts
- `python scripts/forum_scan.py` — new Blizzard staff posts about Forever (tier 1)
- `python scripts/wago_diff.py --list-products | --snapshot | --diff` — snapshot and diff the client's data tables between builds (tier 2)
- `python scripts/wago_query.py talents <class> | racials | legacy | spell "<name>"` — read values from a snapshot
- `python scripts/fetch_talents.py --dry-run` — re-scrape the classicwowforever.com talent calculator (tier 3)
- `python scripts/lint_knowledge.py` — check every knowledge file obeys the provenance SOP
- `python scripts/install_addon.py` / `read_addon_data.py` — the optional read-only in-game addon (`addon/WFATest`)

## Layout
```
CLAUDE.md                      agent instructions, guild context, source hierarchy, sync rules
CLAUDE.local.md                your profile (git-ignored; you create it)
knowledge/                     the knowledge base (INDEX.md is the map)
knowledge/gear/, quests/       per-spec gear notes and quest chains
data/talents.json              machine-readable talents (generated)
data/builds.json               build registry; newest entry = current build
data/wago/, data/forum/        DB2 snapshots + diffs; staff forum posts (generated)
docs/sop-provenance.md         citation tags, precedence rules, build tracking
docs/addon-feasibility.md      what addons can and cannot read in Forever
docs/wargame/                  red-team question sets and results
scripts/                       scrapers, diffs, lint, addon tools
addon/WFATest/                 read-only in-game addon
.claude/skills/                forever-refresh, forever-theorycraft
.claude/agents/                refresh-scout (cheap scrape/diff), theorycrafter (deep analysis)
sources.md                     ranked source list
CHANGELOG.md                   dated record of every refresh
```

## Model guidance
- Refresh / scraping / diffing: Claude Sonnet 5
- Theorycraft / strategy / build design: Claude Opus 5 or Fable 5.1
- Bulk reformatting: Claude Haiku 4.5

## Licence
MIT (see `LICENSE`). Not affiliated with Blizzard Entertainment. World of Warcraft is a trademark of Blizzard Entertainment, Inc.
