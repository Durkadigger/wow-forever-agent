# WoW Forever — Druid Talents
Data as of: 2026-11-07 b:1.60.1.70862 (Overrides block: datamined, tier 2). Generated lines below the block: 2026-10-27 b:beta, tier 3, superseded wherever the block covers the same talent.
Source: classicwowforever.com talent calculator chunk. Rank-1 captured tooltips; higher ranks are the site's estimates. Values change with each build.
Provenance: [T3 cwf 2026-10-27 b:beta] applies to every talent line below unless an Overrides entry says otherwise. The tag date is the date this script fetched the site; the site's own capture may be earlier. Provenance tags: `[T<tier> <source-id> <date> b:<build>]`, see docs/sop-provenance.md and sources.md. Build labels in data/builds.json.

<!-- overrides -->
## Overrides (tier 1–2 values that outrank the generated lines)
*Full datamined tree, TraitTree 1089. [T2 wago 2026-11-07 b:1.60.1.70862] applies to every line in this block. Values written a/b/c are ranks 1/2/3, each read from the client's per-rank curves (TraitDefinitionEffectPoints), not extrapolated.*

### 24 Sept 2026 blue-post class changes (not talent-rank values)
*[T1 blizz-forum 2026-09-24] (Kaivax, WoW Forever Beta Development Notes – Updated September 24, https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-updated-september-24/2360696)*
- Rejuvenation and Tranquility can now land critical hits (bug fix).
- Wrath base damage increased ~50%.
- Thorns now dynamically scales with the caster's spell power (reverts to base values if the caster can't be found or is too far away).
- Feral: Mangle renamed Primal Bite (signature debuff removed); Primal Fury talent renamed Blood Frenzy (see tree below, already updated); Feral Charge (Cat) can no longer be cast on allies (bug fix).
- Restoration: Wild Growth can now land critical hits (bug fix).

### 1–27 Oct 2026 blue-post class changes, checked against b:1.60.1.70634 (not talent-rank values; layered on the tree below)
*[T1 blizz-forum 2026-10-16] unless a line carries its own tag. Source: Kaivax, WoW Forever Beta Development Notes (topic 2360696): posts of 1 Oct [T1 blizz-forum 2026-10-01], 8 Oct [T1 blizz-forum 2026-10-08] and 16 Oct. Where the 27 Oct datamine shows the same change the line also carries [T2 wago 2026-10-27 b:1.60.1.70634]. These notes supersede the 24 Sept block above wherever they overlap. Class deep-dive articles of 30 Sept to 15 Oct (blizz-news 24301515, 24301514, 24302097, 24310968, 24302099) describe the same beta changes and were not stored line by line.*
- **Feral:** Tiger's Fury and King of the Jungle removed; new row-4 talent Shifting Power (Cat Form, 55% of base mana for 40 Energy, 16 sec CD) and row-5 Improved Shifting Power (cooldown 4 / 8 sec shorter) [T1 blizz-forum 2026-10-01; T2 wago 2026-10-27 b:1.60.1.70634]. Predatory Instincts renamed Natural Instinct and also adds spell healing of 12 / 25% of Intellect [T1 blizz-forum 2026-10-08; T2 wago 2026-10-27 b:1.60.1.70634]. Primal Bite generates high threat (roughly doubled) [T1 blizz-forum 2026-10-01]. Furor keeps your Cat Form Energy when shifting through Bear Form [T1 blizz-forum 2026-10-16].
- **Auras:** Leader of the Pack is now raid-wide and melee/ranged crit only; Moonkin Aura is raid-wide and spell crit only [T1 blizz-forum 2026-10-16; T2 wago 2026-10-27 b:1.60.1.70634].
- **Forms and spells:** Bear and Dire Bear threat bonus 50% (was 30%) [T1 blizz-forum 2026-10-08]; forms are immune to Disarm [T1 blizz-forum 2026-10-01]; Thorns base damage back to Vanilla values with a 6% spell power ratio (was 13.3%) [T1 blizz-forum 2026-10-08]; Rage from crits 100% (was 75%) [T1 blizz-forum 2026-10-08]; Rejuvenation high ranks no longer block other Druids' Rejuvenation [T1 blizz-forum 2026-10-16]. Wrath ranks 1 to 5 retuned [T1 blizz-forum 2026-10-08]. Nature's Focus wording changed to "chance to not lose casting time" with the same 14 / 28 / 42 / 56 / 70% [T2 wago 2026-10-27 b:1.60.1.70634].

