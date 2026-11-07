# In-game theory — predictions written before the data

Written 18 Sept 2026 for build 1.60.1.69913, before any in-game run. Each test states the hypotheses, what each would look like in the numbers, what would make the run worthless, and which decision it moves. `python scripts/read_addon_data.py --verdict` applies these rules mechanically, so the answer cannot drift toward what we hoped for.

Nothing in this file is a game fact. Reasoning from how the modern engine usually behaves is marked **expectation** and carries no tier. Only a result filed as `[T2 in-game …]` or a Blizzard statement goes into `knowledge/`.

## The constraint: fresh low-level characters
The maintainer is testing on new characters played up to their first heals (Healing Wave at level 1; beta cap 20 this week [T1 blizz-news 2026-09-17]). A level 1–10 character has roughly zero spell power and zero +healing. That splits the tests cleanly:

| Answerable at level 1–10 | Needs spell power (about 30+, better 100+) | Needs talent points or the cap raised |
|---|---|---|
| T0 addon loads, interface number | **T1 Blood Fury and healing** | Tidal Focus hit, Thundering Strikes crit (level 10+) |
| T2 combat secrecy | Riptide coefficients | Water Shield (row 3, about level 20) |
| T3 healing vs damage stat (weak form) | Downranking penalty | Riptide, Mana Tide, Nature's Swiftness, Legacy (25+) |
| T4 Berserking haste maths (Troll) | Purification scope | |
| T5 Blood Fury positive control (attack power) | | |
| T6 both factions in one ruleset (character creation) | | |
| T7 Rapid Regeneration rules (Troll) | | |
| T8 live tooltip vs datamine, Healing Wave rank 1 | | |

**So the first session cannot settle Orc vs Troll, and the tools now say so instead of guessing.** `/wfa go` warns when healing bonus is under 30, and `--verdict` returns INCONCLUSIVE. A percent buff on nothing is nothing: 10% of 6 spell power is 0.6, which the client rounds away.

## T1 — Does Blood Fury raise healing? (open question #1, the race decision)
Datamined: Blood Fury applies three 10-point auras, 166 (attack power %), 167 (ranged attack power %) and 317 (spell power %), and no separate healing aura [T2 wago 2026-09-18 b:1.60.1.69913].

- **H1a — yes, fully.** Healing bonus rises about 10% during the buff, same as spell damage. *Expectation:* this is the likeliest outcome if Forever has one Spell Power stat, because in the modern engine aura 317 scales that single stat and heals read from it. The tooltip saying "Spell Power" rather than "spell damage" points the same way.
- **H1b — partly.** Healing rises by less than 10%. That would mean the healing bonus is made of spell power plus a separate "+healing" pool, and only the spell power part scales. Orc's value would then depend on how Forever itemises healers.
- **H0 — no.** Spell damage rises 10%, healing stays flat. Troll remains the raid pick.

Valid run: Blood Fury (20572) appears in the buff list or attack power moves (the positive control, T5); baseline healing bonus at least 30; reads not secret. Verdict thresholds: rise of 8% or more is YES, 1% or less with damage up is NO, anything between is PARTIAL.

Decision: YES moves Orc ahead of Troll for raid healing (10% for 15 sec every 2 min, plus Shatter Curse, against Berserking 10% haste for 10 sec every 3 min). NO or PARTIAL leaves the maintainer's current ranking alone.

Cheapest way to reach 30 healing bonus on a beta character: **not known.** Candidates to look for while levelling are "of Healing" greens, a spell power weapon oil, and any spell power buff from the new Camping system. None is verified in Forever. Otherwise this waits for the cap to reach 30.

Fallback if stat reads turn out secret: combat log, 20+ non-crit casts of one heal rank on one target per arm, buff on vs off. Same spell power requirement.

## T2 — When do stat reads go secret?
Forever uses retail's secret-value rules (`docs/addon-feasibility.md`). Unknown is *where* they switch on. Outcomes: readable everywhere; secret in combat only; secret inside instances even out of combat. `/wfa go` takes the in-combat snapshot by itself on the first mob hit. Decision: sets the method for every later test. If combat is secret, all stat work is out of combat and per-heal numbers come only from `/combatlog`.

## T3 — Is healing one stat with spell damage?
Weak form (any level): are healing bonus and every school's damage bonus identical at baseline? Identical supports one stat but at zero it proves nothing, since 0 = 0. Strong form: snapshot with and without a +healing-only item. Decision: whether gear weights carry one stat or two, and whether H1b is even possible.

## T4 — Berserking: 10% haste, which maths?
Troll. Read spell haste before and during. If the client reports 10% haste, a 1.5 sec Healing Wave becomes 1.5 / 1.10 = 1.364 sec. If it is a flat 10% cast time reduction it becomes 1.35 sec. The Healing Wave tooltip cast time tells them apart at any level. *Expectation:* 1.36 (haste rating style), which makes Berserking about 9.1% faster casting, not 10%. Decision: the Troll side of the race comparison.

## T5 — Blood Fury positive control
Orc, any level. Attack power must rise about 10% during the buff. If it does not, the button press was missed or aura reads are hidden, and T1 is void whatever healing did.

## T6 — Both factions in one ruleset (open question #3)
No character needed: try creating an Alliance character on the account that already has a Horde one in the same ruleset, on Normal and again on PvP. Decision: whether the maintainer and a guild member can keep alts across factions without a second ruleset.

## T7 — Rapid Regeneration
Troll. Usable in combat? Does casting a heal, dropping a totem, moving, or taking damage cancel it? Tooltip says any movement, action or damage cancels [T2 wago 2026-09-18 b:1.60.1.69913]; if "taking damage" is literal it is an out-of-combat or kiting tool, not a raid cooldown.

## T8 — Live tooltip vs datamine
`/wfa tip` stores the live text. Any difference from `python scripts/wago_query.py spell "<name>"` is either a bug in our tooltip resolver or a server-side hotfix the client tables do not show. Both are worth knowing; the second is the only way we would ever see a hotfix before Blizzard posts it.

## What to actually do on a new character
1. Character creation: T6.
2. Level to your first heal. Type `/wfa go`, press Blood Fury (Orc) or Berserking (Troll) when told, hit one mob, `/reload`.
3. Tell the agent "addon data is ready". It runs `python scripts/read_addon_data.py --verdict`.
4. Expect T1 to say INCONCLUSIVE. Everything else above will have an answer.
