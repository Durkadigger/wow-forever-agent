# WoW Forever Knowledge Base — Plague guild
Data as of: 2026-11-07 b:1.60.1.70862 (newest client, product `wowf`, datamined) for talents, racials, Legacy and Camping. Dates, rulesets and world content: refreshed 2026-11-07 from Blizzard posts (6 Nov hotfixes, 10 Nov tuning notice). Editions, Camping, combat rules: 2026-09-15 b:blizzcon-demo. The beta closed 23 Oct 2026; launch is 4 Nov 2026.
Provenance tags: `[T<tier> <source-id> <date> b:<build>]`, see docs/sop-provenance.md and sources.md. Build labels in data/builds.json.

Built 15 Sept 2026 from classicwowforever.com (talent calculator data chunk, racials, Legacy, Deep Dive recap), Warcraft Tavern hands-on racials, and Blizzard's official recaps. Everything is **pre-release demo data**; beta opens 17 Sept 2026 and values will shift. Treat "captured" as "seen in a BlizzCon demo tooltip," not "final."

## Files
| File | Contents |
|---|---|
| `racials.md` | All 10 race/faction options, racial tooltips, race/class matrix, Priest racial spells, the maintainer's race rankings for Resto Shaman |
| `talents-shaman.md` | Full Elemental / Enhancement / Restoration trees + Resto planning notes. **Every talent file now opens with a datamined Overrides block (all ranks, tier 2); read that first, the generated tier 3 lines below it are superseded.** |
| `talents-mage.md` | Arcane / Fire / Frost |
| `talents-rogue.md` | Assassination / Combat / Subtlety |
| `talents-warlock.md` | Affliction / Demonology / Destruction |
| `talents-warrior.md` | Arms / Fury / Protection |
| `talents-hunter.md` | Beast Mastery / Marksmanship / Survival |
| `talents-priest.md` | Discipline / Holy / Shadow Magic |
| `talents-paladin.md` | Holy / Protection / Retribution |
| `talents-druid.md` | Balance / Feral Combat / Restoration |
| `mechanics.md` | Cross-class combat rules: hit/crit unification, weapon skill, Rage, threat, pets. Player-measured formulas allowed at T5 with the unconfirmed flag |
| `systems-legacy-servers-dates.md` | Dates, editions, realmless rulesets, Legacy tree, Camping, combat rules, new zones/dungeons, quest log and vendor rules |
| `gear/paladin-ret-20.md` | Retribution gear at the beta cap: weapon rule, two-hand targets, Blacksmithing. First file under `gear/` |
| `quests/wolfsbane-paladin.md` | The Wolfsbane weapon chain: confirmed steps, unverified tail, and the Classic quests ruled out of it. First file under `quests/` |

## Guild context
*Provenance: guild choice, not game data. The Normal ruleset itself: [T1 blizz-news 2026-10-22] (article 24302070).*
- Plague: Horde, Normal (PvE) ruleset. Each member's own class, spec and characters live in their git-ignored `CLAUDE.local.md`, not here.

## Open questions to resolve after 17 Sept Q&A / beta datamine
Only a T1 or T2 source resolves a question (docs/sop-provenance.md §3). T3–T5 evidence is noted beneath the question but leaves it open.
1. Does Orc Blood Fury's Spell Power affect healing?
   - Evidence, not a resolution [T2 wago 2026-09-17 b:1.60.1.69893]: Blood Fury carries a single percent-Spell-Power aura (317) and no healing-done aura, while other spell power buffs in the client pair a damage aura with a healing aura. The tables cannot show how the server applies 317 to heals. Needs an in-game test (see `knowledge/racials.md`, Orc).
   - 18 Sept 2026: unchanged in b:1.60.1.69913 (same three auras 166/167/317). Nothing from Blizzard on it in the known-issues list or the Q&A recap. [T2 wago 2026-09-18 b:1.60.1.69913]
   - 27 Oct 2026: still unchanged in b:1.60.1.70634 (same three auras 166/167/317); the cooldown is now 3 min (2 min announced for launch) and no post addresses healing. The beta is closed, so an in-game test has to wait for launch. [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-27]
   - 4 Nov 2026 (launch day): still unchanged in b:1.60.1.70790 (same three auras 166/167/317, no healing-done aura); the cooldown is now 2 min as announced, and the 2 Nov development notes say nothing about healing. Can only be settled by an in-game test on the live game. [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03]
   - 25 Sept 2026: still unchanged in b:1.60.1.70009 (same three auras 166/167/317). The 24 Sept blue post (WoW Forever Beta Development Notes) touched many spells but named no Shaman racial. [T2 wago 2026-09-25 b:1.60.1.70009; T1 blizz-forum 2026-09-24]
