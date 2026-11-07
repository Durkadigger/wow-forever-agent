# WoW Forever — Hunter Talents
Data as of: 2026-11-07 b:1.60.1.70862 (Overrides block: datamined, tier 2). Generated lines below the block: 2026-10-27 b:beta, tier 3, superseded wherever the block covers the same talent.
Source: classicwowforever.com talent calculator chunk. Rank-1 captured tooltips; higher ranks are the site's estimates. Values change with each build.
Provenance: [T3 cwf 2026-10-27 b:beta] applies to every talent line below unless an Overrides entry says otherwise. The tag date is the date this script fetched the site; the site's own capture may be earlier. Provenance tags: `[T<tier> <source-id> <date> b:<build>]`, see docs/sop-provenance.md and sources.md. Build labels in data/builds.json.

<!-- overrides -->
## Overrides (tier 1–2 values that outrank the generated lines)
*Full datamined tree, TraitTree 1091. [T2 wago 2026-11-07 b:1.60.1.70862] applies to every line in this block. Values written a/b/c are ranks 1/2/3, each read from the client's per-rank curves (TraitDefinitionEffectPoints), not extrapolated.*

### 24 Sept 2026 blue-post class changes (not talent-rank values)
*[T1 blizz-forum 2026-09-24] (Kaivax, WoW Forever Beta Development Notes – Updated September 24, https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-updated-september-24/2360696)*
- Pets: Furious Howl Attack Power bonus reduced 40%. Tame Beast no longer works on beasts higher level than the Hunter.
- Marksmanship: talenting out of Lone Wolf no longer leaves a -4% damage penalty while the pet is active (bug fix).
- Survival: Lacerating Strikes can now land critical hits (bug fix). Strider Kick now also increases movement speed 30% for 3 sec (tree below already updated).

### 1–27 Oct 2026 blue-post class changes, checked against b:1.60.1.70634 (not talent-rank values; layered on the tree below)
*[T1 blizz-forum 2026-10-16] unless a line carries its own tag. Source: Kaivax, WoW Forever Beta Development Notes (topic 2360696): posts of 1 Oct [T1 blizz-forum 2026-10-01], 8 Oct [T1 blizz-forum 2026-10-08] and 16 Oct. Where the 27 Oct datamine shows the same change the line also carries [T2 wago 2026-10-27 b:1.60.1.70634]. These notes supersede the 24 Sept block above wherever they overlap. Class deep-dive articles of 30 Sept to 15 Oct (blizz-news 24301515, 24301514, 24302097, 24310968, 24302099) describe the same beta changes and were not stored line by line.*
- **Marksmanship:** Sniper Shot is a 45 yd shot that also adds 10 yd of range to your next 3 shots for 10 sec [T1 blizz-forum 2026-10-01; T2 wago 2026-10-27 b:1.60.1.70634]. Trueshot Aura is raid-wide [T1 blizz-forum 2026-10-16; T2 wago 2026-10-27 b:1.60.1.70634].
- **Survival:** Deflection parry 1 / 2 / 3 / 4 / 5% (was 2 to 10%) [T1 blizz-forum 2026-10-01; T2 wago 2026-10-27 b:1.60.1.70634]. Expose Prey lasts 10 sec (was 5) [T1 blizz-forum 2026-10-08; T2 wago 2026-10-27 b:1.60.1.70634]. Resourcefulness now works only on melee and ranged ability crits, not traps [T1 blizz-forum 2026-10-16; T2 wago 2026-10-27 b:1.60.1.70634].
- **General:** Auto Shot requires standing still for 0.5 sec; Fire and Ice traps can be active together; pet Dismember, Sonic Blast and Mine! were weakened; Hunter pet Ferocity crit shows wrongly on the character sheet (visual bug) [T1 blizz-forum 2026-10-16; T1 blizz-forum 2026-10-08].