### 6–7 Nov 2026 hotfixes and client build 1.60.1.70862
*[T1 blizz-forum 2026-11-06] (Kaivax, "WoW: Forever Hotfixes - November 6, 2026", https://us.forums.blizzard.com/en/wow/t/wow-forever-hotfixes-november-6-2026/2403040/4) unless a line carries its own tag; client build 1.60.1.70862 (7 Nov) carries the matching tooltip changes [T2 wago 2026-11-07 b:1.60.1.70862]. Builds 70840 and 70862 are the first post-launch client builds; 70840 was not snapshotted. No talent rank changed between 70790 and 70862.*
- Bloom now correctly heals the target.
- Bear Form tooltip reported a wrong health value; functionality was already correct. Client: Bear Form (Passive2, spell 21178) effect value 50 → 115 and the Bear Form description text changed [T2 wago 2026-11-07 b:1.60.1.70862].
- Ravage tooltip showed a wrong damage value, corrected; no damage change. Client: all four Ravage ranks' descriptions changed [T2 wago 2026-11-07 b:1.60.1.70862].
- Swiftmend tooltip no longer says it consumes the effect. Thorns description now reads `$s1` instead of `$w1` on all six ranks (tooltip only) [T2 wago 2026-11-07 b:1.60.1.70862].
- Night Elf: Shadowmelded Druids no longer get Ravage and Pounce (bug fix).

### Coverage note (7 Nov 2026)
*[T1 blizz-forum 2026-11-03]*
- The 2 Nov development notes carry a Druid section that this file has not summarised line by line [T1 blizz-forum 2026-11-03] (Kaivax, WoW Forever Beta Development Notes, updated 2 Nov (topic 2360696, post 9, https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9)); the datamined tree below (b:1.60.1.70790, unchanged in b:1.60.1.70862) already reflects its talent changes, but non-talent lines (tooltips, cooldowns, spell changes) are only in the post. Read it before answering a Druid question about launch changes.

### Balance — datamined (16 talents, 46 points)

**R1**
- Improved Wrath [5] — Reduces the cast time of your Wrath spell by 0.1/0.2/0.3/0.4/0.5 sec and its Mana cost by 10/20/30/40/50%. `id 16814`
- Genesis [5] — Increases the periodic damage and healing done by your spells and abilities by 2/4/6/8/10%. `id 1223081`

**R2**
- Moonglow [3] — Reduces the Mana cost of your damaging spells by 8/17/25%. `id 16845`
- Improved Moonfire [2] — Increases the damage and critical strike chance of your Moonfire spell by 5/10%. `id 16821`
- Nature's Majesty [2] — Increases your critical strike chance with spells and melee attacks by 2/4%. *(requires Nature's Splendor)* `id 1223082`
- Nature's Reach [2] — Increases the range of your offensive Balance spells by 10/20% and improves your chance to hit by 2/4%. `id 16819`

**R3**
- Improved Entangling Roots [3] — Increases the damage done by your Entangling Roots spell by 25/50/75%, and its victims can take up to 25/50/75% more damage without interrupting the effect. `id 16918`
- Nature's Splendor [1] — Increases the duration of your Moonfire and Rejuvenation spells by 3 sec, your Regrowth spell by 6 sec, and your Insect Swarm spell by 2 sec. *(requires Nature's Majesty)* `id 1223083`

