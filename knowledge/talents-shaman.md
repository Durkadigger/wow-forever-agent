# WoW Forever — Shaman Talents
Data as of: 2026-11-07 b:1.60.1.70862 (Overrides block: datamined, tier 2). Generated lines below the block: 2026-10-27 b:beta, tier 3, superseded wherever the block covers the same talent.
Source: classicwowforever.com talent calculator chunk. Rank-1 captured tooltips; higher ranks are the site's estimates. Values change with each build.
Provenance: [T3 cwf 2026-10-27 b:beta] applies to every talent line below unless an Overrides entry says otherwise. The tag date is the date this script fetched the site; the site's own capture may be earlier. Provenance tags: `[T<tier> <source-id> <date> b:<build>]`, see docs/sop-provenance.md and sources.md. Build labels in data/builds.json.

<!-- overrides -->
## Overrides (tier 1–2 values that outrank the generated lines)
*Full datamined tree, TraitTree 1082. [T2 wago 2026-11-07 b:1.60.1.70862] applies to every line in this block. Values written a/b/c are ranks 1/2/3, each read from the client's per-rank curves (TraitDefinitionEffectPoints), not extrapolated.*

### 24 Sept 2026 blue-post class changes (not talent-rank values; layered on top of the tree below)
*[T1 blizz-forum 2026-09-24] (Kaivax, WoW Forever Beta Development Notes – Updated September 24, https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-updated-september-24/2360696)*
- **Riptide can now land critical hits.** "Corrected an issue and now Riptide can land critical hits." Bug fix, not a tooltip-number change; direct heal, HoT, and the Chain Heal buff all now benefit from Resto's crit chance (Tidal Mastery, Water Shield procs, gear crit). Resto's core HoT/direct-heal hybrid.
- Lightning Bolt: damage on ranks 3 and 4 increased so those ranks are always an upgrade over the previous rank (Elemental/leveling).
- Lava Burst: ranks 1–2 base damage increased ~10% above the same-level Lightning Bolt rank (id 408490 rank-1 effect base points 113→164, confirmed by wago diff; tooltip above already reflects the new value).
- Windfury Totem and Flametongue Totem: buff names cleaned up ("Windfury Totem" / "Flametongue Totem", no more "Passive"/"Effect" suffix). Flametongue Totem no longer has a duration (replaced instantly by recasting), no longer stacks with itself, Flametongue Weapon, or Windfury Totem. Tranquil Air, Windfury, and Grace of Air Totems no longer stack with themselves even from different Shamans in the same group. Affects Resto's totem choices in group content (no more layering Flametongue Totem under Windfury Totem for extra effect).
- Elemental: Elemental Fury (Row 3) and Elemental Alacrity (Row 6) swapped rows — see the tree below, already updated. Devs' note: this affects Enhancement's spell crit damage (previously fed by the row-3 Elemental Fury), with more Enhancement changes promised in a future build.
- Enhancement: Rage of the Far Seer (R7) no longer increases spell casting speed, only attack speed — see the tree below, already updated.
- Not mentioned in this post: Water Shield, Healing Way, Chain Heal, Mana Tide Totem, Berserking, Blood Fury — no changes found in the 24 Sept notes or the wago diff for these.

