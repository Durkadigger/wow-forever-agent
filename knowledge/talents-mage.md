# WoW Forever — Mage Talents
Data as of: 2026-11-07 b:1.60.1.70862 (Overrides block: datamined, tier 2). Generated lines below the block: 2026-10-27 b:beta, tier 3, superseded wherever the block covers the same talent.
Source: classicwowforever.com talent calculator chunk. Rank-1 captured tooltips; higher ranks are the site's estimates. Values change with each build.
Provenance: [T3 cwf 2026-10-27 b:beta] applies to every talent line below unless an Overrides entry says otherwise. The tag date is the date this script fetched the site; the site's own capture may be earlier. Provenance tags: `[T<tier> <source-id> <date> b:<build>]`, see docs/sop-provenance.md and sources.md. Build labels in data/builds.json.

<!-- overrides -->
## Overrides (tier 1–2 values that outrank the generated lines)
*Full datamined tree, TraitTree 1112. [T2 wago 2026-11-07 b:1.60.1.70862] applies to every line in this block. Values written a/b/c are ranks 1/2/3, each read from the client's per-rank curves (TraitDefinitionEffectPoints), not extrapolated.*

### 24 Sept 2026 blue-post class changes (not talent-rank values)
*[T1 blizz-forum 2026-09-24] (Kaivax, WoW Forever Beta Development Notes – Updated September 24, https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-updated-september-24/2360696)*
- Arcane Missiles no longer checks line of sight on each missile, only once at channel start.
- Fire: Ignite no longer double-dips on percent damage-increase modifiers.
- Wake of Fire buff duration and Hot Streak buff duration increased (see tree below, already updated).

### 1–27 Oct 2026 blue-post class changes, checked against b:1.60.1.70634 (not talent-rank values; layered on the tree below)
*[T1 blizz-forum 2026-10-16] unless a line carries its own tag. Source: Kaivax, WoW Forever Beta Development Notes (topic 2360696): posts of 1 Oct [T1 blizz-forum 2026-10-01], 8 Oct [T1 blizz-forum 2026-10-08] and 16 Oct. Where the 27 Oct datamine shows the same change the line also carries [T2 wago 2026-10-27 b:1.60.1.70634]. These notes supersede the 24 Sept block above wherever they overlap. Class deep-dive articles of 30 Sept to 15 Oct (blizz-news 24301515, 24301514, 24302097, 24310968, 24302099) describe the same beta changes and were not stored line by line.*
- **Frost, Ice Lance:** damage against Frozen targets is a 200% increase (was 300%) [T1 blizz-forum 2026-10-16; T2 wago 2026-10-27 b:1.60.1.70634].
- **Frost, Winter's Chill redesigned:** no longer adds crit. Gives Frostbolt, Frost Blast and Fingers of Frost-empowered Ice Lance a 20 / 40 / 60 / 80 / 100% chance to apply a stack; each stack adds 5% damage taken from your next Cone of Cold and 7% of your spell damage as coefficient, up to 5 stacks, consumed by Cone of Cold [T1 blizz-forum 2026-10-16; T2 wago 2026-10-27 b:1.60.1.70634]. Application no longer rolls to resist [T1 blizz-forum 2026-10-01].
- **Frost, Cone of Cold:** the first 4 targets are slowed 10% more and for 3 sec longer [T1 blizz-forum 2026-10-16]. **Frost Warding** now also raises Ice Barrier and Frost Ward absorb 10 / 20% and gives Frost Ward a 10 / 20% chance to negate the warded damage [T2 wago 2026-10-27 b:1.60.1.70634]. **Ice Barrier** now also adds 3% Frost damage for its duration (6% total while shielded) and still prevents casting-time loss while it holds [T2 wago 2026-10-27 b:1.60.1.70634]. Frostbite and Fingers of Frost now trigger from Frost Armor and Ice Armor [T1 blizz-forum 2026-10-16]. Elemental Precision is 3 points at 2 / 4 / 6% (was 5 points at 1 to 5%) [T2 wago 2026-10-27 b:1.60.1.70634].
- **Frost Blast (new, level 24):** 1.5 sec cast, slows movement 40% for 9 sec, affected by every talent that affects Frostbolt, higher mana cost and a little more damage than rank 1 Frostbolt; its purpose is to replace down-ranking Frostbolt [T1 blizz-forum 2026-10-16]. Datamined ranks: 40 / 65 / 90 mana, 28–31 / 48–53 / 80–89 Frost damage at level 60 with 0 spell power, spell power coefficient 0.271 [T2 wago 2026-10-27 b:1.60.1.70634].
- **Down-ranking:** a rank 1 Frostbolt at level 60 has a 0% chance of Frostbite; spells far below your level get a reduced spell power benefit and a reduced chance to trigger talents [T1 blizz-forum 2026-10-01]. Frostbolt, Fireball and Arcane Missiles low ranks were retuned so every new rank is an upgrade [T1 blizz-forum 2026-10-08].
- **Arcane:** Arcane Blast redesigned (1.5 sec cast, each cast adds 15% of Intellect as spell damage for 15 sec, stacks 4, mana cost still rises, damage and coefficient down 40%); Arcane Wrath added as the 16-point talent; Missile Barrage moved to row 1 as a 2-point talent [T1 blizz-forum 2026-10-16; T2 wago 2026-10-27 b:1.60.1.70634].
- **Fire:** Heating Up (was Hot Streak) no longer needs a streak; Combustion back to 3 charges [T1 blizz-forum 2026-10-01]; Critical Mass is 5 points for 10% total; Fire Power redesigned to 3 points, 1 / 2 / 3% per Fire effect up to 12%; Wake of Fire reverted to Improved Fire Blast [T1 blizz-forum 2026-10-16; T2 wago 2026-10-27 b:1.60.1.70634].

