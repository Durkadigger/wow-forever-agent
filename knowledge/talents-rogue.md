# WoW Forever — Rogue Talents
Data as of: 2026-11-07 b:1.60.1.70862 (Overrides block: datamined, tier 2). Generated lines below the block: 2026-10-27 b:beta, tier 3, superseded wherever the block covers the same talent.
Source: classicwowforever.com talent calculator chunk. Rank-1 captured tooltips; higher ranks are the site's estimates. Values change with each build.
Provenance: [T3 cwf 2026-10-27 b:beta] applies to every talent line below unless an Overrides entry says otherwise. The tag date is the date this script fetched the site; the site's own capture may be earlier. Provenance tags: `[T<tier> <source-id> <date> b:<build>]`, see docs/sop-provenance.md and sources.md. Build labels in data/builds.json.

<!-- overrides -->
## Overrides (tier 1–2 values that outrank the generated lines)
*Full datamined tree, TraitTree 1111. [T2 wago 2026-11-07 b:1.60.1.70862] applies to every line in this block. Values written a/b/c are ranks 1/2/3, each read from the client's per-rank curves (TraitDefinitionEffectPoints), not extrapolated.*

### 24 Sept 2026 blue-post class changes (not talent-rank values)
*[T1 blizz-forum 2026-09-24] (Kaivax, WoW Forever Beta Development Notes – Updated September 24, https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-updated-september-24/2360696)*
- Sap now correctly flags the Rogue for PvP when used on a PvP-flagged target (bug fix).

### 1–27 Oct 2026 blue-post class changes, checked against b:1.60.1.70634 (not talent-rank values; layered on the tree below)
*[T1 blizz-forum 2026-10-16] unless a line carries its own tag. Source: Kaivax, WoW Forever Beta Development Notes (topic 2360696): posts of 1 Oct [T1 blizz-forum 2026-10-01], 8 Oct [T1 blizz-forum 2026-10-08] and 16 Oct. Where the 27 Oct datamine shows the same change the line also carries [T2 wago 2026-10-27 b:1.60.1.70634]. These notes supersede the 24 Sept block above wherever they overlap. Class deep-dive articles of 30 Sept to 15 Oct (blizz-news 24301515, 24301514, 24302097, 24310968, 24302099) describe the same beta changes and were not stored line by line.*
- Sap no longer triggers weapon procs and has a new mechanic category; Cold Blood is consumed correctly by Mutilate crits; Setup wording clarified; poisons no longer trigger on targets attacking the Rogue [T1 blizz-forum 2026-10-16; T2 wago 2026-10-27 b:1.60.1.70634].