**R4**
- Insect Swarm [1] — 45 mana, 30 yd, spell power coeff 0.158; numbers are level 60 with 0 spell power. The enemy target is swarmed by insects, decreasing their chance to hit with attacks by 2% and causing 48 Nature damage over 12 sec. `id 5570`
- Vengeance [5] — Increases the critical strike damage bonus of your Arcane and Nature spells by 20/40/60/80/100%. *(requires Improved Moonfire)* `id 16909`
- Improved Starfire [5] — Reduces the cast time of Starfire by 0.1/0.2/0.3/0.4/0.5 sec and Starfire has a 3/6/9/12/15% chance to stun its target for 3 sec. `id 16850`

**R5**
- Overgrowth [2] — Increases the maximum number of targets you may have affected by Entangling Roots by 1/2. `id 17245`
- Nature's Grace [1] — All non-periodic spell criticals grace you with a blessing of nature, increasing your spellcasting speed and reducing your global cooldown by 10% for 3 sec. `id 16880`
- Eclipse [3] — Your Wrath spell reduces the cast time of your next 2 Starfire spells by 0.17/0.33/0.50 sec. Stores up to 4 charges. Lasts 15 sec. `id 408248`

**R6**
- Moonfury [5] — Increases the damage done by your Arcane and Nature spells by 2/4/6/8/10%. `id 16896`

**R7**
- Moonkin Form [1] — 35% of base mana. Shapeshift into Moonkin Form, increasing Omen of Clarity's chance to trigger by 100%, Armor contribution from items by 360%, and all party or raid members within 45 yards have their Critical Strike chance increased by 3%. Also protects the caster from Polymorph effects and prevents the use of healing spells. The act of shapeshifting frees the caster of Polymorph and Movement Impairing effects. `id 24858`

### Feral Combat — datamined (20 talents, 50 points)

**R1**
- Ferocity [5] — Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 1/2/3/4/5 Rage or Energy. `id 16934`
- Furor [5] — Gives you a 20/40/60/80/100% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 20/40/60/80/100% of the Energy you had when last in Cat Form, plus 2/4/6/8/10 Energy per second spent outside Bear Form or Dire Bear Form, up to 20/40/60/80/100 Energy. `id 17056`

**R2**
- Feral Swiftness [2] — Increases your movement speed while in Cat Form by 15/30%, and increases your chance to Dodge by 2/4%. `id 17002`
- Feral Instinct [3] — Increases damage done by your Swipe ability by 10/20/30% and reduces the chance enemies have to detect you while Prowling as if you were 1/2/3 levels higher. `id 16947`
- Brutal Impact [2] — Increases the stun duration of your Bash and Pounce abilities by 0.5/1 sec and reduces the cooldown of Bash by 15/30 sec. `id 16940`
- Thick Hide [3] — While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 1/2/3 additional base Armor per level and another 0.67/1.33/2.00 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms. `id 16929`

**R3**
- Shredding Attacks [3] — Reduces the Energy cost of your Shred ability by 6/12/18 and reduces the Rage cost of your Lacerate ability by 1/2/3. `id 16966`
- Savage Fury [2] — Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 5/10%. `id 16998`
- Feral Charge [1] — 5 rage, 25 yd, 15 sec CD. $?a5487|a9634[|CFFFFFFFFRequires Bear Form, Dire Bear Form|R][|CFFFF2020Requires Bear Form, Dire Bear Form|R] Charge an enemy, immobilizing them and interrupting any spell they are casting for 4 sec. $@spelltooltip414924 `id 1238122`
- Sharpened Claws [2] — Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 3/6%. `id 16942`

**R4**
- Predatory Strikes [3] — Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 50/100/150% of your level. `id 16972`
- Lacerate [1] — 15 rage, 5 yd. Lacerates the enemy target, making them bleed for 20 damage over 15 sec plus 10% weapon damage per existing application of Lacerate on the target. Causes a high amount of threat. This effect stacks up to 5 times on the same target. *(requires Savage Fury)* `id 1328617`
- Predatory Discipline [1] — Your Ferocious Bite ability no longer converts extra Energy into damage, but still deals extra damage based on your excess Energy. `id 1328613`
- Blood Frenzy [2] — Gives you a 50/100% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 50/100% chance to add an additional Combo Point. *(requires Sharpened Claws)* `id 16958`

