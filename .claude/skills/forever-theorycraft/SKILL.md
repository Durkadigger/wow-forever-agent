---
name: forever-theorycraft
description: Structured method for WoW Forever race, class, spec, talent build, gear, and stat-priority comparisons. Use this whenever a member asks which race/class/spec/talent/item/enchant/consumable is best, asks to compare options, asks for a build, asks about stat weights or caps, or asks "should I go X or Y" about anything character-related — even casually phrased. Default frame is the member's class and spec from CLAUDE.local.md (Horde, Normal ruleset); ask if there is none.
---

# forever-theorycraft

## Method
1. **Restate the question in one line** with the assumed context: spec, role (raid heal / dungeon / leveling / PvP), phase (beta, launch, later raid tier).
2. **Load the relevant knowledge files.** Always `racials.md` and the class's `talents-*.md`; add `systems-legacy-servers-dates.md` for anything touching hit/crit unification, Legacy perks, or Camping buffs.
3. **List the mechanics that decide it.** For Resto Shaman today: Water Shield converts heal crits to mana (crit is a mana stat); hit is unified; Riptide buffs Chain Heal 25%; Healing Way is flat; Berserking/Blood Fury cooldowns unknown.
4. **Compare with explicit assumptions.** State which values are captured (demo), datamined, or official. Where a number is missing (cooldowns, higher ranks), say what range would flip the answer.
5. **Give a ranking with a one-line reason each**, then a "what would change this" list.
6. **Separate contexts** when they differ: raid healing, 5-man, solo leveling, PvP.
7. **Cite files** used and flag stale data (`Data as of` older than the current build).

## Classic baselines that still apply unless Forever says otherwise
- Spell hit cap 16% vs raid bosses (level 63); melee hit cap 9% (8% with weapon skill removed? — verify, weapon skill racials are gone). Hit is unified in Forever, so one number covers everything.
- Healing crit had no mana value in Classic; in Forever Water Shield changes that for Resto.
- mp5 and Spirit: Mindfulness (17% regen while casting) makes Spirit worth more than Classic Resto.
- Threat: Natural Grace −5%; Spirit Weapons on Enhancement is a tank toggle.

## Output format
Answer first, in one sentence. Short table only if 3+ options on 3+ criteria. End with "Unconfirmed:" bullets and a single trailing line naming the knowledge files used; do not scatter file paths through the prose.

## Numbers you may not state
- Higher talent ranks: only rank 1 is captured. Say "rank 1 is X; ranks 2–N not captured." Do not extrapolate, even labelled as an estimate; an estimate in the answer becomes a fact in the next conversation.
- Cooldowns, coefficients, and item stats that have no tag. Say "not in the knowledge base" and name the source that would supply it.
- Prices and dates from living pages: state them "as of <tag date>". Say "today" only if the shop was fetched in this session.

## Future extensions (add references/ files as they exist)
- `references/stat-weights-resto.md` — once beta datamines give spell coefficients
- `references/gear-preraid-resto.md`, `references/gear-raid-resto.md`
- `references/consumables.md` — Forever adds 600+ recipes; food buffs matter with Gourmand
