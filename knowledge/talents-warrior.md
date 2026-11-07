# WoW Forever — Warrior Talents
Data as of: 2026-11-07 b:1.60.1.70862 (Overrides block: datamined, tier 2). Generated lines below the block: 2026-10-27 b:beta, tier 3, superseded wherever the block covers the same talent.
Source: classicwowforever.com talent calculator chunk. Rank-1 captured tooltips; higher ranks are the site's estimates. Values change with each build.
Provenance: [T3 cwf 2026-10-27 b:beta] applies to every talent line below unless an Overrides entry says otherwise. The tag date is the date this script fetched the site; the site's own capture may be earlier. Provenance tags: `[T<tier> <source-id> <date> b:<build>]`, see docs/sop-provenance.md and sources.md. Build labels in data/builds.json.

<!-- overrides -->
## Overrides (tier 1–2 values that outrank the generated lines)
*Full datamined tree, TraitTree 1117. [T2 wago 2026-11-07 b:1.60.1.70862] applies to every line in this block. Values written a/b/c are ranks 1/2/3, each read from the client's per-rank curves (TraitDefinitionEffectPoints), not extrapolated.*

### 24 Sept 2026 blue-post class changes (not talent-rank values)
*[T1 blizz-forum 2026-09-24] (Kaivax, WoW Forever Beta Development Notes – Updated September 24, https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-updated-september-24/2360696)*
- Sunder Armor: corrected threat values on all ranks, including a small increase to threat generated from Attack Power (bug fix).
- Slam's base cooldown increased to 18 sec (was 15 sec) — reverted to 15 sec on 2 Nov [T1 blizz-forum 2026-11-03], 15 sec in b:1.60.1.70862 [T2 wago 2026-11-07 b:1.60.1.70862]; Arms talent Improved Slam now also reduces Slam's cooldown by 1.5/3.0 sec (tree below already updated) and Bloodthrill activation chance/behavior changed (tree below already updated).