### 2 Nov 2026 development notes, checked against b:1.60.1.70790 (launch client; supersedes the 1-27 Oct block above wherever they overlap)
*[T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] unless a line carries its own tag. Source: Kaivax, WoW Forever Beta Development Notes, updated 2 Nov (topic 2360696, post 9, https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9). Per-rank talent numbers are in the datamined tree below.*
- **Frost Blast** is removed from the game; Improved Frostbolt, Arctic Reach (now Frostbolt, Ice Lance and Blizzard range), Winter's Chill and Missile Barrage no longer name it [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03].
- **Arcane:** Arcane Focus removed (folded into Precision). Arcane Resilience moved to row 1 and is now 3 ranks, 25 / 50 / 75% of Intellect as Armor (was 2 ranks, 25 / 50%). Missile Barrage moved to row 2 and is consumed at the start of the Arcane Missiles channel. Clearcasting is not consumed by Arcane Missiles while Missile Barrage is active. **Arcane Blast:** mana cost increase per stack 100% (was 175%), 12% of Intellect as spell damage per stack (was 15%), duration 18 sec [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] (was: 175% / 15% [T2 wago 2026-10-27 b:1.60.1.70634]).
- **Fire:** Incineration is 5 ranks, +2 / 4 / 6 / 8 / 10% crit on Fire Blast, Ice Lance, Arcane Blast and Scorch (was 3 ranks, up to 6%). Improved Fireball is renamed **Accelerant** and also cuts Arcane Wrath cast time by up to 0.5 sec. Critical Mass back to 3 ranks, 2 / 4 / 6% (was 5 ranks, up to 10%). Improved Fire Blast moved to row 3 [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03].
- **Frost:** Piercing Ice removed. **Ice Lance** has an 8 sec cooldown shared with Fire Blast; damage to Frozen targets back to 300% (was 200%) [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] (was: no cooldown, 200% [T2 wago 2026-10-27 b:1.60.1.70634]). **Ice Barrier** gives +15% Frost damage for 1 min on cast and +5% more while the barrier holds (was 3% and 3%). Winter's Chill: Cone of Cold bonus 20% per stack (was 5%). Frost Warding now has a chance to fully negate a spell's damage without depleting the Frost Ward instead of reflecting. Elemental Precision is renamed **Precision**, 3 ranks, +2 / 4 / 6% hit with all spells (was Frost and Fire spells only).