**R5**
- Leader of the Pack [1] — While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the Critical Strike chance of all party or raid members within 45 yards by 3%. `id 17007`
- Natural Instinct [2] — Increases the critical strike damage bonus of your melee abilities by 10/20% and increases your spell healing by 12/25% of your Intellect. `id 1223242`

**R6**
- Rend and Tear [5] — Increases damage done by your melee abilities on Bleeding targets by 3/6/9/12/15%. *(requires Predatory Strikes)* `id 1223246`
- Natural Reaction [5] — Increases your dodge chance by 1/2/3/4/5%, and gives you a 20/40/60/80/100% chance to gain 5 Rage each time you dodge. `id 417051`

**R7**
- Primal Bite [1] — 20 rage, 5 yd, 6 sec CD. Bite the target, dealing 100% normal damage plus 42 and generating a high amount of threat. *(requires Leader of the Pack)* `id 407995`
- Shifting Power [1] — 55% of base mana, 8 sec CD. Instantly convert $c Mana into $s2 Energy. Shifting Power's cost is reduced by effects that reduce the cost of Shapeshifting. *(requires Predatory Discipline)* `id 1322605`

### Restoration — datamined (16 talents, 51 points)

**R1**
- Nature's Focus [5] — Gives your Arcane and Nature spells a 14/28/42/56/70% chance to not lose casting time when you take damage. `id 17063`
- Heart of the Wild [5] — Increases your Intellect by 2/4/6/8/10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 4/8/12/16/20% and while in Cat Form your Strength is increased by 2/4/6/8/10%. `id 17003`

**R2**
- Naturalist [5] — Reduces the cast time of your Healing Touch and Wild Growth spells by 0.1/0.2/0.3/0.4/0.5 sec and increases all damage you deal by 2/4/6/8/10%. `id 17069`
- Reflection [3] — Allows 17/33/50% of your Mana regeneration to continue while casting. `id 17106`
- Natural Shapeshifter [3] — Reduces the mana cost of all shapeshifting by 10/20/30%. `id 16833`

**R3**
- Subtlety [3] — Reduces the threat generated by your Nature and Arcane spells by 10/20/30%. `id 17118`
- Gift of Nature [5] — Increases the effect of all your healing spells by 2/4/6/8/10%. `id 17104`
- Bloom [1] — When your Rejuvenation or Regrowth spell expires due to its duration, the target is instantly healed for an amount equal to 100% of your Spirit. If either spell expires due to being dispelled, the target is healed for 50% of your Spirit instead. `id 1328621`

**R4**
- Tranquil Spirit [5] — Reduces the mana cost of your Healing Touch and Tranquility spells by 2/4/6/8/10%. `id 24968`
- Improved Rejuvenation [3] — Increases the effect of your Rejuvenation spell by 5/10/15%. `id 17111`
- Swiftmend [1] — 20% of base mana, 40 yd, 15 sec CD. Instantly heals a target with your active Rejuvenation or Regrowth effect for an amount equal to the full duration of the periodic effect of the consumed spell. `id 18562`

**R5**
- Nature's Swiftness [1] — 3 min CD. When activated, your next Nature spell becomes an instant cast spell. *(requires Naturalist)* `id 17116`
- Living Spirit [3] — Increases your Spirit by 5/10/15%. `id 1309631`
- Improved Tranquility [2] — Reduces threat caused by Tranquility by 50/100% and its cooldown by 30/60%. `id 17123`

**R6**
- Improved Regrowth [5] — Increases the critical effect chance of your Regrowth spell by 10/20/30/40/50%. *(requires Improved Rejuvenation)* `id 17074`