### 1–27 Oct 2026 blue-post class changes, checked against b:1.60.1.70634 (not talent-rank values; layered on the tree below)
*[T1 blizz-forum 2026-10-16] unless a line carries its own tag. Source: Kaivax, WoW Forever Beta Development Notes (topic 2360696): posts of 1 Oct [T1 blizz-forum 2026-10-01], 8 Oct [T1 blizz-forum 2026-10-08] and 16 Oct. Where the 27 Oct datamine shows the same change the line also carries [T2 wago 2026-10-27 b:1.60.1.70634]. These notes supersede the 24 Sept block above wherever they overlap. Class deep-dive articles of 30 Sept to 15 Oct (blizz-news 24301515, 24301514, 24302097, 24310968, 24302099) describe the same beta changes and were not stored line by line.*
- **Fury rework (1–2 Oct build):** Lingering Rage, Furious Precision and Gore Drinker added; Improved Cleave and Boundless Rage removed; Flurry now requires Death Wish; Raging Blows lowers Cleave and Whirlwind Rage cost by 3; Bloodthirst 45% of Attack Power (was 35%) [T1 blizz-forum 2026-10-01; T2 wago 2026-10-27 b:1.60.1.70634].
- **Protection:** Toughness removed; Iron Will, Anticipation, Improved Bloodrage, Improved Revenge, Improved Disarm and Improved Shield Bash moved up a row each; Bastion and Focused Rage reordered [T1 blizz-forum 2026-10-01; T2 wago 2026-10-27 b:1.60.1.70634]. Battle Shout is raid-wide; Slam is no longer subject to spell pushback [T1 blizz-forum 2026-10-16]. Rage gained from damage taken was recalculated (typically more Rage) [T1 blizz-forum 2026-10-08].
- **Rage from dealing damage (all specs).** Critical strikes generate 100% additional Rage (was 75%); Unbridled Wrath no longer grants twice as much Rage to two-handed weapons [T1 blizz-forum 2026-10-02] (Kaivax, "Warrior updates in today's Beta build", https://us.forums.blizzard.com/en/wow/t/warrior-updates-in-todays-beta-build/2369360/1).
- **Rage normalization (player report).** Rage per swing is reported to be normalized to weapon speed instead of damage dealt, about 3.46 Rage per second with any one-hander and 4.5 with any two-hander, so weapon damage, Attack Power and Strength do not raise Rage income [T5 forum-player 2026-09-20] (player testing, https://us.forums.blizzard.com/en/wow/t/warrior-rage-normalization-auto-attack-crits-dont-generate-extra-rage/2355684). Unconfirmed: no staff post states the formula or numbers; the crit-Rage line above implies a fixed base per hit. Rage formulas are server-side and cannot be datamined.

### 2 Nov 2026 development notes, Warrior section (summarised 7 Nov; the datamined tree below already carries the talent changes)
*[T1 blizz-forum 2026-11-03] (Kaivax, WoW Forever Beta Development Notes, updated 2 Nov (topic 2360696, post 9, https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9)). Found uncited by `scripts/coverage_check.py`; the stored copy of the post had been cut at 4,000 characters until 7 Nov.*
- Defensive Stance threat bonus 30% → 80%. Defiance 7/13/20% (was 5/10/15%). Slam cooldown 15 sec (was 18; this reverses the 24 Sept change above). Victory Rush tooltip damage corrected.
- Arms: Improved Tactical Mastery 3 points, 5/10/15 Rage (was 5 points, 3–15); Two-Handed Weapon Specialization 2/4/6% (was 1/2/3%); Bloodthrill 2 points, 10/20% (was 5 points, 4–20%); Improved Slam cooldown cut 2.5/5 sec (was 3/3).
- Fury: Blood Craze and Gore Drinker self-heals no longer generate threat; Blood Craze does not trigger while sitting; Booming Voice also cuts Piercing Howl's Rage cost 5–25%; Enrage to row 3; new Reckless Swings (row 4, 1 point, 15 sec CD, costs 25% of base health, next 4 melee attacks generate 5 extra Rage, 8 sec); Gore Drinker to row 5, linked to Blood Craze; Death Wish no longer required for Flurry, but required for Bloodthirst; Flurry 3 points, 10/20/30%; new Improved Whirlwind (row 6, 2 points, −1/2 sec cooldown, +15/30% damage to the closest enemy).
- PvP: dropping the flag in Darkspear Islands no longer applies the Recently Dropped Flag debuff.

### 6–7 Nov 2026 hotfixes and client build 1.60.1.70862
*[T1 blizz-forum 2026-11-06] (Kaivax, "WoW: Forever Hotfixes - November 6, 2026", https://us.forums.blizzard.com/en/wow/t/wow-forever-hotfixes-november-6-2026/2403040/4) unless a line carries its own tag; client build 1.60.1.70862 (7 Nov) carries the matching tooltip changes [T2 wago 2026-11-07 b:1.60.1.70862]. Builds 70840 and 70862 are the first post-launch client builds; 70840 was not snapshotted. No talent rank changed between 70790 and 70862.*
- **Defensive Stance threat bonus is 80%** (was 30%; Classic baseline 30%). Announced in the 2 Nov notes [T1 blizz-forum 2026-11-03]; the launch client's tables still said 30 and the 70862 client now says 80 (effect base points on the stance passive, spell 7376; with Defiance 3/3 the tooltip computes 107%) [T2 wago 2026-11-07 b:1.60.1.70862].
- Reckless Swings tooltip now mentions that it activates Gore Drinker (tooltip only).
- Rage: see `knowledge/mechanics.md` for the 2 Oct crit-Rage change and the player-reported normalization.

### Arms — datamined (17 talents, 42 points)

**R1**
- Improved Heroic Strike [3] — Reduces the cost of your Heroic Strike ability by 1/2/3 Rage. `id 12282`
- Deflection [5] — Increases your Parry chance by 1/2/3/4/5%. `id 16462`
- Improved Rend [3] — Increases the Bleed damage done by your Rend ability by 12/23/35%. `id 12286`

**R2**
- Improved Charge [2] — Increases the Rage generated by your Charge ability by 3/6. `id 12285`
- Improved Tactical Mastery [3] — Tactical Mastery lets you retain up to an additional 5/10/15 Rage when you change stances. `id 12295`
- Improved Overpower [2] — Increases the critical strike chance of your Overpower ability by 25/50%. `id 12290`

**R3**
- Anger Management [1] — Generates 1 Rage every 3 sec while in combat, and reduces Rage loss while out of combat by 30%. *(requires Improved Tactical Mastery)* `id 12296`
- Deep Wounds [3] — Your critical strikes cause your opponent to Bleed, dealing 20/40/60% of your melee weapon's average damage over 12 sec. *(requires Improved Rend)* `id 12834`

**R4**
- Spearing Strike [1] — 15 rage, 5 yd, 20 sec CD. A brutal attack that deals 75% weapon damage. Deals an additional 75% weapon damage against Giants, Dragonkin, and mounted targets. Mounted targets are dismounted. `id 1310222`
- Two-Handed Weapon Specialization [3] — Increases the damage you deal with two-handed melee weapons by 2/4/6%. `id 12163`
- Impale [2] — Increases the critical strike damage bonus of your abilities by 10/20%. *(requires Deep Wounds)* `id 16493`

**R5**
- Bloodthrill [2] — Grants your Main Hand melee attacks against enemies afflicted by your Rend a 10/20% chance to allow an activation of Overpower. `id 1289682`
- Sweeping Strikes [1] — 30 rage, 30 sec CD. Your next 5 melee attacks strike an additional nearby opponent. `id 12292`
- Weaponmaster [5] — Gives your melee weapon attacks a benefit depending on the weapon. |CFFFFFFFFAxe/Polearm:|R Increases your critical strike chance by 1/2/3/4/5%. |CFFFFFFFFMace/Staff:|R Your attacks ignore 3/6/9/12/15% of your target's armor. |CFFFFFFFFSword:|R Your successful melee attacks have a 1/2/3/4/5% chance to trigger an extra attack on the target. `id 1290261`

**R6**
- Improved Slam [2] — Reduces the cooldown of your Slam ability by 2.5/5.0 sec, the cast time and global cooldown by 0.25/0.50 sec, and Slam no longer interrupts or delays your melee swing. `id 12862`
- Improved Hamstring [3] — Gives your Hamstring ability a 5/10/15% chance to immobilize the target for 5 sec. `id 12289`

**R7**
- Mortal Strike [1] — 30 rage, 5 yd, 6 sec CD. A vicious strike that deals weapon damage plus 85 and wounds the target, reducing the effectiveness of any healing by 50% for 10 sec. *(requires Sweeping Strikes)* `id 12294`

### Fury — datamined (18 talents, 53 points)

**R1**
- Booming Voice [5] — Increases the area of effect of your Shouts by 10/20/30/40/50% and reduces the Rage cost by of your Shouts and Howls by 5/10/15/20/25%. `id 12321`
- Cruelty [5] — Improves your chance to get a critical strike with melee attacks by 1/2/3/4/5%. `id 12320`

**R2**
- Lingering Rage [5] — Increases the time before your Rage begins to decay after leaving combat by 2/4/6/8/10 sec. `id 1323964`
- Unbridled Wrath [5] — Gives you a 12/24/36/48/60% chance to generate 1 additional Rage when you deal melee damage with a weapon. `id 12322`

**R3**
- Furious Precision [3] — Increases your chance to hit with off-hand attacks by 4/7/10%. `id 1323963`
- Piercing Howl [1] — 10 rage. Causes all enemies within $a2 yds to be Dazed, reducing movement speed by 50% for 6 sec. `id 12323`
- Blood Craze [3] — Regenerates 1/2/3% of your total Health over 6 sec after being the victim of a critical strike or suffering more than 20% of your maximum Health from a single attack. `id 16487`
- Enrage [5] — Gives you a 30% chance to deal 2/4/6/8/10% increased Physical damage for 12 sec after being the victim of any damaging attack. `id 12317`

**R4**
- Dual Wield Specialization [5] — Increases the damage done by your off-hand weapon by 5/10/15/20/25% and the Rage generated by your off-hand attacks by 10/20/30/40/50%. `id 23584`
- Reckless Swings [1] — 25% of base power, 15 sec CD. Your next 4 melee attacks generate 5 additional Rage. Lasts 8 sec. `id 1329555`
- Improved Execute [2] — Reduces the Rage cost of your Execute ability by 3/5. `id 20502`

**R5**
- Improved Berserker Rage [2] — Your Berserker Rage ability will instantly generate 5/10 Rage and has a 50/100% chance to remove all movement impairing effects when activated. `id 20500`
- Death Wish [1] — 10 rage, 3 min CD. When activated, increases your Physical damage done by 20% and makes you immune to Fear effects, but increases all damage you take by 5%. Lasts 30 sec. `id 12328`
- Gore Drinker [2] — Your Enrage, Berserker Rage, Bloodrage, Death Wish, Reckless Swings, and Bloodthirst abilities cause your next 3 melee attacks to restore 0.5/1.0% of your maximum Health. *(requires Blood Craze)* `id 1323967`
- Improved Intercept [2] — Reduces the cooldown of your Intercept ability by 5/10 sec. `id 20504`

**R6**
- Improved Whirlwind [2] — Reduces the cooldown of your Whirlwind ability by 1/2 sec and increases the damage it deals to the closest enemy by 15/30%. `id 1310315`
- Flurry [3] — Increases your melee attack speed by 10/20/30% for your next 3 swings after dealing a melee critical strike. `id 12319`

**R7**
- Bloodthirst [1] — 30 rage, 5 yd, 6 sec CD. Instantly attack the target causing damage equal to 45% of your Attack Power plus 30 and increasing your movement speed by 10% for 10 sec. *(requires Death Wish)* `id 23881`

### Protection — datamined (18 talents, 50 points)

**R1**
- Improved Bloodrage [2] — Increases all the Rage generated by your Bloodrage ability by 25/50%. `id 12301`
- Shield Specialization [5] — Increases your chance to Block attacks with your shield by 1/2/3/4/5% and grants you a 20/40/60/80/100% chance to generate 5 Rage when you Block. `id 12298`
- Iron Will [5] — Reduces the duration of Stun and Fear effects inflicted on you by 3/6/9/12/15%. `id 12962`

**R2**
- Anticipation [5] — Increases your Defense Skill by 4/8/12/16/20. `id 12297`
- Improved Revenge [3] — Increases damage dealt by your Revenge ability by 20/40/60%. `id 12797`
- Improved Thunder Clap [3] — Reduces the Rage cost of your Thunder Clap ability by 2/4/6. `id 12287`

**R3**
- Last Stand [1] — 3 min CD. When activated, this ability temporarily grants you 30% of your maximum health for 20 sec. After the effect expires, the health is lost. `id 12975`
- Master of Defense [2] — Grants you a 50/100% chance to generate 5 Rage when you Dodge or Parry while a shield is equipped. *(requires Shield Specialization)* `id 1310316`
- Improved Disarm [3] — Reduces the cooldown of your Disarm ability by 7/13/20 secs. `id 12313`
- Defiance [3] — Increases all threat generated in Defensive stance by an additional 7/13/20% while a shield is equipped. `id 12792`

**R4**
- Improved Sunder Armor [3] — Reduces the Rage cost of your Sunder Armor ability by 1/2/3. `id 12308`
- Vanguard [1] — Your Charge ability is now usable while in Defensive Stance. `id 1310317`
- Improved Shield Bash [2] — Gives your Shield Bash ability a 50/100% chance to Silence the target for 3 sec. `id 12311`

**R5**
- Improved Shield Wall [2] — Reduces the cooldown of your Shield Wall ability by 5.5/11.0 min. `id 12312`
- Concussion Blow [1] — 10 rage, 5 yd, 45 sec CD. Stuns the target for 5 sec. `id 12809`
- Focused Rage [3] — Reduces the Rage cost of your offensive abilities by 1/2/3. `id 29787`

**R6**
- Bastion [5] — Increases all damage you deal by 2/4/6/8/10% while a shield is equipped. `id 16538`

**R7**
- Shield Slam [1] — 20 rage, 5 yd, 6 sec CD. Slam the target with your shield, causing 421–439 damage, increased by your Block Value, and has a 50% chance of dispelling 1 magic effect on the target. Causes a very high amount of threat. *(requires Concussion Blow)* `id 23922`

<!-- /overrides -->

## Arms (17 talents)

**R1**
- Improved Heroic Strike [3] — Reduces the cost of your Heroic Strike ability by 1 Rage.
- Deflection [5] — Increases your Parry chance by 1%.
- Improved Rend [3] — Increases the Bleed damage done by your Rend ability by 12%.

**R2**
- Improved Charge [2] — Increases the Rage generated by your Charge ability by 3.
- Improved Tactical Mastery [5] — Tactical Mastery lets you retain up to an additional 3 Rage when you change stances.
- Improved Overpower [2] — Increases the critical strike chance of your Overpower ability by 25%.

**R3**
- Anger Management [1] — Generates 1 Rage every 3 sec while in combat, and reduces Rage loss while out of combat by 30%.
- Deep Wounds [3] — Your critical strikes cause your opponent to Bleed, dealing 20% of your melee weapon's average damage over 12 sec.

**R4**
- Spearing Strike [1] — 15 Rage | Melee Range | Instant | 20 sec cooldown | Requires Battle Stance | A brutal attack that deals 40% weapon damage. Deals an additional 80% weapon damage against Giants, Dragonkin, and mounted targets. Mounted targets are dismounted.
- Two-Handed Weapon Specialization [3] — Increases the damage you deal with two-handed melee weapons by 1%.
- Impale [2] — Increases the critical strike damage bonus of your abilities by 10%.

**R5**
- Bloodthrill [5] — Grants your Main Hand melee attacks against enemies afflicted by your Rend a 4% chance to allow an activation of Overpower.
- Sweeping Strikes [1] — 30 Rage | Instant | 30 sec cooldown | Requires Battle Stance | Your next 5 melee attacks strike an additional nearby opponent.
- Weaponmaster [5] — Gives your melee weapon attacks a benefit depending on the weapon. | Axe/Polearm: Increases your | critical strike chance by 1%. | Mace/Staff: Your attacks ignore | 3% of your target's armor. | Sword: Your successful melee | attacks have a 1% chance to | trigger an extra attack on the | target.

**R6**
- Improved Slam [2] — Reduces the global cooldown and cast time of your Slam ability by 0.25 sec. In addition, Slam no longer interrupts or delays your melee swing and Slam's cooldown is reduced by 3 sec.
- Improved Hamstring [3] — Gives your Hamstring ability a 5% chance to immobilize the target for 5 sec.

**R7**
- Mortal Strike [1] — 30 Rage | Melee Range | Instant | 6 sec cooldown | A vicious strike that deals weapon damage plus 85 and wounds the target, reducing the effectiveness of any healing by 50% for 10 sec.

## Fury (17 talents)

**R1**
- Booming Voice [5] — Increases the area of effect of your Shouts by 10% and reduces their Rage cost by 5%.
- Cruelty [5] — Improves your chance to get a critical strike with melee attacks by 1%.

**R2**
- Lingering Rage [5] — Increases the time before your Rage begins to decay after leaving combat by 2 sec.
- Unbridled Wrath [5] — Gives you a 12% chance to generate 1 additional Rage when you deal melee damage with a weapon.

**R3**
- Furious Precision [3] — Increases your chance to hit with off-hand attacks by 4%.
- Piercing Howl [1] — 10 Rage | Instant | Causes all enemies within 10 yds to be Dazed, reducing movement speed by 50% for 6 sec.
- Blood Craze [3] — Regenerates 1% of your total Health over 6 sec after being the victim of a critical strike or suffering more than 20% of your maximum Health from a single attack.

**R4**
- Dual Wield Specialization [5] — Increases the damage done by your off-hand weapon by 5% and the Rage generated by your off-hand attacks by 10%.
- Raging Blows [1] — Reduces the Rage cost of your Cleave and Whirlwind abilities by 3.
- Enrage [5] — Gives you a 30% chance to deal 2% increased Physical damage for 12 sec after being the victim of any damaging attack.
- Improved Execute [2] — Reduces the Rage cost of your Execute ability by 3.

**R5**
- Improved Berserker Rage [2] — Your Berserker Rage ability will instantly generate 5 Rage and has a 50% chance to remove all movement impairing effects when activated.
- Death Wish [1] — 10 Rage | Instant | 3 min cooldown | When activated, increases your Physical damage done by 20% and makes you immune to Fear effects, but increases all damage you take by 5%. Lasts 30 sec.
- Improved Intercept [2] — Reduces the cooldown of your Intercept ability by 5 sec.

**R6**
- Flurry [5] — Increases your melee attack speed by 5% for your next 3 swings after dealing a melee critical strike.
- Gore Drinker [2] — Your Enrage, Berserker Rage, Bloodrage, Death Wish, and Bloodthirst abilities cause your next 3 melee attacks to restore 0.5% of your maximum Health.

**R7**
- Bloodthirst [1] — 30 Rage | Melee Range | Instant | 6 sec cooldown | Instantly attack the target causing damage equal to 45% of your Attack Power plus 30 and increasing your movement speed by 10% for 10 sec.

## Protection (18 talents)

**R1**
- Improved Bloodrage [2] — Increases all the Rage generated by your Bloodrage ability by 25%.
- Shield Specialization [5] — Increases your chance to Block attacks with your shield by 1% and grants you a 20% chance to generate 5 Rage when you Block.
- Iron Will [5] — Reduces the duration of Stun and Fear effects inflicted on you by 3%.

**R2**
- Anticipation [5] — Increases your Defense Skill by 4.
- Improved Revenge [3] — Increases damage dealt by your Revenge ability by 20%.
- Improved Thunder Clap [3] — Reduces the Rage cost of your Thunder Clap ability by 2.

**R3**
- Last Stand [1] — Instant | 3 min cooldown | When activated, this ability temporarily grants you 30% of your maximum health for 20 sec. After the effect expires, the health is lost.
- Master of Defense [2] — Grants you a 50% chance to generate 5 Rage when you Dodge or Parry while a shield is equipped.
- Improved Disarm [3] — Reduces the cooldown of your Disarm ability by 7 secs.
- Defiance [3] — Requires Defensive Stance | Increases all threat generated in Defensive stance by an additional 5% while a shield is equipped.

**R4**
- Improved Sunder Armor [3] — Reduces the Rage cost of your Sunder Armor ability by 1.
- Vanguard [1] — Your Charge ability is now usable while in Defensive Stance.
- Improved Shield Bash [2] — Gives your Shield Bash ability a 50% chance to Silence the target for 3 sec.

**R5**
- Improved Shield Wall [2] — Reduces the cooldown of your Shield Wall ability by 5.5 min.
- Concussion Blow [1] — 10 Rage | Melee Range | Instant | 45 sec cooldown | Stuns the target for 5 sec.
- Focused Rage [3] — Reduces the Rage cost of your offensive abilities by 1.

**R6**
- Bastion [5] — Increases all damage you deal by 2% while a shield is equipped.

**R7**
- Shield Slam [1] — 20 Rage | Melee Range | Instant | 6 sec cooldown | Requires Shields | Slam the target with your shield, causing 421 to 439 damage, increased by your Block Value, and has a 50% chance of dispelling 1 magic effect on the target. Causes a very high amount of threat.