### 1–27 Oct 2026 blue-post class changes, checked against b:1.60.1.70634 (not talent-rank values; layered on the tree below)
*[T1 blizz-forum 2026-10-16] unless a line carries its own tag. Source: Kaivax, WoW Forever Beta Development Notes (topic 2360696): posts of 1 Oct [T1 blizz-forum 2026-10-01], 8 Oct [T1 blizz-forum 2026-10-08] and 16 Oct. Where the 27 Oct datamine shows the same change the line also carries [T2 wago 2026-10-27 b:1.60.1.70634]. These notes supersede the 24 Sept block above wherever they overlap. Class deep-dive articles of 30 Sept to 15 Oct (blizz-news 24301515, 24301514, 24302097, 24310968, 24302099) describe the same beta changes and were not stored line by line.*
- **Restoration, Water Shield:** can now trigger from any critical spell cast by the Shaman (was only critical heals) [T1 blizz-forum 2026-10-16; T2 wago 2026-10-27 b:1.60.1.70634]. The 15 sec cooldown shown in the tooltip is gone; it never had one [T1 blizz-forum 2026-10-08]; cooldown row 15000 → 0 [T2 wago 2026-10-27 b:1.60.1.70634]. Still 3 globes (ProcCharges 3) at 2% of max mana each with a 3.5 sec gap between globes [T2 wago 2026-10-27 b:1.60.1.70634]. The aura tooltip text now prints "1 charges" because it reads a new effect row; the spell description still says 3 globes. Unexplained, flagged [T2 wago 2026-10-27 b:1.60.1.70634].
- **Restoration, Mana Tide Totem:** an extra rank is learned at level 38, so ranks come at 25, 38, 48 and 58 (was 25, 48, 58) [T1 blizz-forum 2026-10-16]. Datamined: four ranks restoring 88 / 133 / 197 / 290 mana every 3 sec for 12 sec to group members within 30 yd, 5 min CD [T2 wago 2026-10-27 b:1.60.1.70634]. The Water Shield display fix and the restored Mana Tide pulse visual are cosmetic [T1 blizz-forum 2026-10-08].
- **Restoration, talent rows:** Tidal Focus and Totemic Focus swapped. Tidal Focus is now row 1, Totemic Focus row 2 [T1 blizz-forum 2026-10-16; T2 wago 2026-10-27 b:1.60.1.70634]. Restorative Totems now raises the entire Healing Stream Totem effect (was the base value only) [T1 blizz-forum 2026-10-16]; the talent's effect row changed 8 → 22 [T2 wago 2026-10-27 b:1.60.1.70634].
- **Restoration, wording only:** Healing Focus and Eye of the Storm now read "chance to not lose casting time when you take damage" with the same 23 / 47 / 70% numbers (was "avoid interruption" / "reduces pushback") [T2 wago 2026-10-27 b:1.60.1.70634]. No number changed; whether the mechanic changed is not stated.
- **Restoration, unchanged in b:1.60.1.70634 (Riptide changed in b:1.60.1.70790, see the 2 Nov block below):** Riptide (rank 1: 245 mana, 6 sec CD, 484–535 plus 445 over 15 sec at level 60 with 0 spell power, +25% to Chain Heal on that target; the 24 Sept crit fix stands) and Earth Shield (rank 1 of the talent version 5% of base mana, 9 charges, heals 28 per charge before healing power, 30% less casting time lost) [T2 wago 2026-10-27 b:1.60.1.70634]. Chain Heal only got a green tint to its visual [T1 blizz-forum 2026-10-16].
- **Totems (all specs):** Grace of Air, Strength of Earth, Windfury and Flametongue Totems are now raid-wide; Grace of Air is no longer exclusive with Windfury and Flametongue (those two stay exclusive with each other); Flametongue and Windfury now affect players only [T1 blizz-forum 2026-10-16]. The Windfury Totem effect rows changed type in the datamine [T2 wago 2026-10-27 b:1.60.1.70634].
- **Elemental:** Lava Burst moved from row 7 to row 5 as the 21-point talent, rank 4 added, no prerequisite; rank 1 is now 135 mana (was 165) and 113–146 Fire damage (was 150–193) [T1 blizz-forum 2026-10-16; T2 wago 2026-10-27 b:1.60.1.70634]. Elemental Mastery returned as the 31-point talent: 3 min CD, Lightning Bolt and Lava Burst cast 0.5 sec faster and Chain Lightning loses its cooldown for 15 sec, Lava Burst is the prerequisite [T1 blizz-forum 2026-10-16; T2 wago 2026-10-27 b:1.60.1.70634]. Call of Thunder removed; Elemental Alacrity moved to row 2 and Elemental Warding to row 3; Lightning Overload requires Elemental Alacrity and Elemental Fury requires Lightning Overload; Earthbound is the row-4 16-point talent [T1 blizz-forum 2026-10-16; T2 wago 2026-10-27 b:1.60.1.70634]. Elemental Reach also cuts the Totemic Projection cooldown 10 / 20 sec; Call of Flame also extends Flame Shock 3 / 6 / 9 sec; Improved Fire Nova is now Trial by Fire (and also lengthens Magma Totem 10 / 20 sec) [T2 wago 2026-10-27 b:1.60.1.70634]. Chain Lightning mana cost down about 35% on all four ranks (rank 4 485 → 315) [T1 blizz-forum 2026-10-16; T2 wago 2026-10-27 b:1.60.1.70634]. Fire Nova spell power coefficient 0.143 (was 0.214) with much lower base damage and mana cost [T1 blizz-forum 2026-10-16].
- **Enhancement:** Stormstrike costs 8% of base mana (was a flat 125) [T1 blizz-forum 2026-10-16; T2 wago 2026-10-27 b:1.60.1.70634]. Stormstrike's debuff is no longer consumed by a spell that misses or by other players [T1 blizz-forum 2026-10-16].
- **Not found in any post or in the datamine:** a change to Earth Shield, Riptide, Nature's Swiftness, Healing Way, Purification or Mindfulness numbers between b:1.60.1.70009 and b:1.60.1.70634 [T2 wago 2026-10-27 b:1.60.1.70634].

