# WoW Forever — Combat and resource mechanics (cross-class)

Data as of: 2026-11-07 b:1.60.1.70790
Provenance: [T1 blizz-forum 2026-10-02] and the tags on each line. This file holds rules that are not talents and not racials: resource generation, weapon skill, hit and crit, threat. Server-side formulas cannot be datamined, so player measurements are allowed here at tier 5 **only** when the line says Blizzard has not confirmed them; a tier 1–2 source replaces them. Added after wargame drill 02 (`docs/wargame/drill-02-questions.md`, root cause R2): the Warrior Rage change had no file to live in.
Source: Blizzard staff posts in `data/forum/staff-posts.json`; the launch-client tables for anything the tables can show; player forum threads for measured formulas (tier 5, leads only).

## Hit and crit
- Hit and crit are unified across spell, melee and ranged in Forever [T1 blizz-deepdive 2026-09-12] (`racials.md`). One hit stat, one crit stat; a melee racial crit bonus applies to spells and vice versa.
- Classic baseline, not confirmed for Forever: 8% melee miss against a level-63 boss (9% dual-wield extra), 16% spell miss cap; treat these as assumptions and say so.

## Weapon skill
- The weapon-skill racials (Orc axes, Human swords and maces, Dwarf guns, Troll bows) are gone; their replacements give crit or hit without a weapon condition [T1 blizz-deepdive 2026-09-12; T2 wago 2026-11-04 b:1.60.1.70790] (`racials.md`).
- **Unconfirmed:** whether weapon skill itself still exists, levels with use, and affects miss and glancing-blow chance as in Classic. No staff post addresses it and the tables cannot show it. Members report a freshly trained weapon missing more; that is consistent with Classic behaviour but is not a measurement. Check in game: Skills tab, weapon line, "x / 5×level".
- Shaman weapon skills in the launch client: one-hand and two-hand axes, one-hand and two-hand maces, daggers, fist weapons, staves, shields; no swords or polearms [T2 wago 2026-11-06 b:1.60.1.70790]. Dual Wield: spell 674 has a SkillLineAbility row on the Shaman skill line, but no talent, trigger or level grant was found in b:1.60.1.70790 or b:1.60.1.70862 and no trainer has been seen offering it; the new passive 1300344 is granted to no class. Treat Shaman dual wield as unavailable until someone sees it on a trainer in game (unconfirmed) [T2 wago 2026-11-04 b:1.60.1.70790; T2 wago 2026-11-07 b:1.60.1.70862]. Weapon masters: Orgrimmar (Hanashi, Sayoc) two-handed axes; Thunder Bluff (Ansekhwa) two-handed maces; Undercity (Archibald) two-handed swords and polearms, 1 gold at level 20 [T2 in-game 2026-09-23 b:1.60.1.69913] (`systems-legacy-servers-dates.md`, `gear/paladin-ret-20.md`).

## Rage (Warrior and Druid)
- Critical strikes generate 100% additional Rage (was 75%) [T1 blizz-forum 2026-10-02] (Kaivax, "Warrior updates in today's Beta build"). Druid: Rage from crits 100% (was 75%) [T1 blizz-forum 2026-10-08] (`talents-druid.md`).
- Unbridled Wrath no longer grants twice as much Rage to two-handed weapons [T1 blizz-forum 2026-10-02].
- Rage from damage taken: three bugs fixed in the 8 Oct build (health-based calculation that penalised Stamina, crit and crushing multipliers, absorbs). Blizzard now balances Rage from damage taken around 20–40% armour by level, not the 50% a tank has, so questing Warriors and Druids gain more [T1 blizz-forum 2026-10-08].
- **Unconfirmed, player-measured:** Rage from dealing damage is normalized to weapon speed, not damage dealt: about 3.46 Rage per second with any one-hand weapon and 4.5 with any two-hand weapon, i.e. 7–9 Rage per one-hand swing and 14–17 per two-hand swing; weapon damage, Attack Power and Strength do not change Rage income [T5 forum-player 2026-09-20] (https://us.forums.blizzard.com/en/wow/t/warrior-rage-normalization-auto-attack-crits-dont-generate-extra-rage/2355684). The same thread's claim that crits give no extra Rage is superseded by the 2 Oct staff post above. No staff post states the formula.
- Consequence for gear advice, if the report holds: a higher-damage weapon gives more threat and damage, not more Rage; crit chance and getting hit are what raise Rage income.

## Threat
- Bear and Dire Bear Form threat bonus 50% (was 30%) [T1 blizz-forum 2026-10-08] (`talents-druid.md`).
- Warrior Defensive Stance threat bonus 80% (was 30%; Classic 30%) [T1 blizz-forum 2026-11-03]; in the client tables from b:1.60.1.70862 [T2 wago 2026-11-07 b:1.60.1.70862]. Defiance 7/13/20%. Blood Craze and Gore Drinker self-heals generate no threat [T1 blizz-forum 2026-11-03] (`talents-warrior.md`).
- Sunder Armor threat values corrected on all ranks, with a small increase to threat from Attack Power [T1 blizz-forum 2026-09-24] (`talents-warrior.md`).
- Shaman Spirit Weapons: −30% threat without Rockbiter, +30% with it [T2 wago 2026-11-04 b:1.60.1.70790] (`talents-shaman.md`).
- Classic baseline for everything else (healing threat split across enemies, threat wipes, tank modifiers): not confirmed for Forever.

## Pets
- Announced 6 Nov 2026 for a 10 Nov hotfix: Hunter pets and Warlock Voidwalkers tank worse than intended; Blizzard will raise their stats to match Classic Era effectiveness [T1 blizz-forum 2026-11-06] (Kaivax, "Class Tuning Incoming - November 10"). Voidwalker base health +about 40 at all levels in the 6 Nov hotfixes [T1 blizz-forum 2026-11-06].