### 6–7 Nov 2026 hotfixes and client build 1.60.1.70862
*[T1 blizz-forum 2026-11-06] (Kaivax, "WoW: Forever Hotfixes - November 6, 2026", https://us.forums.blizzard.com/en/wow/t/wow-forever-hotfixes-november-6-2026/2403040/4) unless a line carries its own tag; client build 1.60.1.70862 (7 Nov) carries the matching tooltip changes [T2 wago 2026-11-07 b:1.60.1.70862]. Builds 70840 and 70862 are the first post-launch client builds; 70840 was not snapshotted. No talent rank changed between 70790 and 70862.*
- Shank shows Rank 1 and Rank 2 in tooltips, and with Boot Knife talented shows the Combo Points it grants. Client: Shank descriptions (spells 1329283, 1329549) changed [T2 wago 2026-11-07 b:1.60.1.70862].
- Gouge and Kidney Shot descriptions are now rank-conditional strings (tooltip only) [T2 wago 2026-11-07 b:1.60.1.70862].

### Coverage note (7 Nov 2026)
*[T1 blizz-forum 2026-11-03]*
- The 2 Nov development notes carry a Rogue section that this file has not summarised line by line [T1 blizz-forum 2026-11-03] (Kaivax, WoW Forever Beta Development Notes, updated 2 Nov (topic 2360696, post 9, https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9)); the datamined tree below (b:1.60.1.70790, unchanged in b:1.60.1.70862) already reflects its talent changes, but non-talent lines (tooltips, cooldowns, spell changes) are only in the post. Read it before answering a Rogue question about launch changes.

### Assassination — datamined (17 talents, 46 points)

**R1**
- Improved Gouge [3] — Increases the duration of your Gouge ability by 0.5/1/1.5 sec. `id 13741`
- Remorseless Attacks [2] — After killing a non-trivial enemy, gives you a 20/40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. `id 14144`
- Malice [5] — Increases your critical strike chance with all attacks and Poisons by 1/2/3/4/5%. `id 14138`

**R2**
- Ruthlessness [3] — Gives your finishing moves a 20/40/60% chance to add a Combo Point to your target. `id 14156`
- Improved Expose Armor [2] — Reduces the Energy cost of your Expose Armor ability by 5/10, and refunds 1/2 Combo $LPoint:Points; when cast with 5 Combo Points. `id 14168`
- Improved Slice and Dice [3] — Increases the duration of your Slice and Dice ability by 15/30/45%. `id 14165`

**R3**
- Vigor [2] — Increases your maximum Energy by 5/10. `id 14983`
- Blood Splatter [1] — Increases the duration of your Rupture ability by 6 sec and your Garrote ability by 9 sec. `id 1329256`
- Lethality [2] — Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 10/20%. *(requires Malice)* `id 14128`

**R4**
- Vile Poisons [5] — Increases the damage dealt by your poisons by 4/8/12/16/20% and gives your poisons an additional 8/16/24/32/40% chance to resist dispel effects. `id 16513`
- Cold Blood [1] — 3 min CD. When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. `id 14177`
- Improved Poisons [5] — Increases the chance to apply Poisons to your target by 2/4/6/8/10%, and gives Poison applications a 10/20/30/40/50% chance to not consume a charge. `id 14113`

**R5**
- Relentless Strikes [5] — Your finishing moves have a 4/8/12/16/20% chance per Combo Point to restore 25 Energy. `id 14179`
- Venom [1] — Causes your Shank ability to increase your Poison damage by 30% and your chance to apply Poisons by 20% for 6 sec. `id 1329328`
- Improved Kidney Shot [2] — Enemies Stunned by your Kidney Shot ability take 5/10% increased damage from your poisons and attacks. `id 14174`

**R6**
- Seal Fate [3] — Your critical strikes from abilities that add Combo Points have a 33/66/100% chance to add an additional Combo Point. `id 14186`

**R7**
- Mutilate [1] — 60 energy, 5 yd. Instantly attacks with both weapons for 90% weapon damage plus an additional 39.6 with each weapon. Damage increased by 20% against Poisoned targets. Awards 2 Combo $LPoint:Points;. *(requires Venom)* `id 399956`

### Combat — datamined (19 talents, 48 points)

**R1**
- Coup de Grace [3] — Increases the damage done by your Eviscerate ability by 7/13/20%, and the damage and storage rate of your Death Mark ability by 7/13/20%. `id 14162`
- Efficient Strikes [2] — Reduces the Energy cost of your Sinister Strike and Hemorrhage abilities by 3/5. `id 13732`
- Lightning Reflexes [5] — Increases your Dodge chance by 1/2/3/4/5%. `id 13712`

**R2**
- Puncturing Wounds [3] — Increases the critical strike chance of your Backstab by 10/20/30% and your Mutilate by 5/10/15%, and gives Backstab a 15/30/45% chance to add an additional Combo Point. `id 1224716`
- Deflection [3] — Increases your Parry chance by 2/4/6%. `id 13713`
- Precision [3] — Improves your chance to hit by 1/2/3%. `id 13705`
- Improved Sprint [2] — Gives a 50/100% chance to remove all movement impairing effects when you activate your Sprint ability. `id 13743`

**R3**
- Endurance [2] — Reduces the cooldown of your Sprint and Evasion abilities by 30/60%. `id 13742`
- Riposte [1] — 10 energy, 5 yd, 6 sec CD. A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec. *(requires Deflection)* `id 14251`
- Composure [2] — Increases the Energy cost reduction of your Poised ability by 5/10. `id 1329265`

**R4**
- Improved Kick [2] — Gives your Kick ability a 50/100% chance to Silence the target for 2 sec. `id 13754`
- Flawless Execution [1] — Reduces the Energy cost of your Eviscerate ability by 15. `id 1310711`
- Weapon Expertise [2] — Reduces the chance for your attacks to be Dodged or Parried by 1/2%. *(requires Precision)* `id 30919`
- Aggression [3] — Increases the damage of your Sinister Strike and Eviscerate abilities by 5/10/15%. `id 18427`

**R5**
- Dual Wield Specialization [2] — Increases the damage done by your off-hand weapon by 25/50%. `id 13715`
- Blade Flurry [1] — 25 energy, 2 min CD. Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec. `id 13877`
- Hack and Slash [5] — Gives your melee weapon attacks a benefit depending on the weapon. |CFFFFFFFFAxe/Sword:|R Your successful melee attacks have a 1/2/3/4/5% chance to trigger an extra attack on the target. |CFFFFFFFFDagger/Fist:|R Increases your critical strike chance by 1/2/3/4/5%. |CFFFFFFFFMace:|R Your attacks ignore 3/6/9/12/15% of your target's armor. `id 13960`

**R6**
- Flash of Steel [5] — Increases the Energy generated by your Shank ability by 3/6/9/12/15 and reduces its cooldown by 0.4/0.8/1.2/1.6/2.0 sec. `id 1329284`

**R7**
- Adrenaline Rush [1] — 5 min CD. Increases your Energy regeneration rate by 100% for 15 sec. *(requires Blade Flurry)* `id 13750`

### Subtlety — datamined (18 talents, 43 points)

**R1**
- Setup [3] — Gives you a 15/30/45% chance to add a Combo Point to your target after Dodging their attack or fully resisting one of their spells. `id 13983`
- Master of Deception [3] — Reduces the chance enemies have to detect you while in Stealth mode as if you were 1/2/3 levels higher. `id 13958`
- Opportunity [5] — Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 4/8/12/16/20%. `id 14057`

**R2**
- Dirty Deeds [2] — Reduces the Energy cost of your Cheap Shot and Garrote abilities by 10/20, and your Garrote ability no longer requires you to be behind your target. `id 14082`
- Camouflage [3] — Reduces your speed penalty from your Stealth ability by 5/10/15% and reduces its cooldown by 2/4/6 sec. `id 13975`
- Improved Ambush [3] — Increases the critical strike chance of your Ambush ability by 15/30/45%. `id 14079`
- Dirty Tricks [2] — Reduces the Energy cost of your Sap and Blind abilities by 25/50%. `id 1224782`

**R3**
- Initiative [3] — Gives you a 33/67/100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. `id 13976`
- Premeditation [1] — 20 yd, 2 min CD. Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost. `id 14183`
- Serrated Blades [3] — Causes your attacks to ignore 3/6/9% of your target's Armor and increases the damage dealt by your Rupture ability by 10/20/30%. `id 14171`

**R4**
- Elusiveness [2] — Reduces the cooldown of your Vanish and Blind abilities by 45/90 sec. `id 13981`
- Ghostly Strike [1] — 40 energy, 5 yd, 20 sec CD. A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage, increases your chance to dodge by 15% for 7 sec, and causes your next Ambush or Garrote cast within 7 sec to not require Stealth. Awards 1 combo points. `id 14278`
- Quick Getaway [2] — Increases the maximum number of targets you may have Sapped by 1, and increases your movement speed by 15/30% for 3 sec after Sapping a target. *(requires Dirty Tricks)* `id 1310728`

**R5**
- Heightened Senses [2] — Increases your Stealth detection as if you were 1/3 levels higher and reduces your chance to be hit by spells and ranged attacks by 2/4%. `id 30894`
- Preparation [1] — 10 min CD. When activated, this ability immediately finishes the cooldown on your other Rogue abilities. `id 14185`
- Hemorrhage [1] — 35 energy, 5 yd. An instant strike that deals 100% weapon damage (145% if a Dagger is equipped) and causes the target to take 15% increased Rupture and Garrote damage from the Rogue. Lasts 15 sec. Awards 1 Combo Points. *(requires Serrated Blades)* `id 16511`

**R6**
- Boot Knife [5] — Grants your Shank ability a 20/40/60/80/100% chance to add 2 Combo Points to the target. `id 1329286`

**R7**
- Death Mark [1] — 25 energy, 20 yd, 10 sec CD. Finishing move that marks the target, storing a portion of the damage dealt by your attacks per Combo Point. Garrote and Rupture damage is stored at twice the rate. After 6 sec, the stored damage is dealt, up to a maximum increased by Attack Power and Critical Strike chance: 1 point : ${1*$<ratio>}% stored, ${((63+(1*102)+1*$<maxAP>*$apm)*($mcrit/100+1))*$<coup>} damage cap 2 points: ${2*$<ratio>}% stored, ${((63+(2*102)+2*$<maxAP>*$apm)*($mcrit/100+1))*$<coup>} damage cap 3 points: ${3*$<ratio>}% stored, ${((63+(3*102)+3*$<maxAP>*$apm)*($mcrit/100+1))*$<coup>} damage cap 4 points: ${4*$<ratio>}% stored, ${((63+(4*102)+4*$<maxAP>*$apm)*($mcrit/100+1))*$<coup>} damage cap 5 points: ${5*$<ratio>}% stored, ${((63+(5*102)+5*$<maxAP>*$apm)*($mcrit/100+1))*$<coup>} damage cap *(requires Preparation)* `id 1316709`

<!-- /overrides -->

## Assassination (17 talents)

**R1**
- Improved Gouge [3] — Increases the duration of your Gouge ability by 0.5 sec.
- Remorseless Attacks [2] — After killing a non-trivial enemy, gives you a 20% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec.
- Malice [5] — Increases your critical strike chance with all attacks and Poisons by 1%.

**R2**
- Ruthlessness [3] — Gives your finishing moves a 20% chance to add a Combo Point to your target.
- Murder [2] — Increases all damage dealt by 2% against Humanoid and Giant targets.
- Improved Slice and Dice [3] — Increases the duration of your Slice and Dice ability by 15%.

**R3**
- Relentless Strikes [1] — Your finishing moves have a 20% chance per Combo Point to restore 25 Energy.
- Improved Expose Armor [2] — Reduces the Energy cost of your Expose Armor ability by 5, and refunds 1 Combo Point when cast with 5 Combo Points.
- Lethality [5] — Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 4%.

**R4**
- Vile Poisons [5] — Increases the damage dealt by your poisons by 4% and gives your poisons an additional 8% chance to resist dispel effects.
- Cold Blood [1] — Instant | 3 min cooldown | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%.
- Improved Poisons [5] — Increases the chance to apply Poisons to your target by 2%, and gives Poison applications a 10% chance to not consume a charge.

**R5**
- Vigor [2] — Increases your maximum Energy by 5.
- Mutilate [1] — 60 Energy | Melee Range | Instant | Requires Daggers | Instantly attacks with both weapons for 75% weapon damage plus an additional 13 with each weapon. Damage increased by 20% against Poisoned targets. Awards 2 Combo Points.
- Improved Kidney Shot [2] — Enemies Stunned by your Kidney Shot ability take 5% increased damage from your poisons and attacks.

**R6**
- Seal Fate [5] — Your critical strikes from abilities that add Combo Points have a 20% chance to add an additional Combo Point.

**R7**
- Venom [1] — 25 Energy | 100 yd range | Instant | Finishing move that increases the damage of your Poisons by 30% and your chance to apply Poisons by 10%. Lasts longer per combo point: | 1 point : 9 sec | 2 points: 12 sec | 3 points: 15 sec | 4 points: 18 sec | 5 points: 21 sec

## Combat (17 talents)

**R1**
- Improved Eviscerate [3] — Increases the damage done by your Eviscerate ability by 7%.
- Improved Sinister Strike [2] — Reduces the Energy cost of your Sinister Strike ability by 3.
- Lightning Reflexes [5] — Increases your Dodge chance by 1%.

**R2**
- Puncturing Wounds [3] — Increases the critical strike chance of your Backstab by 10% and your Mutilate by 5%, and gives Backstab a 15% chance to add an additional Combo Point.
- Deflection [3] — Increases your Parry chance by 2%.
- Precision [3] — Improves your chance to hit by 1%.

**R3**
- Endurance [2] — Reduces the cooldown of your Sprint and Evasion abilities by 30%.
- Riposte [1] — 10 Energy | Melee Range | Instant | 6 sec cooldown | A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec.
- Improved Sprint [2] — Gives a 50% chance to remove all movement impairing effects when you activate your Sprint ability.

**R4**
- Improved Kick [2] — Gives your Kick ability a 50% chance to Silence the target for 2 sec.
- Flawless Execution [1] — Reduces the Energy cost of your Eviscerate ability by 10.
- Dual Wield Specialization [5] — Increases the damage done by your off-hand weapon by 5%.

**R5**
- Blade Flurry [1] — 25 Energy | Instant | 2 min cooldown | Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec.
- Hack and Slash [5] — Gives your melee weapon attacks a benefit depending on the weapon. | Axe/Sword: Your successful | melee attacks have a 1% chance | to trigger an extra attack on the | target. | Dagger/Fist: Increases your | critical strike chance by 1%. | Mace: Your attacks ignore 3% of | your target's armor.

**R6**
- Weapon Expertise [2] — Reduces the chance for your attacks to be Dodged or Parried by 1%.
- Aggression [3] — Increases the damage of your Sinister Strike, Backstab, and Eviscerate abilities by 2%.

**R7**
- Adrenaline Rush [1] — Instant | 5 min cooldown | Increases your Energy regeneration rate by 100% for 15 sec.

## Subtlety (19 talents)

**R1**
- Camouflage [5] — Reduces your speed penalty from your Stealth ability by 3% and reduces its cooldown by 2 sec.
- Master of Deception [3] — Reduces the chance enemies have to detect you while in Stealth mode as if you were 1 level higher.
- Opportunity [2] — Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 5%.

**R2**
- Setup [3] — Gives you a 33% chance to add a Combo Point to your target after Dodging one of their attacks or fully resisting one of their spells.
- Elusiveness [2] — Reduces the cooldown of your Vanish and Blind abilities by 45 sec.
- Dirty Tricks [2] — Reduces the Energy cost of your Sap and Blind abilities by 25%.
- Improved Ambush [3] — Increases the critical strike chance of your Ambush ability by 15%.

**R3**
- Initiative [3] — Gives you a 33% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability.
- Ghostly Strike [1] — 40 Energy | Melee Range | Instant | 20 sec cooldown | A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point.
- Improved Distract [2] — Increases the radius of your Distract ability by 3 yds, and further reduces the Stealth detection of distracted enemies as though they were an additional 1 level lower.

**R4**
- Heightened Senses [2] — Increases your Stealth detection as if you were 1 level higher and reduces your chance to be hit by spells and ranged attacks by 2%.
- Premeditation [1] — 20 yd range | Instant | 2 min cooldown | Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost.
- Serrated Blades [3] — Causes your attacks to ignore 3% of your target's Armor and increases the damage dealt by your Rupture ability by 10%.

**R5**
- Dirty Deeds [2] — Reduces the Energy cost of your Cheap Shot and Garrote abilities by 10, and your Garrote ability no longer requires you to be behind your target.
- Preparation [1] — Instant | 10 min cooldown | When activated, this ability immediately finishes the cooldown on your other Rogue abilities.
- Hemorrhage [1] — 35 Energy | Melee Range | Instant | An instant strike that deals 100% weapon damage (145% if a Dagger is equipped) and causes the target to take 15% increased Rupture damage from the Rogue. Lasts 15 sec. Awards 1 Combo Point.

**R6**
- Quietus [5] — Your Sinister Strike, Ghostly Strike, and Hemorrhage abilities cause 2% more damage against targets below 35% health.
- Cutthroat [5] — Your Backstab has a 3% chance to cause your next Ambush within 10 sec to not require Stealth.

**R7**
- Thousand Cuts [1] — When your Rupture ability deals periodic damage, the Energy cost of your next Hemorrhage or Backstab ability within 10 sec is reduced by 3, stacking up to 5 times.