**R7**
- Wild Growth [1] — 550 mana, 40 yd, 3 sec cast, 6 sec CD, spell power coeff 0.033; numbers are level 60 with 0 spell power. Heals the target and their party for 336 over 7 sec. Party members must be within 43.5 yards of target. The amount healed is applied quickly at first, and slows down as Wild Growth reaches its full duration. *(requires Living Spirit)* `id 408120`

<!-- /overrides -->

## Balance (16 talents)

**R1**
- Improved Wrath [5] — Reduces the cast time of your Wrath spell by 0.1 sec and its Mana cost by 10%.
- Genesis [5] — Increases the periodic damage and healing done by your spells and abilities by 1%.

**R2**
- Moonglow [3] — Reduces the Mana cost of your damaging spells by 8%.
- Improved Moonfire [2] — Increases the damage and critical strike chance of your Moonfire spell by 5%.
- Nature's Majesty [2] — Increases your critical strike chance with spells and melee attacks by 2%.
- Nature's Reach [2] — Increases the range of your offensive Balance spells by 10% and improves your chance to hit by 2%.

**R3**
- Improved Entangling Roots [3] — Increases the damage done by your Entangling Roots spell by 25%, and its victims can take up to 25% more damage without interrupting the effect.
- Nature's Splendor [1] — Increases the duration of your Moonfire and Rejuvenation spells by 3 sec, your Regrowth spell by 6 sec, and your Insect Swarm spell by 2 sec.

**R4**
- Insect Swarm [1] — 45 Mana | 30 yd range | Instant | The enemy target is swarmed by insects, decreasing their chance to hit with attacks by 2% and causing 48 Nature damage over 12 sec.
- Vengeance [5] — Increases the critical strike damage bonus of your Arcane and Nature spells by 20%.
- Improved Starfire [5] — Reduces the cast time of Starfire by 0.1 sec and Starfire has a 3% chance to stun its target for 3 sec.

**R5**
- Overgrowth [2] — Increases the maximum number of targets you may have affected by Entangling Roots by 1.
- Nature's Grace [1] — All non-periodic spell criticals grace you with a blessing of nature, increasing your spellcasting speed and reducing your global cooldown by 10% for 3 sec.
- Eclipse [3] — Your Wrath spell reduces the cast time of your next 2 Starfire spells by 0.17 sec. Stores up to 4 charges. Lasts 15 sec.

**R6**
- Moonfury [5] — Increases the damage done by your Arcane and Nature spells by 2%.

**R7**
- Moonkin Form [1] — 35% of base mana | Instant | Shapeshift into Moonkin Form, increasing Omen of Clarity's chance to trigger by 100%, Armor contribution from items by 360%, and all party or raid members within 45 yards have their spell Critical Strike chance increased by 3%. Also protects the caster from Polymorph effects and prevents the use of healing spells. | The act of shapeshifting frees the caster of Polymorph and Movement Impairing effects.

## Feral Combat (20 talents)

**R1**
- Ferocity [5] — Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 1 Rage or Energy.
- Heart of the Wild [5] — Increases your Intellect by 2%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 4% and while in Cat Form your Strength is increased by 2%.

**R2**
- Feral Swiftness [2] — Increases your movement speed while in Cat Form by 15%, and increases your chance to Dodge by 2%.
- Feral Instinct [3] — Increases damage done by your Swipe ability by 10% and reduces the chance enemies have to detect you while Prowling as if you were 1 level higher.
- Brutal Impact [2] — Increases the stun duration of your Bash and Pounce abilities by 0.5 sec and reduces the cooldown of Bash by 15 sec.
- Thick Hide [3] — While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 1 additional base Armor per level and another 0.67 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms.

**R3**
- Shredding Attacks [3] — Reduces the Energy cost of your Shred ability by 6 and reduces the Rage cost of your Lacerate ability by 1.
- Savage Fury [2] — Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 5%.
- Feral Charge [1] — 5 Rage | 8-25 yd range | Instant | 15 sec cooldown | Requires Cat Form, Bear Form, Dire Bear Form | Charge an enemy, immobilizing them and interrupting any spell they are casting for 4 sec. | Leap behind an enemy.
- Sharpened Claws [2] — Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 3%.