### 6 Nov 2026 hotfixes
*[T1 blizz-forum 2026-11-06] (Kaivax, "WoW: Forever Hotfixes - November 6, 2026", https://us.forums.blizzard.com/en/wow/t/wow-forever-hotfixes-november-6-2026/2403040/4) unless a line carries its own tag; client build 1.60.1.70862 (7 Nov) carries the matching tooltip changes [T2 wago 2026-11-07 b:1.60.1.70862]. Builds 70840 and 70862 are the first post-launch client builds; 70840 was not snapshotted. No talent rank changed between 70790 and 70862.*
- Mages no longer learn the Research spell (it should not exist); only Study, after the relevant quest.
- Arcane Blast's duration is now correctly 18 sec.

### Arcane — datamined (18 talents, 45 points)

**R1**
- Wand Specialization [2] — Increases your damage with Wands by 13/25%. `id 6057`
- Improved Channeling [5] — Gives your Arcane Missiles spell a 20/40/60/80/100% chance and your Arcane Blast and Arcane Wrath spells a 14/28/42/56/70% chance to not lose casting time when you take damage. `id 11237`
- Arcane Resilience [3] — Increases your Armor by an amount equal to 25/50/75% of your Intellect. `id 28574`

**R2**
- Arcane Subtlety [2] — Reduces your target's resistance to all your spells by 8/15 and reduces the threat caused by your Arcane spells by 15/30%. `id 11210`
- Magic Absorption [2] — Increases all your resistances by 5/10 and causes all spells you fully resist to restore 1/2% of your total mana. Cannot trigger more often than 1 time per sec. `id 29441`
- Arcane Concentration [5] — Gives you a 2/4/6/8/10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. `id 11213`
- Missile Barrage [2] — Gives your Arcane Blast spell a 20/40% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 10/20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. `id 400588`

**R3**
- Arcane Geometry [2] — Increases the range of your Arcane spells by 3/6 yards. `id 11247`
- Arcane Impact [3] — Increases the critical strike chance of your Arcane spells by 2/4/6%. `id 11242`
- Arcane Blast [1] — 15% of base mana, 30 yd, 1.5 sec cast, spell power coeff 0.429; numbers are level 60 with 0 spell power. Blasts the target with energy, dealing 33–39 Arcane damage. Each time you cast Arcane Blast, you gain 12% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 100%. Effect stacks up to 4 times and lasts 18 sec from time of initial application. `id 400574`

**R4**
- Arcane Shielding [2] — Decreases the Mana lost per point of damage taken when your Mana Shield spell is active by 17/33% and increases the resistances granted by your Mage Armor spell by 25/50%. `id 11252`
- Improved Counterspell [2] — Your Counterspell also Silences the target for 2/4 sec. `id 11255`
- Arcane Meditation [3] — Allows 17/33/50% of your Mana regeneration to continue while casting. *(requires Arcane Concentration)* `id 18462`
- Arcane Wrath [1] — 140 mana, 30 yd, 3.5 sec cast, 6 sec CD. Launches a projectile of pure Arcane energy at the enemy target, causing 121–147 Arcane damage. This spell gains additional Spell Damage equal to 5% of your maximum Mana. *(requires Arcane Blast)* `id 1326079`

**R5**
- Presence of Mind [1] — 3 min CD. When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. `id 12043`
- Arcane Mind [5] — Increases your Intellect by 2/4/6/8/10% and increases the critical strike damage bonus of your Arcane spells by 20/40/60/80/100%. `id 11232`

**R6**
- Arcane Instability [3] — Increases the damage done by your spells by 1/2/3% and your critical strike chance by 1/2/3%. `id 15058`

**R7**
- Arcane Power [1] — 3 min CD. For the next 15 sec, your spells deal 30% more damage while costing 30% more mana to cast. *(requires Presence of Mind)* `id 12042`

### Fire — datamined (17 talents, 46 points)

**R1**
- Incineration [5] — Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 2/4/6/8/10%. `id 18459`
- Accelerant [5] — Reduces the casting time of your Fireball, Frostfire Bolt, and Arcane Wrath spells by 0.1/0.2/0.3/0.4/0.5 sec. `id 11069`

**R2**
- Ignite [5] — Your critical strikes from Fire damage spells cause the target to burn for an additional 8/16/24/32/40% of your spell's damage over 4 sec. `id 11119`
- Flame Throwing [2] — Increases the range of your Fire spells by 3/6 yards. `id 11100`
- Impact [3] — Gives your Fire spells a 3/7/10% chance to stun the target for 2 sec. `id 11103`

**R3**
- Burning Soul [3] — Gives your Fire spells a 23/47/70% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 10/20/30%. `id 11083`
- Improved Flamestrike [3] — Increases the critical strike chance of your Flamestrike spell by 5/10/15%. `id 11108`
- Pyroblast [1] — 125 mana, 35 yd, 6 sec cast, spell power coeff 0.15; numbers are level 60 with 0 spell power. Hurls an immense fiery boulder that causes 100–132 Fire damage and an additional 44 Fire damage over 12 sec. `id 11366`
- Improved Fire Blast [2] — Reduces the cooldown of your Fire Blast spell by 1/2 sec and increases its range by 8/15 yards. `id 11078`

**R4**
- Improved Scorch [3] — Your Scorch spell has a 33/67/100% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. `id 11095`
- Improved Fire Ward [2] — Causes your Fire Ward to have a 10/20% chance to reflect Fire spells while active. `id 11094`
- Heating Up [1] — Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage. *(requires Pyroblast)* `id 400624`
- Master of Elements [3] — Your Fire and Frost critical strikes will refund 10/20/30% of their base mana cost. `id 29074`

**R5**
- Critical Mass [3] — Increases the critical strike chance of your Fire spells by 2/4/6%. `id 11115`
- Blast Wave [1] — 215 mana, 45 sec CD, spell power coeff 0.129; numbers are level 60 with 0 spell power. A wave of flame radiates outward from the caster, damaging all enemies caught within the blast for 153–185 Fire damage, and Dazing them for 50% reduced movement speed for 6 sec. `id 11113`

**R6**
- Fire Power [3] — Increases the damage done by your Fire spells by 1/2/3% per your Fire effects on the target, up to a maximum increase of 4/8/12%. Effects which mix multiple schools of magic do not qualify. `id 11124`

**R7**
- Combustion [1] — 3 min CD. When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells. *(requires Critical Mass)* `id 11129`

### Frost — datamined (18 talents, 48 points)

**R1**
- Frost Warding [2] — Increases the Armor and resistances granted by your Frost Armor and Ice Armor spells by 15/30%, gives your Frost Ward a 10/20% chance to negate the warded damage spell, and increases the amount absorbed by your Ice Barrier and Frost Ward by 10/20%. `id 11189`
- Improved Frostbolt [5] — Reduces the casting time of your Frostbolt spell by 0.1/0.2/0.3/0.4/0.5 sec. `id 11070`
- Precision [3] — Improves your chance to hit with all spells by 2/4/6%. `id 29438`

**R2**
- Ice Shards [5] — Increases the critical strike damage bonus of your Frost spells by 20/40/60/80/100%. `id 11207`
- Frostbite [3] — Gives your Chill effects a 5/10/15% chance to Freeze the target for 5 sec. `id 11071`
- Improved Frost Nova [2] — Reduces the cooldown of your Frost Nova spell by 2/4 sec. `id 11165`
- Permafrost [3] — Increases the duration of your Chill effects by 11/22/33% and reduces the target's speed by an additional 3/7/10%. `id 11175`

**R3**
- Frost Channeling [3] — Reduces the mana cost of your Frost spells by 5/10/15% and reduces the threat caused by your Frost spells by 10/20/30%. `id 11160`
- Improved Blizzard [3] — Adds a Chill effect to your Blizzard spell. This effect lowers the target's movement speed by 15/25/40% for 1.5 sec. `id 11185`
- Ice Lance [1] — 45 mana, 30 yd, 8 sec CD. Deals 28–33 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. `id 1312002`

**R4**
- Arctic Reach [2] — Increases the range of your Frostbolt, Ice Lance, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 10/20%. `id 16757`
- Ice Block [1] — 15 mana, 5 min CD. You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. `id 11958`
- Shatter [3] — Increases the critical strike chance of all your spells against Frozen targets by 17/33/50%. `id 11170`

**R5**
- Improved Cone of Cold [3] — Increases the damage dealt by your Cone of Cold spell by 12/23/35%. `id 11190`
- Cold Snap [1] — 10 min CD. Finishes the remaining cooldown on all your other Frost spells. `id 12472`
- Fingers of Frost [2] — Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 1/2 spells cast as if the target were Frozen. Lasts 15 sec. *(requires Ice Lance)* `id 400647`

**R6**
- Winter's Chill [5] — Gives your Frostbolt and Fingers of Frost empowered Ice Lance spells a 20/40/60/80/100% chance to apply Winter's Chill, increasing the target's damage taken from your next Cone of Cold by 20% and it gains an additional 7% of your spell damage, stacking up to 5 times. `id 11180`

**R7**
- Ice Barrier [1] — 305 mana, 30 sec CD. Shield yourself, absorbing ${448+($SPFR*0.1)*(0/100+1)} damage and increasing your Frost damage by 15% for 1 min. While shielded, your Frost damage is increased by an additional 5% and you do not lose casting time when you take damage. *(requires Cold Snap)* `id 11426`

<!-- /overrides -->

## Arcane (19 talents)

**R1**
- Wand Specialization [2] — Increases your damage with Wands by 13%.
- Arcane Focus [5] — Improves your chance to hit with Arcane spells by 1%.
- Improved Channeling [5] — Gives you a 20% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 14% chance while casting Arcane Blast or Arcane Wrath.
- Missile Barrage [2] — Gives your Arcane Blast spell a 20% chance, your Arcane Missile hits a 5% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 10% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec.

**R2**
- Arcane Subtlety [2] — Reduces your target's resistance to all your spells by 8 and reduces the threat caused by your Arcane spells by 15%.
- Magic Absorption [2] — Increases all your resistances by 5 and causes all spells you fully resist to restore 1% of your total mana. Cannot trigger more often than 1 time per sec.
- Arcane Concentration [5] — Gives you a 2% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%.
- Arcane Resilience [2] — Increases your Armor by an amount equal to 25% of your Intellect.

**R3**
- Arcane Geometry [2] — Increases the range of your Arcane spells by 3 yards.
- Arcane Impact [3] — Increases the critical strike chance of your Arcane spells by 2%.
- Arcane Blast [1] — 15% of base mana | 30 yd range | 1.5 sec cast | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 15% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 175%. Effect stacks up to 4 times and lasts 15 sec from time of initial application.

**R4**
- Arcane Shielding [2] — Decreases the Mana lost per point of damage taken when your Mana Shield spell is active by 17% and increases the resistances granted by your Mage Armor spell by 25%.
- Improved Counterspell [2] — Your Counterspell also Silences the target for 2 sec.
- Arcane Meditation [3] — Allows 17% of your Mana regeneration to continue while casting.
- Arcane Wrath [1] — 140 Mana | 30 yd range | 3.5 sec cast | 6 sec cooldown | Launches a projectile of pure Arcane energy at the enemy target, causing 122 to 146 Arcane damage. This spell gains additional Spell Damage equal to 5% of your maximum Mana.

**R5**
- Presence of Mind [1] — Instant | 3 min cooldown | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell.
- Arcane Mind [5] — Increases your Intellect by 2% and increases the critical strike damage bonus of your Arcane spells by 20%.

**R6**
- Arcane Instability [3] — Increases the damage done by your spells by 1% and your critical strike chance by 1%.

**R7**
- Arcane Power [1] — Instant | 3 min cooldown | For the next 15 sec, your spells deal 30% more damage while costing 30% more mana to cast.

## Fire (17 talents)

**R1**
- Improved Fire Blast [2] — Reduces the cooldown of your Fire Blast spell by 1 sec and increases its range by 8 yards.
- Incineration [3] — Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 2%.
- Improved Fireball [5] — Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.1 sec.

**R2**
- Ignite [5] — Your critical strikes from Fire damage spells cause the target to burn for an additional 8% of your spell's damage over 4 sec.
- Flame Throwing [2] — Increases the range of your Fire spells by 3 yards.
- Impact [3] — Gives your Fire spells a 3% chance to stun the target for 2 sec.

**R3**
- Burning Soul [3] — Gives your Fire spells a 23% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 10%.
- Improved Flamestrike [3] — Increases the critical strike chance of your Flamestrike spell by 5%.
- Pyroblast [1] — 125 Mana | 35 yd range | 6 sec cast | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec.

**R4**
- Improved Scorch [3] — Your Scorch spell has a 33% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times.
- Improved Fire Ward [2] — Causes your Fire Ward to have a 10% chance to reflect Fire spells while active.
- Heating Up [1] — Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage.
- Master of Elements [3] — Your Fire and Frost critical strikes will refund 10% of their base mana cost.

**R5**
- Critical Mass [5] — Increases the critical strike chance of your Fire spells by 2%.
- Blast Wave [1] — 215 Mana | Instant | 45 sec cooldown | A wave of flame radiates outward from the caster, damaging all enemies caught within the blast for 154 to 184 Fire damage, and Dazing them for 50% reduced movement speed for 6 sec.

**R6**
- Fire Power [3] — Increases the damage done by your Fire spells by 1% per your Fire effects on the target, up to a maximum increase of 4%. Effects which mix multiple schools of magic do not qualify.

**R7**
- Combustion [1] — Instant | 3 min cooldown | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells.

## Frost (19 talents)

**R1**
- Frost Warding [2] — Increases the Armor and resistance given by your Frost Armor and Ice Armor spells by 15%. In addition, gives your Frost Ward a 10% chance to reflect Frost spells and effects while active.
- Improved Frostbolt [5] — Reduces the casting time of your Frostbolt and Frost Blast spells by 0.1 sec.
- Elemental Precision [5] — Improves your chance to hit with Frost and Fire spells by 1%.

**R2**
- Ice Shards [5] — Increases the critical strike damage bonus of your Frost spells by 20%.
- Permafrost [3] — Increases the duration of your Chill effects by 11% and reduces the target's speed by an additional 3%.
- Improved Frost Nova [2] — Reduces the cooldown of your Frost Nova spell by 2 sec.
- Frostbite [3] — Gives your Chill effects a 5% chance to Freeze the target for 5 sec.

**R3**
- Piercing Ice [3] — Increases the damage done by your Frost spells by 2%.
- Frost Channeling [3] — Reduces the mana cost of your Frost spells by 5% and reduces the threat caused by your Frost spells by 10%.
- Ice Lance [1] — 45 Mana | 30 yd range | Instant | Deals 28 to 32 Frost damage to an enemy target. Deals 200% increased damage to Frozen targets.
- Improved Blizzard [3] — Adds a Chill effect to your Blizzard spell. This effect lowers the target's movement speed by 15% for 1.5 sec.

**R4**
- Arctic Reach [2] — Increases the range of your Frostbolt, Frost Blast, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 10%.
- Ice Block [1] — 15 Mana | Instant | 5 min cooldown | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells.
- Shatter [3] — Increases the critical strike chance of all your spells against Frozen targets by 17%.

**R5**
- Improved Cone of Cold [3] — Increases the damage dealt by your Cone of Cold spell by 12%.
- Cold Snap [1] — Instant | 10 min cooldown | Finishes the remaining cooldown on all your other Frost spells.
- Fingers of Frost [2] — Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 1 spell cast as if the target were Frozen. Lasts 15 sec.

**R6**
- Winter's Chill [5] — Gives your Frost damage spells a 20% chance to apply the Winter's Chill effect, which increases the damage done by your Cone of Cold spell to the target by 40%, stacking up to 5 times.

**R7**
- Ice Barrier [1] — 305 Mana | Instant | 30 sec cooldown | Instantly shields you, absorbing 447 damage. Lasts 1 min. While the shield holds, your spellcasts will not be interrupted or delayed from taking damage.