### 2 Nov 2026 development notes, checked against b:1.60.1.70790 (launch client; supersedes the 1-27 Oct block above wherever they overlap)
*[T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] unless a line carries its own tag. Source: Kaivax, WoW Forever Beta Development Notes, updated 2 Nov (topic 2360696, post 9, https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9). Blizzard's developer note: damage was raised on classes across the game and higher-level creature health raised to compensate; no big tuning changes are planned before the raids open on 9 Dec.*
- **Restoration, Riptide:** no initial heal any more, healing over time only; mana cost down about 40%; cooldown 12 sec. Rank 1 now 150 mana, 12 sec CD, 445 over 15 sec at level 60 with 0 spell power, spell power coefficient 0.1, still +25% to Chain Heal on that target; the other two ranks cost 180 and 230 mana (spell ids 1239242 and 1239243, which carry the same changes) [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] (was: rank 1 245 mana, 6 sec CD, 484-535 direct plus 445 over 15 sec, coefficients 0.214 / 0.1 [T2 wago 2026-10-27 b:1.60.1.70634]). The 24 Sept crit fix still applies to the HoT.
- **Restoration, unchanged in b:1.60.1.70790:** Water Shield (still 2% of max mana per globe, 3 globes; the aura tooltip still prints "1 charges", so that oddity is still unexplained), Mana Tide Totem (ranks 88 / 133 / 197 / 290), Chain Heal, Healing Wave and the Restoration talent ranks show no change in the diff [T2 wago 2026-11-04 b:1.60.1.70790]. No post names them [T1 blizz-forum 2026-11-03].
- **Totems:** Totemic Projection renamed **Totemic Call**; it teleports your totems to your own location and its cooldown is 30 sec [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] (was: 60 sec, relocates to a specified location [T2 wago 2026-10-27 b:1.60.1.70634]). Elemental Reach no longer reduces its cooldown. Windfury Weapon and Windfury Totem now animate an additional weapon swing attack [T1 blizz-forum 2026-11-03] (an animation change; the spell tables show no number change).
- **Elemental:** Lava Burst is removed from the talent tree and "all references to Lava Burst removed" (Convection, Elemental Alacrity, Call of Flame, Eye of the Storm and Elemental Reach no longer list it); **Call of Thunder** is back as a 1-point talent: +5% critical strike chance on Lightning Bolt and Chain Lightning. **Elemental Mastery is renamed Lightning Mastery** (3 min CD, Lightning Bolt cast 0.5 sec faster, Chain Lightning loses its cooldown, 15 sec; requires Call of Thunder) [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] (was: Elemental Mastery and Lava Burst in the tree [T2 wago 2026-10-27 b:1.60.1.70634]). Lightning Overload is 10 / 20 / 30% (was 3 / 7 / 10%).
- **Lightning Bolt and Chain Lightning:** Lightning Bolt base damage up on every rank (EffectBasePointsF rank 1 15 to 16, rank 10 196 to 353). Chain Lightning cast time is now 2.5 sec; mana cost now 245 / 360 / 425 / 495 for ranks 1-4 (was 145 / 200 / 250 / 315); rank 4 primary-target base 510 (was 123) [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03].
- **Shocks:** Earth, Flame and Frost Shock base damage reverted toward Classic Era values, e.g. Earth Shock rank 1 20 (was 18), rank 7 531 (was 301); Flame Shock rank 6 292 / 80 (was 166 / 44) [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03].
- **Enhancement:** Stormstrike now 150% weapon damage (was normal weapon damage) with a 6 sec cooldown (was 8). Mental Dexterity is 50 / 100 / 150% of Intellect (was 33 / 67 / 100%). Flurry is 6 / 12 / 18 / 24 / 30% (was 5 / 10 / 15 / 20 / 25%). Improved Ghost Wolf moved to row 4. Maelstrom Weapon trigger chance doubled [T1 blizz-forum 2026-11-03] (a proc rate; not seen in the spell tables).
- **Dual Wield:** spell 674 still has its SkillLineAbility row on the Shaman skill line, as in b:1.60.1.70634, but no talent, trigger or level grant was found and no trainer has been seen offering it; treat Shaman dual wield as unavailable until confirmed in game (unconfirmed; drill 02 finding F1, 7 Nov 2026). The new passive spell 1300344 "Dual Wield" (Off Hand weapons in the Off Hand) is not granted to any class by a SkillLineAbility row, a talent definition or another spell's trigger in b:1.60.1.70790, and was equally unreferenced in b:1.60.1.70634 [T2 wago 2026-11-04 b:1.60.1.70790].