3. Can one account have Horde and Alliance in the same ruleset (esp. PvP)?
   - Partly answered by Blizzard: on the PvP ruleset each account can create characters for only one faction. Normal and Roleplaying are not stated, so the question stays open for them. [T1 blizz-news 2026-10-22] (article 24302070)
6. Skyborne druid form names; whether Skyborne unlocks without purchase later.
8. Seal of Command's proc rate in Forever. Classic was about 7 per minute. Decides how much weapon speed is worth to a Retribution Paladin (`knowledge/gear/paladin-ret-20.md`).
9. Forsaken Greataxe and Corpse Chopper tooltips, and Wolfsbane's real secondary stats. No Forever item data is datamined into this repo, and 7 Nov 2026 showed why: wago's `ItemSparse` for `wowf` holds 19,307 rows and none of the levelling items checked (Classic-line clients keep item data server-side) [T2 wago 2026-11-07 b:1.60.1.70862]. Every item value we hold is tier 2 in-game (a member's tooltip screenshot) or tier 5. A member's screenshot of a tooltip is the way to close this per item.
10. The Wolfsbane steps after the Lumina escort. One tier-5 gold-seller source only (`knowledge/quests/wolfsbane-paladin.md`).

## Resolved
- (was #4) Beta end date: the beta closed Fri 23 Oct 2026 at 10:00 a.m. PDT, not 21 or 22 Oct. A stress test ran on 21 Oct and the beta reopened until 23 Oct. [T1 blizz-forum 2026-10-22; T1 blizz-forum 2026-10-23]
- (was #7) Level cap 20 → 30: raised in the beta build of 1–2 Oct 2026. [T1 blizz-forum 2026-10-01] The cap was 20 for the first two weeks of the beta.
- (was #2) Racial cooldown lengths: all known. Blood Fury 2 min, Shatter Curse 3 min, Berserking 3 min, Rapid Regeneration 3 min, War Stomp 2 min, Will of the Forsaken 2 min, Cannibalize 2 min; full list in `racials.md`. [T2 wago 2026-09-17 b:1.60.1.69893] Changed since: Blood Fury 3 min on 16 Oct and back to 2 min in the launch client [T2 wago 2026-11-04 b:1.60.1.70790], War Stomp 90 sec, Walk on Air 90 sec, Cultivation 15 min; see `racials.md`. [T2 wago 2026-10-27 b:1.60.1.70634]
- (was #5) Elemental Mastery (4 Nov: now renamed Lightning Mastery, and Lava Burst is removed from the tree [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03]): was removed in the first beta client [T2 wago 2026-09-17 b:1.60.1.69893]; it **returned on 16 Oct** as the 31-point Elemental capstone (3 min CD, -0.5 sec Lightning Bolt and Lava Burst cast, Chain Lightning no cooldown, 15 sec), and Lava Burst moved to row 5 [T1 blizz-forum 2026-10-16; T2 wago 2026-10-27 b:1.60.1.70634].
- (was #7) Higher-rank values: every rank of every talent and Legacy perk is now read from the client's per-rank curves. See the Overrides block in each `talents-<class>.md` and the Legacy section of `systems-legacy-servers-dates.md`. [T2 wago 2026-09-17 b:1.60.1.69893]

## Suggested project instructions
"Use these files as the baseline for WoW Forever questions. Prefer Blizzard official recaps > classicwowforever.com captured tooltips > creator videos > secondhand articles. Flag any value that predates the current beta build. Frame racial and talent advice for the member's class and spec (CLAUDE.local.md); Horde, Normal ruleset. Always link products when recommending them."

## Refresh plan
Beta-day steps and deferred wargames: `docs/beta-day-checklist.md` (run from 17 Sept 2026).
Procedure: `.claude/skills/forever-refresh/SKILL.md`. Provenance and precedence: `docs/sop-provenance.md`. Sources and ids: `sources.md`. Builds: `data/builds.json`.

Re-scrape the talent chunk after: (a) 17 Sept Q&A, (b) first beta datamine (Wowhead/Warcraft Tavern), (c) launch build. The chunk URL pattern is `classicwowforever.com/_next/static/chunks/forever-talents-*.js`; the hash changes each deploy. Claude Sonnet 5 in Claude Code is the cost-effective model for the re-scrape; use Fable 5.1 for the analysis pass.
