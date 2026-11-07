# In-game test plan — WoW Forever beta

Written 17 Sept 2026 for build 1.60.1.69893. Ordered by how much each answer changes a decision for a Horde Resto Shaman. Tick as you go and tell the agent what you saw; results go into `knowledge/` with an in-game tag once the tier question at the bottom is settled.

**Predictions and verdict rules for each test are in `docs/ingame-theory.md`, written before any data. `/wfa go` runs Session 0 and test 1.1 in one command.**

**Method key.** `addon` = WFATest snapshot, then `/reload`. `log` = Advanced Combat Logging on, `/combatlog`, cast, then the agent reads `Logs/WoWCombatLog.txt`. `eyes` = look and report. Do stat reads out of combat.

**Rules for a clean heal test.** Same spell and rank, same target, exclude crits, at least 20 casts per arm, change one thing between arms, note talents and gear. Where a direct stat read answers the question, prefer it: no statistics needed.

## Session 0 — does anything work (5 minutes)
- [ ] 0.1 `/wfa status`. Record the interface number. Do addons load at all? (`addon`)
- [ ] 0.2 `/wfa snap baseline`, then attack a mob and `/wfa snap incombat`. Are stats hidden in open-world combat? (`addon`)
- [ ] 0.3 Enter any dungeon, out of combat: `/wfa snap dungeon-ooc`. Does the map alone hide stats? (`addon`)
- [ ] 0.4 `/combatlog` then a few casts, then check the file exists and whether lines carry spell power. (`log`)
- [ ] 0.5 Can one account make Horde and Alliance characters in the same ruleset? Try it at character creation. Resolves open question #3. (`eyes`)

## Session 1 — the race decision
- [ ] 1.1 **Blood Fury and healing.** Orc. `/wfa watch 25 bloodfury`, press Blood Fury at 3 sec. Healing bonus moves about 10% or it does not. Resolves open question #1. (`addon`)
- [ ] 1.2 **Are healing and spell damage separate stats?** Equip one item with +healing only, or compare the two numbers on the character sheet. Foundation for every gear weight. (`addon` snap with and without the item)
- [ ] 1.3 **Berserking.** Troll. Healing Wave tooltip cast time with and without it. Is 10% haste a 10% shorter cast or 9.1%? (`eyes`, or `addon` spell haste read)
- [ ] 1.4 **Axe Specialization and spell crit.** Orc. Snap with an axe equipped, snap without. Does spell crit move 1%? It feeds Water Shield. (`addon`)
- [ ] 1.5 **Unified crit.** Put a point in Thundering Strikes; do melee crit and spell crit both rise 1%? (`addon`)
- [ ] 1.6 **Rapid Regeneration.** Troll. Usable in combat? What cancels it: a heal cast, a totem drop, taking damage? (`eyes`)

## Session 2 — Resto mechanics that set the build
- [ ] 2.1 **Tooltip versus datamine.** `/wfa talents` and `/wfa tip 408521`, `/wfa tip 408510`, `/wfa tip 16190`. The agent compares live text with the datamined per-rank values and the level-scaling formula. Any mismatch is a bug in our resolver or a server-side hotfix. (`addon`)
- [ ] 2.2 **Downranking.** Rank 1 Healing Wave versus max rank with the same +healing. Is there a penalty on low ranks? Decides the whole mana-efficiency approach. (`log`)
- [ ] 2.3 **Riptide coefficients.** Datamined: 0.214 direct, 0.10 per tick. Cast at two different +healing values; the slope is the coefficient. (`log`)
- [ ] 2.4 **Riptide and Chain Heal.** Does Chain Heal consume the Riptide heal-over-time for its +25%, or leave it running? (`eyes` + `log`)
- [ ] 2.5 **Water Shield.** Mana per globe (datamined 2% of max), and the hidden gap between procs: "every few seconds" in the tooltip. Count the seconds between mana gains. Does a heal crit on someone else trigger it? (`log`)
- [ ] 2.6 **Mindfulness.** Mana regen while casting, before and after each rank: expect 17/33/50% of the not-casting number. (`addon` mana regen read)
- [ ] 2.7 **Purification scope.** Does it raise Healing Stream Totem ticks and Riptide ticks, or only direct heals? (`log`)
- [ ] 2.8 **Healing Way.** Datamined as a flat 8/17/25% to Healing Wave, not Classic's stacking buff on the target. Confirm no buff appears on the target. (`eyes`)
- [ ] 2.9 **Crit heal size.** 150% or something else? (`log`)
- [ ] 2.10 **Nature's Swiftness.** Works with Chain Heal? Shares a cooldown with anything? (`eyes`)
- [ ] 2.11 **Mana Tide at your level.** Datamined numbers look like a low-level base (88 mana per 3 sec for 12 sec). What does the live tooltip say? (`addon` tip 16190)
- [ ] 2.12 **Tidal Focus hit.** Does spell hit modifier rise 1% per point? (`addon`)

## Session 3 — systems
- [ ] 3.1 **Legacy.** Where does the first Legacy point come from, and how fast do they arrive? Cap is 16 in the data. Note every source you see. (`eyes`, `/wfa talents`)
- [ ] 3.2 **Talented perk.** With rank 1, does a level 9 character get a talent point? (`eyes`)
- [ ] 3.3 **Reagent Economy.** With the perk, does Reincarnation still need an Ankh? (`eyes`)
- [ ] 3.4 **Camping.** Buff size, duration, the one-hour cooldown, whether camp buffs stack with class buffs (reported: First Aid Kit stamina does not stack with Fortitude), what a Shaman contributes. (`addon` snap before and after resting)
- [ ] 3.5 **Permanence.** Does it lengthen totems? Probably not, since totems are not long-duration buffs. Worth one look. (`eyes`)
- [ ] 3.6 **Beta level cap and any boost or template characters.** Decides which of the tests above are even possible. (`eyes`)
- [ ] 3.7 **Skyborne druid form names.** Open question #6. (`eyes`)

## Session 4 — gold and professions
- [ ] 4.1 **Cultivation.** Cooldown, which herbs qualify, whether the duplicate is visible to other players. Decides whether it depresses herb prices. (`eyes`)
- [ ] 4.2 **Bountiful Harvest.** Which materials count as "Scarce"? (`eyes`)
- [ ] 4.3 **Merchant's Favor.** What the supply crates ask for and what the currency buys. Nobody has published this. (`eyes`, screenshots)
- [ ] 4.4 **Alchemy Lab.** Does flask crafting need the camp object? Any other recipe gated by a camp object? (`eyes`)
- [ ] 4.5 **Profession trainer.** New recipes at the trainer for Alchemy, Herbalism, Cooking: names and skill levels. (`eyes`, screenshots)

## Decision for the maintainer before results are filed
In-game observation is not in the tier list in `sources.md`. Proposal: add source-id `in-game` at **tier 2**, the same as a datamine, because it is the live client. It would outrank fan sites and creators, and lose to a Blizzard statement about the same build. A measured result would carry the method in the note, for example `[T2 in-game 2026-09-18 b:1.60.1.69893] (addon stat read, n=1)` or `(combat log, n=24 per arm)`.