### 6 Nov 2026 post-launch notice (announcement; hotfix due Tue 10 Nov)
*[T1 blizz-forum 2026-11-06] Kaivax, "Class Tuning Incoming - November 10", https://us.forums.blizzard.com/en/wow/t/class-tuning-incoming-november-10/2404092/1. Current values in the tree below stay until the hotfix lands; the hotfix is server-side, so check it in game or in the 10 Nov hotfix notes.*
- **Enhancement stat priority.** Current: Intellect and Spell Power are stronger than Strength and Attack Power for Enhancement (Blizzard's statement of live behaviour) [T1 blizz-forum 2026-11-06]. Announced: changes so that Strength is always Enhancement's strongest stat and its best items carry Strength or Attack Power with some Intellect or Spell Power; Blizzard tells levelling Enhancement Shamans to collect Strength and Attack Power gear from now on [T1 blizz-forum 2026-11-06]. The post does not say which numbers change (Mental Dexterity, Intellect scaling or Strength scaling).

### Elemental — datamined (16 talents, 46 points)

**R1**
- Convection [5] — Reduces the mana cost of your Shock, Lightning Bolt, and Chain Lightning spells by 2/4/6/8/10%. `id 16039`
- Concussion [5] — Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 1/2/3/4/5%. `id 16035`

**R2**
- Elemental Devastation [3] — Your Critical Strikes with direct damage spells increase your chance to get a Critical Strike with melee attacks by 3/6/9% for 10 sec. `id 30160`
- Reverberation [5] — Reduces the cooldown of your Shock spells by 0.2/0.4/0.6/0.8/1.0 sec. `id 16040`
- Elemental Alacrity [3] — Reduces the cast time of your Lightning Bolt and Chain Lightning spells by 0.17/0.33/0.50 sec. `id 16578`
- Call of Flame [3] — Increases the damage done by your Fire Totems and by your Flame Shock and Fire Nova spells by 5/10/15%, as well as increases the duration of your Flame Shock spell by 3/6/9 sec. `id 16038`

**R3**
- Elemental Focus [1] — Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. `id 16164`
- Elemental Warding [3] — Reduces damage taken from Fire, Frost, and Nature effects by 3/7/10%. `id 28996`

**R4**
- Trial by Fire [2] — Increases the damage done by your Fire Nova spell by 10/20% and reduces its cooldown by 2/4 sec, and increases the duration of your Magma Totem by 10/20 sec. `id 16086`
- Eye of the Storm [3] — Gives your Lightning Bolt and Chain Lightning spells a 23/47/70% chance to not lose casting time when you take damage. `id 29062`
- Earthbound [1] — Your Earthbind Totem Immobilizes nearby targets for 5 sec when cast. `id 1222988`

**R5**
- Elemental Reach [2] — Increases the range of your Lightning Bolt, Chain Lightning, and Fire Nova spells by 3/6 yards. `id 28999`
- Call of Thunder [1] — Increases the critical strike chance of your Lightning Bolt and Chain Lightning spells by 5%. `id 16120`
- Lightning Overload [3] — Gives your Lightning Bolt and Chain Lightning spells a 10/20/30% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat. *(requires Elemental Alacrity)* `id 408438`

**R6**
- Elemental Fury [5] — Increases the critical strike damage bonus of your Searing and Magma Totems and your Fire, Frost, and Nature spells by 20/40/60/80/100%. *(requires Lightning Overload)* `id 16089`

**R7**
- Lightning Mastery [1] — 3 min CD. Gain mastery over Lightning, reducing the cast time of your Lightning Bolt spell by 0.5 sec, and removing the cooldown from your Chain Lightning spell. Lasts 15 sec. *(requires Call of Thunder)* `id 16166`

### Enhancement — datamined (18 talents, 51 points)

**R1**
- Earth's Grasp [2] — Increases the health of your Stoneclaw Totem by 25/50% and the radius of your Earthbind Totem by 10/20%. `id 16043`
- Thundering Strikes [5] — Improves your chance to get a critical strike with all spells and attacks by 1/2/3/4/5%. `id 16255`
- Ancestral Knowledge [5] — Increases your Intellect by 2/4/6/8/10%. `id 17485`

**R2**
- Guardian Totems [2] — Increases the amount of damage reduced by your Stoneskin Totem and Windwall Totem by 10/20% and reduces the cooldown of your Grounding Totem by 1/2 sec. `id 16258`
- Mental Dexterity [3] — Increases your Attack Power by an amount equal to 50/100/150% of your Intellect. `id 415140`
- Improved Lightning Shield [3] — Increases the damage done by your Lightning Shield orbs by 5/10/15%. `id 16261`

**R3**
- Elemental Weapons [3] — Increases the melee attack power bonus of your Rockbiter Weapon by 7/13/20%, your Windfury Weapon effect by 13/27/40% and increases the damage caused by your Flametongue Weapon and Frostbrand Weapon by 5/10/15%. `id 16266`
- Shamanistic Focus [1] — Reduces the mana cost of your Shock and Lightning Shield spells by 45%. `id 1223030`
- Anticipation [3] — Increases your chance to dodge by an additional 2/4/6%. `id 16254`

**R4**
- Toughness [5] — Increases your Stamina by 2/4/6/8/10%. `id 16252`
- Flurry [5] — Increases your attack speed by 6/12/18/24/30% for your next 3 swings after dealing a melee critical strike. *(requires Mental Dexterity)* `id 16256`
- Stormstrike [1] — 8% of base mana, 5 yd, 6 sec CD. Instantly strike for 150% weapon damage and increase the damage you deal to the target with your next Lightning Bolt, Chain Lightning, or Earth Shock spell by 20% for 12 sec. `id 17364`
- Improved Ghost Wolf [2] — Reduces the cast time of your Ghost Wolf spell by 1.0/3.0 sec, and Ghost Wolf may be used indoors. `id 16262`

**R5**
- Spirit Weapons [1] — Gives a chance to parry enemy melee attacks, reduces all threat generated by your attacks by 30% while Rockbiter Weapon is not active, and increases all threat generated by 30% while Rockbiter Weapon is active. `id 16268`
- Mental Quickness [2] — Increases your spell damage and healing by up to 15/30% of your Intellect. `id 30812`
- Improved Stormstrike [2] — When you Stormstrike, you have a 50/100% chance to gain 50% mana regeneration while casting spells for 15 sec, and Stormstrike's cooldown has a 50/100% chance to reset each time you Dodge or Parry. *(requires Stormstrike)* `id 1223031`

**R6**
- Maelstrom Weapon [5] — When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 4/8/12/16/20%. Stacks up to 5 times. Lasts 30 sec. `id 408498`

**R7**
- Rage of the Farseer [1] — 3 min CD. Increases your attack speed by 30% for 25 sec. *(requires Mental Quickness)* `id 425336`

### Restoration — datamined (16 talents, 51 points)

**R1**
- Improved Healing Wave [5] — Reduces the casting time of your Healing Wave spell by 0.1/0.2/0.3/0.4/0.5 sec. `id 16182`
- Tidal Focus [5] — Reduces the Mana cost of your healing spells by 1/2/3/4/5% and improves your chance to hit by 1/2/3/4/5%. `id 16179`

**R2**
- Mindfulness [3] — Allows 17/33/50% of your Mana regeneration to continue while casting. `id 1223033`
- Natural Grace [3] — Reduces the threat generated by your spells by 5/10/15%. `id 29187`
- Totemic Focus [5] — Reduces the Mana cost of your totems and any spells that summon or move them by 5/10/15/20/25%. `id 16173`
- Improved Reincarnation [2] — Reduces the cooldown of your Reincarnation spell by 10/20 min, increases your maximum health by 2/4%, and increases the amount of health and Mana you reincarnate with by an additional 10/20%. `id 16184`

**R3**
- Ancestral Healing [3] — Increases your target's armor value by 8/17/25% for 15 sec after getting a critical effect from one of your healing spells. `id 16176`
- Healing Focus [3] — Gives your healing spells a 23/47/70% chance to not lose casting time when you take damage. `id 16181`
- Water Shield [1] — The caster is surrounded by 3 globes of water. When a spell, melee, or ranged attack hits the caster or when one of the caster's spells gets a critical result, 2% of maximum mana is restored to the caster, expending one water globe. Only one globe will activate every few seconds. Lasts 10 min. Only one Elemental Shield can be active on the Shaman at any one time. `id 408510`

**R4**
- Tidal Mastery [5] — Increases the critical effect chance of your healing spells by 1/2/3/4/5%. `id 16194`
- Restorative Totems [5] — Increases the effect of your Mana Spring Totem by 5/10/15/20/25% and increases the effect of your Healing Stream Totem by 10/20/30/40/50%. `id 16187`
- Mana Tide Totem [1] — 10 mana, 5 min CD. Summons a Mana Tide Totem with 5 health at the feet of the caster for 12 sec that restores 88 mana every 3 seconds to group members within 30 yards. `id 16190`

**R5**
- Healing Way [3] — Increases the amount healed by your Healing Wave spell by 8/17/25%. `id 29206`
- Nature's Swiftness [1] — 3 min CD. When activated, your next Nature spell with a casting time less than 10 sec. becomes an instant cast spell. `id 16188`

**R6**
- Purification [5] — Increases the effectiveness of your healing spells by 2/4/6/8/10%. `id 16178`

**R7**
- Riptide [1] — 150 mana, 40 yd, 12 sec CD, spell power coeff 0.1; numbers are level 60 with 0 spell power. Heals a friendly target for 445 over 15 sec, and increases the effectiveness of your Chain Heal casts directly on that target by 25%. *(requires Healing Way)* `id 408521`

<!-- /overrides -->

## Elemental Combat (16 talents)

**R1**
- Convection [5] — Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 2%.
- Concussion [5] — Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 1%.

**R2**
- Elemental Devastation [3] — Your Critical Strikes with direct damage spells increase your chance to get a Critical Strike with melee attacks by 3% for 10 sec.
- Reverberation [5] — Reduces the cooldown of your Shock spells by 0.2 sec.
- Elemental Alacrity [3] — Reduces the cast time of your Lightning Bolt, Chain Lightning, and Lava Burst spells by 0.17 sec.
- Call of Flame [3] — Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 5%, as well as increases the duration of your Flame Shock spell by 3 sec.

**R3**
- Elemental Focus [1] — Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%.
- Elemental Warding [3] — Reduces damage taken from Fire, Frost, and Nature effects by 3%.

**R4**
- Trial by Fire [2] — Increases the damage done by your Fire Nova spell by 10% and reduces its cooldown by 2 sec, and increases the duration of your Magma Totem by 10 sec.
- Eye of the Storm [3] — Reduces the pushback suffered from damaging attacks while casting Lightning Bolt, Chain Lightning, and Lava Burst by 23%.
- Earthbound [1] — Your Earthbind Totem Immobilizes nearby targets for 5 sec when cast.

**R5**
- Elemental Reach [2] — Increases the range of your Lightning Bolt, Chain Lightning, Fire Nova, and Lava Burst spells by 3 yards and reduces the cooldown of Totemic Projection by 10 sec.
- Lava Burst [1] — 135 Mana | 30 yd range | 2.5 sec cast | 10 sec cooldown | You hurl molten lava at the target, dealing 114 to 145 Fire damage. If your Flame Shock is on the target, Lava Burst deals 20% increased damage.
- Lightning Overload [3] — Gives your Lightning Bolt and Chain Lightning spells a 3% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat.

**R6**
- Elemental Fury [5] — Increases the critical strike damage bonus of your Searing and Magma Totems and your Fire, Frost, and Nature spells by 20%.

**R7**
- Elemental Mastery [1] — Instant | 3 min cooldown | Gain mastery over Fire and Lightning, reducing the cast time of Lightning Bolt and Lava Burst by 0.5 sec, and removing the cooldown from Chain Lightning. Lasts 15 sec.

## Enhancement (18 talents)

**R1**
- Earth's Grasp [2] — Increases the health of your Stoneclaw Totem by 25% and the radius of your Earthbind Totem by 10%.
- Thundering Strikes [5] — Improves your chance to get a critical strike with all spells and attacks by 1%.
- Ancestral Knowledge [5] — Increases your Intellect by 2%.

**R2**
- Guardian Totems [2] — Increases the amount of damage reduced by your Stoneskin Totem and Windwall Totem by 10% and reduces the cooldown of your Grounding Totem by 1 sec.
- Mental Dexterity [3] — Increases your Attack Power by an amount equal to 33% of your Intellect.
- Improved Ghost Wolf [2] — Reduces the cast time of your Ghost Wolf spell by 1 sec, and Ghost Wolf may be used indoors.
- Improved Lightning Shield [3] — Increases the damage done by your Lightning Shield orbs by 5%.

**R3**
- Elemental Weapons [3] — Increases the melee attack power bonus of your Rockbiter Weapon by 7%, your Windfury Weapon effect by 13% and increases the damage caused by your Flametongue Weapon and Frostbrand Weapon by 5%.
- Shamanistic Focus [1] — Reduces the mana cost of your Shock and Lightning Shield spells by 45%.
- Anticipation [3] — Increases your chance to dodge by an additional 2%.

**R4**
- Toughness [5] — Increases your Stamina by 2%.
- Flurry [5] — Increases your attack speed by 5% for your next 3 swings after dealing a melee critical strike.
- Stormstrike [1] — 8% of base mana | Melee Range | Instant | 8 sec cooldown | Instantly strike for normal weapon damage and increase the damage you deal to the target with your next Lightning Bolt, Chain Lightning, or Earth Shock spell by 20% for 12 sec.

**R5**
- Spirit Weapons [1] — Gives a chance to parry enemy melee attacks, reduces all threat generated by your attacks by 30% while Rockbiter Weapon is not active, and increases all threat generated by 30% while Rockbiter Weapon is active.
- Mental Quickness [2] — Increases your spell damage and healing by up to 15% of your Intellect.
- Improved Stormstrike [2] — When you Stormstrike, you have a 50% chance to gain 50% mana regeneration while casting spells for 15 sec, and Stormstrike's cooldown has a 50% chance to reset each time you Dodge or Parry.

**R6**
- Maelstrom Weapon [5] — When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 4%. Stacks up to 5 times. Lasts 30 sec.

**R7**
- Rage of the Farseer [1] — Instant | 3 min cooldown | Increases your attack speed by 30% for 25 sec.

## Restoration (16 talents)

**R1**
- Improved Healing Wave [5] — Reduces the casting time of your Healing Wave spell by 0.1 sec.
- Tidal Focus [5] — Reduces the Mana cost of your healing spells by 1% and improves your chance to hit by 1%.

**R2**
- Mindfulness [3] — Allows 17% of your Mana regeneration to continue while casting.
- Natural Grace [3] — Reduces the threat generated by your spells by 5%.
- Totemic Focus [5] — Reduces the Mana cost of your totems and any spells that summon or move them by 5%.
- Improved Reincarnation [2] — Reduces the cooldown of your Reincarnation spell by 10 min, increases your maximum health by 2%, and increases the amount of health and Mana you reincarnate with by an additional 10%.

**R3**
- Ancestral Healing [3] — Increases your target's armor value by 8% for 15 sec after getting a critical effect from one of your healing spells.
- Healing Focus [3] — Gives you a 23% chance to avoid interruption caused by damage while casting any healing spell.
- Water Shield [1] — Instant | The caster is surrounded by 3 globes of water. When a spell, melee, or ranged attack hits the caster or when one of the caster's spells gets a critical result, 2% of maximum mana is restored to the caster, expending one water globe. Only one globe will activate every few seconds. Lasts 10 min. | Only one Elemental Shield can be active on the Shaman at any one time.

**R4**
- Tidal Mastery [5] — Increases the critical effect chance of your healing spells by 1%.
- Restorative Totems [5] — Increases the effect of your Mana Spring Totem by 5% and increases the effect of your Healing Stream Totem by 10%.
- Mana Tide Totem [1] — 10 Mana | Instant | 5 min cooldown | Tools: Water Totem | Summons a Mana Tide Totem with 5 health at the feet of the caster for 12 sec that restores 88 mana every 3 seconds to group members within 30 yards.

**R5**
- Healing Way [3] — Increases the amount healed by your Healing Wave spell by 8%.
- Nature's Swiftness [1] — Instant | 3 min cooldown | When activated, your next Nature spell with a casting time less than 10 sec. becomes an instant cast spell.

**R6**
- Purification [5] — Increases the effectiveness of your healing spells by 2%.

**R7**
- Riptide [1] — 245 Mana | 40 yd range | Instant | 6 sec cooldown | Heals a friendly target for 485 to 533, an additional 445 over 15 sec, and increases the effectiveness of your Chain Heal casts directly on that target by 25%.