**R4**
- Shifting Power [1] — 55% of base mana | Instant | 16 sec cooldown | Requires Cat Form | Instantly convert 55% of base Mana into 40 Energy. Shifting Power's cost is reduced by effects that reduce the cost of Shapeshifting.
- Primal Bite [1] — 20 Rage | Melee Range | Instant | 6 sec cooldown | Requires Bear Form, Dire Bear Form | Bite the target, dealing 100% normal damage plus 26 and generating a high amount of threat.
- Predatory Strikes [3] — Requires Cat Form, Bear Form, Dire Bear Form | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 50% of your level.
- Blood Frenzy [2] — Gives you a 50% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 50% chance to add an additional Combo Point.

**R5**
- Improved Shifting Power [2] — Reduces the cooldown of your Shifting Power spell by 4 sec.
- Leader of the Pack [1] — While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the melee and ranged Critical Strike chance of all party or raid members within 45 yards by 3%.
- Natural Instinct [2] — Increases the critical strike damage bonus of your melee abilities by 10% and increases your spell healing by 12% of your Intellect.

**R6**
- Natural Reaction [5] — Requires Bear Form, Dire Bear Form | Increases your dodge chance by 1%, and gives you a 20% chance to gain 5 Rage each time you dodge.
- Rend and Tear [5] — Increases damage done by your melee abilities on Bleeding targets by 2%.

**R7**
- Berserk [1] — Instant | 3 min cooldown | Requires Cat Form, Bear Form, Dire Bear Form | Causes your Primal Bite ability to strike up to 3 targets, removes its cooldown, and increases the critical strike chance of your Combo Point-generating abilities by 100%. Clears and grants immunity to Fear effects for the duration. Lasts 15 sec.

## Restoration (16 talents)

**R1**
- Nature's Focus [5] — Gives you a 14% chance to avoid interruption caused by damage while casting Arcane and Nature spells.
- Furor [5] — Gives you a 20% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 20% of the Energy you had when last in Cat Form, plus 2 Energy per second spent outside Bear Form or Dire Bear Form, up to 20 Energy.

**R2**
- Naturalist [5] — Reduces the cast time of your Healing Touch spell by 0.1 sec and increases all damage you deal by 1%.
- Subtlety [3] — Reduces the threat generated by your Nature and Arcane spells by 10%.
- Natural Shapeshifter [3] — Reduces the mana cost of all shapeshifting by 10%.

**R3**
- Reflection [3] — Allows 17% of your Mana regeneration to continue while casting.
- Gift of Nature [5] — Increases the effect of all your healing spells by 2%.
- Gift of the Earthmother [1] — Reduces the global cooldown by 0.5 seconds on your Rejuvenation, Swiftmend, and Wild Growth spells.

**R4**
- Tranquil Spirit [5] — Reduces the mana cost of your Healing Touch and Tranquility spells by 2%.
- Improved Rejuvenation [3] — Increases the effect of your Rejuvenation spell by 5%.
- Swiftmend [1] — 20% of base mana | 40 yd range | Instant | 15 sec cooldown | Instantly heals a target with an active Rejuvenation or Regrowth effect for an amount equal to the full duration of the periodic effect of one of those spells.

**R5**
- Nature's Swiftness [1] — Instant | 3 min cooldown | When activated, your next Nature spell becomes an instant cast spell.
- Living Spirit [3] — Increases your Spirit by 5%.
- Improved Tranquility [2] — Reduces threat caused by Tranquility by 50% and its cooldown by 30%.

**R6**
- Improved Regrowth [5] — Increases the critical effect chance of your Regrowth spell by 10%.

**R7**
- Wild Growth [1] — 550 Mana | 40 yd range | Instant | 6 sec cooldown | Heals the target and their party for 336 over 7 sec. Party members must be within 43 yards of target. The amount healed is applied quickly at first, and slows down as Wild Growth reaches its full duration.