### 6 Nov 2026: 10 Nov tuning notice
*[T1 blizz-forum 2026-11-06] (Kaivax, "WoW: Forever Hotfixes - November 6, 2026", https://us.forums.blizzard.com/en/wow/t/wow-forever-hotfixes-november-6-2026/2403040/4) unless a line carries its own tag; client build 1.60.1.70862 (7 Nov) carries the matching tooltip changes [T2 wago 2026-11-07 b:1.60.1.70862]. Builds 70840 and 70862 are the first post-launch client builds; 70840 was not snapshotted. No talent rank changed between 70790 and 70862.*
- **Announced for a 10 Nov hotfix** [T1 blizz-forum 2026-11-06] (Kaivax, "Class Tuning Incoming - November 10", https://us.forums.blizzard.com/en/wow/t/class-tuning-incoming-november-10/2404092/1): Hunter pets tank worse than intended; Blizzard will adjust pet stats so their effectiveness matches Classic Era. Nothing in the 6 Nov hotfix list names Hunter. Current values stand until the hotfix lands.
- Orc Command (+5% Hunter and Warlock pet damage) was re-added in the 26 Oct notes [T1 blizz-forum 2026-10-26] and is in the launch client; a 6 Nov hotfix stopped some Warlock pet abilities over-benefiting from it (`racials.md`).

### Coverage note (7 Nov 2026)
*[T1 blizz-forum 2026-11-03]*
- The 2 Nov development notes carry a Hunter section that this file has not summarised line by line [T1 blizz-forum 2026-11-03] (Kaivax, WoW Forever Beta Development Notes, updated 2 Nov (topic 2360696, post 9, https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9)); the datamined tree below (b:1.60.1.70790, unchanged in b:1.60.1.70862) already reflects its talent changes, but non-talent lines (tooltips, cooldowns, spell changes) are only in the post. Read it before answering a Hunter question about launch changes.

### Beast Mastery — datamined (16 talents, 44 points)

**R1**
- Deadly Aspects [5] — While Aspect of the Hawk is active, Auto Shot has a 2/4/6/8/10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 2/4/6/8/10% chance of increasing melee attack speed by 30% for 12 sec. `id 19552`
- Endurance Training [5] — Increases the Health and Armor of your pets by 3/6/9/12/15%. `id 19583`

**R2**
- Focused Fire [2] — Increases all damage you and your pet deal by 1/2% while your pet is active. `id 1223755`
- Improved Aspect of the Monkey [3] — 100 yd. Increases the Dodge bonus of your Aspect of the Monkey by 2/4/6%. Additionally, your pet gains 50% of the effect of your Aspect of the Monkey ability. `id 19549`
- Improved Revive Pet [2] — Revive Pet's casting time is reduced by 3/6 sec, mana cost is reduced by 20/40%, and increases the health your pet returns with by an additional 15/30%. `id 24443`

**R3**
- Pathfinding [2] — Increases the speed bonus of your Aspect of the Cheetah and Aspect of the Pack by 3/6%. `id 19559`
- Bestial Swiftness [1] — Increases the movement speed of your pets by 30%. `id 19596`
- Unleashed Fury [5] — Increases the damage done by your pets and hawks by 3/6/9/12/15%. `id 19616`

**R4**
- Improved Mend Pet [2] — Gives your Mend Pet spell a 15/50% chance of cleansing 1 Curse, Disease, Magic, or Poison effect from your pet each time it heals and reduces the Mana cost by 10/20%. `id 19572`
- Ferocity [5] — Increases the critical strike chance of your pets and hawks by 2/4/6/8/10%. `id 19598`
- Summon Hawk [1] — 80 mana, 35 yd, -1000 sec cast, 6 sec CD. Command a hawk to dive-bomb your targeted enemy, dealing ${32+($rap*(5/100))} Physical damage and continuing its assault for 18 sec. Only 2 hawks can be active at once. Summon Hawk shares its cooldown with Arcane Shot. `id 1293241`

**R5**
- Spirit Bond [2] — While your pet is active, you and your pet will regenerate 1% of total health every 10/5 sec. `id 19578`
- Intimidation [1] — 8% of base mana, 100 yd, 1 min CD. Command your pet to Stun the target for 3 sec on its next successful attack, which also gains 100% increased critical strike chance. Generates high threat. *(requires Bestial Swiftness, Bestial Wrath)* `id 19577`
- Bestial Discipline [2] — Increases the Focus regeneration of your pets by 10/20% and allows 25/50% of your Mana regeneration to continue while casting. `id 19590`

**R6**
- Frenzy [5] — Gives your pet a 20/40/60/80/100% chance to gain a 30% attack speed increase for 8 sec after dealing a critical strike. *(requires Ferocity)* `id 19621`

**R7**
- Bestial Wrath [1] — 12% of base mana, 100 yd, 2 min CD. Send your pet into a rage causing 50% additional damage for 18 sec. While enraged, the beast does not feel pity or remorse or fear and it cannot be stopped unless killed. *(requires Intimidation)* `id 19574`

### Marksmanship — datamined (17 talents, 57 points)

**R1**
- Hawk Eye [3] — Increases the range of your ranged weapons by 2/4/6 yards. `id 19498`
- Improved Concussive Shot [5] — Gives your Concussive Shot a 4/8/12/16/20% chance to stun the target for 3 sec. `id 19407`
- Lethal Attacks [5] — Increases your critical strike chance with all attacks by 1/2/3/4/5%. `id 19426`

**R2**
- Improved Stings [3] — Increases the damage of your Serpent Sting ability by 6/13/20%, reduces the cooldown of your Viper Sting ability by 2/4/6 sec, and increases the duration of your Scorpid Sting ability by 15/30/45 sec. `id 1310661`
- Efficiency [5] — Reduces the Mana cost of your Shots, Stings, and melee abilities by 3/6/9/12/15%. `id 19416`
- Careful Aim [5] — Increases your Attack Power by 20/40/60/80/100% of your Intellect. `id 1223984`

**R3**
- Rapid Killing [2] — Reduces the cooldown on your Rapid Fire ability by 1/2 min. In addition, when you kill a non-trivial enemy or it dies while afflicted by your Serpent Sting, you gain Rapid Killing, increasing the damage of your next Shot ability within 20 sec by 10/20%. `id 415405`
- Improved Arcane Shot [5] — Reduces the cooldown of your Arcane Shot by 0.3/0.6/0.9/1.2/1.5 sec. Does not affect the cooldown of abilities which share a cooldown with Arcane Shot. `id 19454`
- Lone Wolf [1] — You deal 20% increased damage with all attacks while you do not have an active pet. `id 415370`

**R4**
- Trueshot Aura [1] — 180 mana. Increases the Ranged Attack Power of party or raid members within 45 yds by 20. `id 1299346`
- Mortal Shots [5] — Increases the critical strike damage bonus on all ranged abilities by 6/12/18/24/30%. *(requires Careful Aim)* `id 19485`

**R5**
- Rapid Recuperation [2] — Afflicting a target with Serpent Sting allows 25/50% of your Mana Regeneration to continue while casting for 15 sec, increased to 50/100% when Rapid Killing is consumed. *(requires Rapid Killing)* `id 1223987`
- Barrage [3] — Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 5/10/15%. `id 19461`
- Scatter Shot [1] — 8% of base mana, 15 yd, -1000 sec cast, 30 sec CD. A short-range shot that deals 50% weapon damage and disorients the target for 4 sec. Any damage caused will remove the effect. Turns off your attack when used. `id 19503`

**R6**
- Ranged Weapon Specialization [5] — Increases the damage you deal with ranged weapons by 1/2/3/4/5%. `id 19507`

**R7**
- Sniper Shot [1] — 365 mana, 45 yd, 4 sec cast, 15 sec CD. A long-range shot that deals ranged damage plus 320 and increases the range of your next 3 Shots by 10 yards for 10 sec. *(requires Trueshot Aura)* `id 1310687`

**R9**
- Improved Serpent Sting [5] — Increases the damage done by your Serpent Sting by 2/4/6/8/10%. `id 19464`

### Survival — datamined (19 talents, 57 points)

**R1**
- Improved Tracking [5] — While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 1/2/3/4/5%. `id 24293`
- Deflection [5] — Increases your Parry chance by 1/2/3/4/5%. `id 19295`

**R2**
- Entrapment [5] — When your traps are triggered, all affected targets are Entrapped, preventing them from moving for 1/2/3/4/5 sec. `id 19184`
- Savage Strikes [2] — Increases the critical strike chance of all your melee abilities by 2/4%. `id 19159`
- Survivalist [5] — Increases your total Health by 2/4/6/8/10%. `id 19255`
- Improved Wing Clip [3] — Gives your Wing Clip ability a 7/13/20% chance to immobilize the target for 5 sec. `id 19228`

**R3**
- Clever Traps [2] — Increases the duration of Freezing and Frost trap effects by 15/30% and the damage of Immolation and Explosive trap effects by 15/30%. `id 19239`
- Surefooted [3] — Increases your hit chance by 1/2/3% and reduces the duration of movement impairing effects on you by 10/20/30%. `id 19290`
- Deterrence [1] — 5 min CD. When activated, increases your Dodge and Parry chance by 25% for 10 sec. `id 19263`

**R4**
- Survival Tactics [2] — Increases your chance to hit with your Trap and Feign Death abilities by 5/10%. `id 19376`
- Predator's Edge [5] — Increases your melee ability critical strike damage by 6/12/18/24/30% and your Off Hand weapon damage by 10/20/30/40/50%. `id 1310627`
- Counterattack [1] — 30 mana, 5 yd, 5 sec CD. A strike that becomes active after parrying an opponent's attack. This attack deals 50% weapon damage plus 26 and immobilizes the target for 5 sec. Counterattack cannot be blocked, dodged, or parried. *(requires Deterrence)* `id 19306`

**R5**
- Resourcefulness [2] — Reduces the Mana cost of your Trap and melee abilities by 30/60%, and grants your melee and ranged ability Critical Strikes a 50/100% chance to allow 50% of your Mana Regeneration to continue while casting for 30 sec. `id 440529`
- Expose Prey [2] — Grants your melee and ranged attacks against enemies afflicted by Hunter's Mark a 5/10% chance to allow an activation of Mongoose Bite. Lasts 10 sec. `id 1310532`
- Survivalist's Discipline [2] — Reduces the cooldown of your Trap and Deterrence abilities by 20/40%. `id 1310496`
- Strider Kick [1] — 5.81% of base mana, 5 yd, 8 sec CD. A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. `id 1317257`

**R6**
- Lightning Reflexes [5] — Increases your Agility by 3/6/9/12/15%. `id 19168`

**R7**
- Lacerating Strikes [1] — Your Mongoose Bite also causes the target to Bleed for damage equal to 40% of the damage done by Mongoose Bite over 21 sec *(requires Expose Prey)* `id 1310533`

**R8**
- Lightning Reflexes [5] — Increases your Agility by 3/6/9/12/15%. `id 19168`

<!-- /overrides -->

## Beast Mastery (16 talents)

**R1**
- Deadly Aspects [5] — While Aspect of the Hawk is active, Auto Shot has a 2% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 2% chance of increasing melee attack speed by 30% for 12 sec.
- Endurance Training [5] — Increases the Health and Armor of your pets by 3%.

**R2**
- Focused Fire [2] — Increases all damage you and your pet deal by 1% while your pet is active.
- Improved Aspect of the Monkey [3] — Increases the Dodge bonus of your Aspect of the Monkey by 2%. Additionally, your pet gains 50% of the effect of your Aspect of the Monkey ability.
- Pathfinding [2] — Increases the speed bonus of your Aspect of the Cheetah and Aspect of the Pack by 3%.
- Improved Revive Pet [2] — Revive Pet's casting time is reduced by 3 sec, mana cost is reduced by 20%, and increases the health your pet returns with by an additional 15%.

**R3**
- Bestial Swiftness [1] — Increases the movement speed of your pets by 30%.
- Unleashed Fury [5] — Increases the damage done by your pets and hawks by 3%.

**R4**
- Improved Mend Pet [2] — Gives your Mend Pet spell a 15% chance of cleansing 1 Curse, Disease, Magic, or Poison effect from your pet each time it heals and reduces the Mana cost by 10%.
- Ferocity [5] — Increases the critical strike chance of your pets and hawks by 2%.
- Summon Hawk [1] — 80 Mana | 35 yd range | Instant | 6 sec cooldown | Command a hawk to dive-bomb your targeted enemy, dealing 32 plus 5% of your Ranged Attack Power Physical damage and continuing its assault for 18 sec. Only 2 hawks can be active at once. Summon Hawk shares its cooldown with Arcane Shot.

**R5**
- Spirit Bond [2] — While your pet is active, you and your pet will regenerate 1% of total health every 10 sec.
- Intimidation [1] — 8% of base mana | 100 yd range | Instant | 1 min cooldown | Command your pet to Stun the target for 3 sec on its next successful attack, which also gains 100% increased critical strike chance. Generates high threat.
- Bestial Discipline [2] — Increases the Focus regeneration of your pets by 10% and allows 25% of your Mana regeneration to continue while casting.

**R6**
- Frenzy [5] — Gives your pet a 20% chance to gain a 30% attack speed increase for 8 sec after dealing a critical strike.

**R7**
- Bestial Wrath [1] — 12% of base mana | 100 yd range | Instant | 2 min cooldown | Send your pet into a rage causing 50% additional damage for 18 sec. While enraged, the beast does not feel pity or remorse or fear and it cannot be stopped unless killed.

## Marksmanship (17 talents)

**R1**
- Hawk Eye [3] — Increases the range of your ranged weapons by 2 yards.
- Improved Concussive Shot [5] — Gives your Concussive Shot a 4% chance to stun the target for 3 sec.
- Lethal Attacks [5] — Increases your critical strike chance with all attacks by 1%.

**R2**
- Improved Stings [3] — Increases the damage of your Serpent Sting ability by 6%, reduces the cooldown of your Viper Sting ability by 2 sec, and increases the duration of your Scorpid Sting ability by 15 sec.
- Efficiency [5] — Reduces the Mana cost of your Shots, Stings, and melee abilities by 3%.
- Careful Aim [5] — Increases your Attack Power by 20% of your Intellect.

**R3**
- Rapid Killing [2] — Reduces the cooldown on your Rapid Fire ability by 1 min. In addition, when you kill a non-trivial enemy or it dies while afflicted by your Serpent Sting, you gain Rapid Killing, increasing the damage of your next Shot ability within 20 sec by 10%.
- Improved Arcane Shot [5] — Reduces the cooldown of your Arcane Shot by 0.3 sec. Does not affect the cooldown of abilities which share a cooldown with Arcane Shot.
- Lone Wolf [1] — You deal 20% increased damage with all attacks while you do not have an active pet.

**R4**
- Trueshot Aura [1] — 180 Mana | Instant | Increases the Ranged Attack Power of party or raid members within 45 yds by 30.
- Mortal Shots [5] — Increases the critical strike damage bonus on all ranged abilities by 6%.
- Improved Serpent Sting [5] — Increases the damage done by your Serpent Sting by 2%.

**R5**
- Rapid Recuperation [2] — Afflicting a target with Serpent Sting allows 25% of your Mana Regeneration to continue while casting for 15 sec, increased to 50% when Rapid Killing is consumed.
- Barrage [3] — Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 3%.
- Scatter Shot [1] — 8% of base mana | 15 yd range | Instant | 30 sec cooldown | A short-range shot that deals 50% weapon damage and disorients the target for 4 sec. Any damage caused will remove the effect. Turns off your attack when used.

**R6**
- Ranged Weapon Specialization [5] — Increases the damage you deal with ranged weapons by 1%.

**R7**
- Sniper Shot [1] — 365 Mana | 8-45 yd range | 4 sec cast | 15 sec cooldown | A long-range shot that deals ranged damage plus 160 and increases the range of your next 3 Shots by 10 yards for 10 sec.

## Survival (18 talents)

**R1**
- Improved Tracking [5] — While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 1%.
- Deflection [5] — Increases your Parry chance by 1%.

**R2**
- Entrapment [5] — When your traps are triggered, all affected targets are Entrapped, preventing them from moving for 1 sec.
- Savage Strikes [2] — Increases the critical strike chance of all your melee abilities by 2%.
- Survivalist [5] — Increases your total Health by 2%.
- Improved Wing Clip [3] — Gives your Wing Clip ability a 7% chance to immobilize the target for 5 sec.

**R3**
- Clever Traps [2] — Increases the duration of Freezing and Frost trap effects by 15% and the damage of Immolation and Explosive trap effects by 15%.
- Surefooted [3] — Increases your hit chance by 1% and reduces the duration of movement impairing effects on you by 10%.
- Deterrence [1] — Instant | 5 min cooldown | When activated, increases your Dodge and Parry chance by 25% for 10 sec.

**R4**
- Survival Tactics [2] — Increases your chance to hit with your Trap and Feign Death abilities by 5%.
- Predator's Edge [5] — Increases your melee ability critical strike damage by 6% and your Off Hand weapon damage by 10%.
- Counterattack [1] — 30 Mana | Melee Range | Instant | 5 sec cooldown | A strike that becomes active after parrying an opponent's attack. This attack deals 50% weapon damage plus 13 and immobilizes the target for 5 sec. Counterattack cannot be blocked, dodged, or parried.

**R5**
- Resourcefulness [2] — Reduces the Mana cost of your Trap and melee abilities by 30%, and grants your melee and ranged ability Critical Strikes a 50% chance to allow 50% of your Mana Regeneration to continue while casting for 30 sec.
- Expose Prey [2] — Grants your melee and ranged attacks against enemies afflicted by Hunter's Mark a 5% chance to allow an activation of Mongoose Bite. Lasts 10 sec.
- Survivalist's Discipline [2] — Reduces the cooldown of your Trap and Deterrence abilities by 20%.
- Strider Kick [1] — 5.81% of base mana | Melee Range | Instant | 8 sec cooldown | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec.

**R6**
- Lightning Reflexes [5] — Increases your Agility by 2%.

**R7**
- Lacerating Strikes [1] — Your Mongoose Bite also causes the target to Bleed for damage equal to 40% of the damage done by Mongoose Bite over 21 sec
