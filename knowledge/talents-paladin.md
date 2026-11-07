# WoW Forever — Paladin Talents
Data as of: 2026-11-07 b:1.60.1.70862 (Overrides block: datamined, tier 2). Generated lines below the block: 2026-10-27 b:beta, tier 3, superseded wherever the block covers the same talent.
Source: classicwowforever.com talent calculator chunk. Rank-1 captured tooltips; higher ranks are the site's estimates. Values change with each build.
Provenance: [T3 cwf 2026-10-27 b:beta] applies to every talent line below unless an Overrides entry says otherwise. The tag date is the date this script fetched the site; the site's own capture may be earlier. Provenance tags: `[T<tier> <source-id> <date> b:<build>]`, see docs/sop-provenance.md and sources.md. Build labels in data/builds.json.

<!-- overrides -->
## Overrides (tier 1–2 values that outrank the generated lines)
*Full datamined tree, TraitTree 1100. [T2 wago 2026-11-07 b:1.60.1.70862] applies to every line in this block. Values written a/b/c are ranks 1/2/3, each read from the client's per-rank curves (TraitDefinitionEffectPoints), not extrapolated.*

### 24 Sept 2026 blue-post class changes (not talent-rank values)
*[T1 blizz-forum 2026-09-24] (Kaivax, WoW Forever Beta Development Notes – Updated September 24, https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-updated-september-24/2360696)*
- Righteous Fury: Holy threat increase reduced to 60% (was 90%).
- Fixed a bug causing the Flash of Light cast animation not to play at the end of the cast; multiple Consecration fixes (targets missing the increased-damage effect, Z-axis inconsistency, could pull targets vertically above/below caster).
- Retribution Aura now dynamically scales with the caster's spell power.
- Fixed a bug with Echo of Justice giving a higher-than-intended activation chance.
- Holy Strike's % of weapon damage per rank, cooldown, Holy Power crit bonus, Retribution talent reshuffle (Improved Holy Strike removed and made baseline, Sacred Arbiter, Two-Handed Weapon Specialization, Vengeance, Twist of Light): see tree below, already updated.

### In-game observations on the live client (not tooltip numbers)
*Provenance: [T2 in-game 2026-09-23 b:1.60.1.69913] — the maintainer's Undead Retribution Paladin at level 20. Method: played, read on screen, no measurement or sample size.*
- **Judgement no longer consumes the active Seal.** There is no reseal step in the Forever Retribution rotation.
- Benediction's "all instant cast spells and abilities" does cover Judgement, the Seals, Consecration, Exorcism, Holy Strike and Hammer of Justice in practice.
- Resistance auras are not available at level 20.
- Blessing of Might against Blessing of Kings, measured on his own character: at 17, 235 attack power and 9.3% crit against 226 and 9.7%; at 20 with better gear, 247 against 240 attack power. The gap is 7 to 9 attack power, so Kings wins on crit plus the Stamina and Intellect. Recheck when the next rank of Might lands at 22.
- Conviction lifts melee crit only; on his character melee crit read 10.62% while Holy spell crit read 5.00% with Conviction 5/5 [T2 in-game 2026-09-25 b:1.60.1.70009]. Forever's unified hit and crit means one rating covers all three schools, not that every talent does.
- Note that the 24 Sept patch **deleted Crusade** and made Improved Holy Strike baseline, so any Retribution plan written before 24 Sept needs redoing.

### 1–27 Oct 2026 blue-post class changes, checked against b:1.60.1.70634 (not talent-rank values; layered on the tree below)
*[T1 blizz-forum 2026-10-16] unless a line carries its own tag. Source: Kaivax, WoW Forever Beta Development Notes (topic 2360696): posts of 1 Oct [T1 blizz-forum 2026-10-01], 8 Oct [T1 blizz-forum 2026-10-08] and 16 Oct. Where the 27 Oct datamine shows the same change the line also carries [T2 wago 2026-10-27 b:1.60.1.70634]. These notes supersede the 24 Sept block above wherever they overlap. Class deep-dive articles of 30 Sept to 15 Oct (blizz-news 24301515, 24301514, 24302097, 24310968, 24302099) describe the same beta changes and were not stored line by line.*
- **Retribution, Champion of the Light:** Intellect-to-spell-damage ratio cut to 20 / 40 / 60% (was 33 / 66 / 100%); the tooltip claim of healing was wrong and removed [T1 blizz-forum 2026-10-01; T2 wago 2026-10-27 b:1.60.1.70634]. **Conflict:** the 16 Oct notes say a further cut to 10 / 20 / 30% [T1 blizz-forum 2026-10-16], b:1.60.1.70532 showed 10 / 20 / 30% [T2 wago 2026-10-27 b:1.60.1.70532], and the newer b:1.60.1.70634 shows 20 / 40 / 60% again [T2 wago 2026-10-27 b:1.60.1.70634]. By SOP section 2 the newer datamine wins; the 16 Oct figure is kept as Blizzard's stated intent. No post announces a revert.
- **Retribution Aura:** now uses the Paladin's spell power, not the target's; base damage returned to Vanilla values (about 33% lower), spell power ratio 6% (was 13.3%) [T1 blizz-forum 2026-10-08].
- **Retribution, Sanctified Judgement:** the mana it restores no longer generates threat [T1 blizz-forum 2026-10-16]. Numbers unchanged: 33 / 66 / 100% chance to return 20 / 40 / 60% of the seal's cost [T2 wago 2026-10-27 b:1.60.1.70634].
- **Seals and Judgement:** Judgement of Righteousness and Judgement of Fury got correct spell power coefficients; Seal of Righteousness had nearly double the intended spell damage benefit, fixed; Consecration coefficient per tick 0.042 (was 0.095); Righteous Fury Holy threat 90% (was 60%); Seal of Fury rank 3 trains at level 26 (was 25) [T1 blizz-forum 2026-10-16]. Salvation is no longer a blessing; Revoke removes it [T1 blizz-forum 2026-10-16].
- **Protection:** Redoubt block chance 4 / 8 / 12 / 16 / 20% (was 6 / 12 / 18 / 24 / 30%); Holy Shield block 30% (was 20%) [T1 blizz-forum 2026-10-01; T2 wago 2026-10-27 b:1.60.1.70634]. Shield Specialization mana restore 4% with a 3 sec internal cooldown (was 6%) [T1 blizz-forum 2026-10-16; T2 wago 2026-10-27 b:1.60.1.70634]. Reckoning stores up to 4 charges, spent on the next auto attack, and cannot trigger from blocks more than once per 1.5 sec [T1 blizz-forum 2026-10-16; T1 blizz-forum 2026-10-08; T2 wago 2026-10-27 b:1.60.1.70634]. Improved Seal of Fury and Shield Specialization mana returns no longer generate threat [T1 blizz-forum 2026-10-08].
- **Holy:** Infusion of Light no longer gives Holy Shock 50% extra damage against enemies; the Light's Vigil focus-macro bug is fixed [T1 blizz-forum 2026-10-16].
- Seal of Command's proc rate (INDEX question 8) is not stated in any post and not visible in the tables [T2 wago 2026-10-27 b:1.60.1.70634].

### 2 Nov 2026 development notes, checked against b:1.60.1.70790 (launch client; supersedes the 1-27 Oct block above wherever they overlap)
*[T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] unless a line carries its own tag. Source: Kaivax, WoW Forever Beta Development Notes, updated 2 Nov (topic 2360696, post 9, https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9). Per-rank talent numbers are in the datamined tree below.*
- **Retribution, Champion of the Light:** now 5 ranks, spell damage 12 / 24 / 36 / 48 / 60% of Intellect, and it reduces Hammer of Wrath cast time by 0.2 / 0.4 / 0.6 / 0.8 / 1.0 sec [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] (was: 3 ranks, 20 / 40 / 60% [T2 wago 2026-10-27 b:1.60.1.70634]). The 20 / 40 / 60% vs 10 / 20 / 30% conflict in the 1-27 Oct block is over: the maximum is 60% in both b:1.60.1.70634 and b:1.60.1.70790, now reached over 5 ranks.
- **Retribution, other talents:** Conviction is 3 ranks, +2 / 4 / 6% crit with all spells and attacks (was 5 ranks, 1-5% melee only). Vindication no longer gives Attack Power (only the target Attack Power reduction remains). Two-Handed Weapon Specialization is +2 / 4 / 6% Physical and Holy damage and reduces threat 7 / 14 / 20% while a two-handed weapon is equipped. Vengeance stacks to 5 (was 3) and requires Seal of Command. Instrument of Law and Twist of Light removed. **Unsealed Wrath** is the new 31-point talent (stores a copy of your Seal for 15 sec, up to 3 stacks; requires Repentance). Turn Evil added in row 5. Unyielding Faith moved here from Holy. Holy Conduit moved to Holy [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03].
- **All specs:** Righteous Fury trainable at level 10 (was 16); it gives +33% to all threat and an extra +90% threat from Holy damage. Salvation, Mass Salvation, Revoke and Blessing of Light are removed (the spells are gone from the client). Judgement of Fury lasts 3 sec (was 4) [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03].
- **Holy:** new Oath of Light (8% base mana, 40 yd, 5 min; Holy Light +400, Flash of Light +115, Holy Shock +230 at level 60) and Boundless Light (+15 / 30% Holy Shock crit on allies without your Oath). Holy Power is now +10 / 20 / 30 / 40 / 50% crit healing bonus on Holy spells. Voice of Truth removed. Light's Vigil is friendly-only. Divine Precision 2 ranks, 4 / 8% hit [T1 blizz-forum 2026-11-03].
- **Protection:** Improved Seal of Fury and One-Handed Weapon Specialization removed; Templar's Bulwark is dispellable; Swift Judgement now unleashes the active Seal without sharing Judgement's cooldown; new Stoicism and Shieldsworn [T1 blizz-forum 2026-11-03].
- **Not changed:** Seal of Command's proc rate is not in the diff or the notes (INDEX open question 8 stays open) [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03].

### Holy — datamined (17 talents, 46 points)

**R1**
- Spiritual Focus [5] — Gives your Flash of Light, Holy Light, and Light's Vigil spells a 14/28/42/56/70% chance to not lose casting time when you take damage. `id 20205`
- Divine Strength [5] — Increases your Strength by 2/4/6/8/10%. `id 20262`

**R2**
- Healing Light [3] — Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 4/8/12%. `id 20237`
- Reverence [2] — Allows 15/30% of your Mana regeneration to continue while casting. `id 1310899`
- Improved Seals [5] — Increases the damage done by your Seals and Judgements by 3/6/9/12/15%. `id 20224`
- Purifying Power [2] — Reduces the mana cost of your Cleanse and Purify spells by 10/20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 17/33%. `id 429144`

**R3**
- Divine Favor [1] — 4% of base mana, 2 min CD. When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. `id 20216`
- Illumination [5] — After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 20/40/60/80/100% chance to gain Mana equal to 50% of the base cost of the spell. *(requires Reverence)* `id 20210`
- Holy Conduit [2] — Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 20/40%. `id 1237268`

**R4**
- Divine Precision [2] — Improves your chance to hit with Holy spells by 4/8%, and reduces the duration of Silence effects on you by 10/20%. `id 1310904`
- Infusion of Light [2] — Your Holy Shock and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 0.5/1.0 sec. `id 426065`
- Oath of Light [1] — 8% of base mana, 40 yd. Swear an Oath to protect target ally for 5 min, increasing the healing of your Holy Light on them by up to 400, your Flash of Light by up to 115, and your Holy Shock by up to 230. Only one Oath of Light may be sworn by the Paladin at any one time. `id 1328548`

**R5**
- Consecrated Ground [2] — Gives your Holy spells 5/10% increased damage against the first 4 enemies that enter your Consecration. `id 1310905`
- Holy Shock [1] — 160 mana, 20 yd, 10 sec CD. Blasts the target with Holy energy, causing 129–139 Holy damage to an enemy, or 110–118 healing to an ally. `id 1311606`
- Boundless Light [2] — Increases the critical strike chance of your Holy Shock spell by 15/30% when cast on allies not affected by your Oath of Light. *(requires Holy Shock)* `id 1328550`

**R6**
- Holy Power [5] — Increases the critical strike healing bonus of your Holy spells by 10/20/30/40/50%. `id 5923`

**R7**
- Light's Vigil [1] — 730 mana, 40 yd, 1.5 sec cast, 6 sec CD. Applies Light's Vigil to a friendly target for 30 sec. The caster's next Holy Shock on the target incurs no cooldown and heals the target and their party for 325–344. Only one Vigil per Paladin may be active in each party. *(requires Holy Shock)* `id 1310911`

### Protection — datamined (17 talents, 49 points)

**R1**
- Divine Intellect [5] — Increases your total Intellect by 2/4/6/8/10%. `id 20257`
- Redoubt [5] — Damaging melee attacks against you have a 10% chance to increase your chance to block by 6/12/18/24/30%. Lasts 10 sec or 5 blocks. `id 20127`

**R2**
- Precision [3] — Improves your chance to hit by 1/2/3%. `id 20189`
- Guardian's Favor [2] — Reduces the cooldown of your Blessing of Protection by 1/2 min and increases the duration of your Blessing of Freedom by 3/6 sec. `id 20174`
- Sacred Duty [2] — Reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 30/60 sec, and reduces the duration of Forbearance by 5/10 sec. `id 1224697`

**R3**
- Templar's Bulwark [1] — 110 mana, 5 min CD. When activated, this ability grants you an absorb shield equal to 100% of your maximum health for 8 sec. Applies Forbearance for 1 min. Cannot be cast while Forbearance is active. `id 1311015`
- Improved Hammer of Justice [3] — Decreases the cooldown of your Hammer of Justice spell by 5/10/15 sec. `id 20487`
- Shield Specialization [2] — Increases the amount of damage absorbed by your shield by 15/30%, and gives your blocks a 50/100% chance to restore 4% of your maximum Mana. May only occur once every $proccooldown sec. *(requires Redoubt)* `id 20150`
- Toughness [5] — Increases your armor value from items by 2/4/6/8/10%. `id 20143`

**R4**
- Swift Judgement [1] — 10 yd, 1 min CD. Unleash the energy of a Seal spell upon an enemy. Does not consume the Seal. Refer to individual Seals for Judgement effect. Does not share a cooldown with your Judgement ability. *(requires Templar's Bulwark)* `id 1310994`
- Improved Righteous Fury [3] — While Righteous Fury is active, all damage taken is reduced by 3/6/9%. `id 20468`
- Anticipation [5] — Increases your Defense Skill by 4/8/12/16/20. `id 20096`

**R5**
- Stoicism [2] — Reduces the duration of Stun and Charm effects on you by 10/20%. `id 1328546`
- Holy Shield [1] — 100 mana, 10 sec CD. Increases chance to block by 30% for 10 sec, and deals 75 Holy damage for each attack blocked while active. Damage caused by Holy Shield causes 20% additional threat. Each block expends a charge. 4 charges. `id 20925`
- Reckoning [5] — Gives you a 8/16/24/32/40% chance after Blocking and a 20/40/60/80/100% chance after receiving a non-periodic critical strike to gain an extra attack. Stores up to 4 extra attacks. Cannot occur from Blocks more than once every ${$proccooldown}.1 sec. `id 20177`

**R6**
- Iron Creed [3] — Increases the threat generated by your Holy Strike ability by 10/20/30%. While Righteous Fury is active, Holy Strike also reduces your damage taken by 2/4/6% for 6 sec. `id 1311034`

**R7**
- Shieldsworn [1] — Reduces the cooldown of your Holy Strike ability by 4 sec. Additionally, Holy Strike now strikes with your shield, triggering your active Holy Shield and Shield Specialization talents without consuming their charges or triggering their cooldowns, and allowing you to Block spells for 6 sec. *(requires Holy Shield)* `id 1328544`

### Retribution — datamined (17 talents, 44 points)

**R1**
- Deflection [5] — Increases your Parry chance by 1/2/3/4/5%. `id 20060`
- Benediction [5] — Reduces the Mana cost of all instant cast spells and abilities by 2/4/6/8/10%. `id 20101`

**R2**
- Improved Judgement [2] — Decreases the cooldown of your Judgement ability by 1/2 sec. `id 25956`
- Conviction [3] — Improves your chance to get a critical strike with all spells and attacks by 2/4/6%. `id 20117`
- Sanctified Judgement [3] — Gives your Judgement ability a 33/66/100% chance to return 20/40/60% of the Mana cost of the judged seal. `id 1311074`

**R3**
- Vindication [3] — Gives your damaging melee attacks a chance to reduce the target's Attack Power by 68/136/204 for 30 sec. `id 9452`
- Unyielding Faith [2] — Reduces the duration of Fear and Disorient effects on you by 15/30%. `id 9453`
- Seal of Command [1] — 65 mana. Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec. Unleashing this Seal's energy will judge an enemy, instantly causing 71 Holy damage, 136–148 if the target is stunned or incapacitated. `id 20375`
- Pursuit of Justice [2] — Increases movement speed and mounted movement speed by 8/15%. This does not stack with other movement speed increasing effects. `id 26022`

**R4**
- Eye for an Eye [2] — All critical strikes against you cause 5/10% of the damage taken to the attacker as well. The damage caused by Eye for an Eye will not exceed 50% of the Paladin's total health. `id 9799`
- Sacred Arbiter [1] — Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. `id 1311087`
- Two-Handed Weapon Specialization [3] — Increases the Physical and Holy damage you deal by 2/4/6%, and reduces all threat you generate by 7/14/20% while a two-handed melee weapon is equipped. `id 20111`

**R5**
- Turn Evil [2] — Reduces the cast time of your Turn Undead spell by 0.5/1.0 sec, its cooldown by 5/10 sec, and allows it to affect Demons. `id 1328370`
- Repentance [1] — 60 mana, 20 yd, 1 min CD. Puts the enemy target in a state of meditation, incapacitating them for up to 6 sec. Any damage caused will awaken the target. Only works against Humanoids. `id 20066`
- Vengeance [3] — Increases your Physical and Holy damage dealt by 1/2/3% for 30 sec after landing a non-periodic critical strike. Stacks up to 5 times. *(requires Seal of Command)* `id 20049`

**R6**
- Champion of the Light [5] — Increases your spell damage by up to 12/24/36/48/60% of your Intellect, and reduces the cast time of your Hammer of Wrath by 0.2/0.4/0.6/0.8/1.0 sec. `id 1311084`

**R7**
- Unsealed Wrath [1] — Your melee attacks store a copy of your active Seal for 15 sec, stacking up to 3 times. Landing an attack with a different Seal consumes all stacks, giving the stored Seal its normal chance to activate once per stack. *(requires Repentance)* `id 1310735`

<!-- /overrides -->

## Holy (17 talents)

**R1**
- Divine Strength [5] — Increases your Strength by 2%.
- Divine Intellect [5] — Increases your total Intellect by 2%.

**R2**
- Healing Light [3] — Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 4%.
- Spiritual Focus [2] — Gives your Flash of Light, Holy Light, and Light's Vigil spells a 35% chance to not lose casting time when you take damage.
- Improved Seals [3] — Increases the damage done by your Seals and Judgements by 5%.
- Unyielding Faith [2] — Reduces the duration of Fear and Disorient effects on you by 15%.

**R3**
- Voice of Truth [1] — Instant | 3 min cooldown | Grants you immunity to Silence and Interrupt effects for 6 sec.
- Reverence [3] — Allows 10% of your Mana regeneration to continue while casting.
- Purifying Power [2] — Reduces the mana cost of your Cleanse and Purify spells by 10% and reduces the cooldown of your Exorcism and Holy Wrath spells by 17%.

**R4**
- Infusion of Light [2] — Your Holy Shock and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 0.5 sec.
- Illumination [5] — After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 20% chance to gain Mana equal to 50% of the base cost of the spell.
- Divine Favor [1] — 4% of base mana | Instant | 2 min cooldown | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance.

**R5**
- Divine Precision [3] — Improves your chance to hit with Holy spells by 6%.
- Holy Shock [1] — 160 Mana | Enemy: 20 yd range | Friendly: 40 yd range | Instant | 10 sec cooldown | Blasts the target with Holy energy, causing 129 to 139 Holy damage to an enemy, or 110 to 118 healing to an ally.
- Consecrated Ground [2] — Gives your Holy spells 5% increased damage against the first 4 enemies that enter your Consecration.

**R6**
- Holy Power [5] — Increases the critical strike chance of your Holy Shock and Holy Strike spells by 3%, and all other spells by 1%.

**R7**
- Light's Vigil [1] — 730 Mana | Enemy: 20 yd range | Friendly: 40 yd range | 1.5 sec cast | 6 sec cooldown | Applies Light's Vigil to the target for 30 sec. Your next Holy Shock cast on them triggers no cooldown and causes enemy targets to suffer 175 to 189 Holy damage and refund 75% of Light's Vigil's Mana cost, or allied targets to heal their party for 325 to 343. You may only have one Light's Vigil active per party.

## Protection (16 talents)

**R1**
- Toughness [5] — Increases your armor value from items by 2%.
- Redoubt [5] — Damaging melee attacks against you have a 10% chance to increase your chance to block by 4%. Lasts 10 sec or 5 blocks.

**R2**
- Precision [3] — Improves your chance to hit by 1%.
- Guardian's Favor [2] — Reduces the cooldown of your Blessing of Protection by 1 min and increases the duration of your Blessing of Freedom by 3 sec.
- Anticipation [5] — Increases your Defense Skill by 4.

**R3**
- Improved Seal of Fury [1] — When Seal of Fury's shield is fully absorbed, restore 60 Mana, increased by 15% per level the attacker is above you, up to 45%.
- Improved Righteous Fury [3] — While Righteous Fury is active, all damage taken is reduced by 2%.
- Shield Specialization [3] — Increases the amount of damage absorbed by your shield by 10%, and gives your blocks a 33% chance to restore 4% of your maximum Mana. May only occur once every 3 sec.
- Sacred Duty [2] — Increases your total Stamina by 2% and reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 30 sec.

**R4**
- Swift Judgement [1] — Instant | 1 min cooldown | Finishes the remaining cooldown on your Judgement ability and reduces the Mana cost of your next Judgement by 100%.
- One-Handed Weapon Specialization [3] — Increases the damage you deal with one-handed melee weapons by 3%.
- Improved Hammer of Justice [3] — Decreases the cooldown of your Hammer of Justice spell by 5 sec.

**R5**
- Templar's Bulwark [1] — 110 Mana | Instant | 5 min cooldown | When activated, this ability grants you an absorb shield equal to 100% of your maximum health for 8 sec. Applies Forbearance for 1 min. Cannot be cast while Forbearance is active.
- Reckoning [5] — Gives you a 8% chance after Blocking and a 20% chance after receiving a non-periodic critical strike to gain an extra attack. Stores up to 4 extra attacks. Cannot occur from Blocks more than once every 1.5 sec.

**R6**
- Iron Creed [5] — Increases the threat generated by your Holy Strike ability by 5%. While Righteous Fury is active, Holy Strike also reduces your damage taken by 2% for 6 sec.

**R7**
- Holy Shield [1] — 150 Mana | Instant | 10 sec cooldown | Requires Shields | Increases chance to block by 30% for 10 sec, and deals 110 Holy damage for each attack blocked while active. Damage caused by Holy Shield causes 20% additional threat. Each block expends a charge. 4 charges.

## Retribution (17 talents)

**R1**
- Deflection [5] — Increases your Parry chance by 1%.
- Benediction [5] — Reduces the Mana cost of all instant cast spells and abilities by 2%.

**R2**
- Improved Judgement [2] — Decreases the cooldown of your Judgement ability by 1 sec.
- Holy Conduit [2] — Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 20%.
- Conviction [5] — Improves your chance to get a critical strike with melee attacks by 1%.

**R3**
- Vindication [3] — Gives your damaging melee attacks a chance to reduce the target's Attack Power by 67, and increase your Attack Power by 1% for 30 sec.
- Sanctified Judgement [3] — Gives your Judgement ability a 33% chance to return 20% of the Mana cost of the judged seal.
- Seal of Command [1] — 65 Mana | Instant | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec. | Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated.
- Pursuit of Justice [2] — Increases movement speed and mounted movement speed by 8%. This does not stack with other movement speed increasing effects.

**R4**
- Eye for an Eye [2] — All critical strikes against you cause 5% of the damage taken to the attacker as well. The damage caused by Eye for an Eye will not exceed 50% of the Paladin's total health.
- Sacred Arbiter [1] — Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target.

**R5**
- Two-Handed Weapon Specialization [3] — Increases the damage you deal with two-handed melee weapons by 2%.
- Vengeance [3] — Increases your Physical and Holy damage dealt by 1% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times.
- Repentance [1] — 60 Mana | 20 yd range | Instant | 1 min cooldown | Puts the enemy target in a state of meditation, incapacitating them for up to 6 sec. Any damage caused will awaken the target. Only works against Humanoids.

**R6**
- Champion of the Light [3] — Increases your spell damage by up to 10% of your Intellect.
- Instrument of Law [2] — Reduces the cast time of your Hammer of Wrath by 0.5 sec, and reduces all threat you generate by 10% while Righteous Fury is not active.

**R7**
- Twist of Light [1] — Requires Level 40 | Reduces the Mana cost of your Seal spells by 20%, and when you replace your Seal of Command, Seal of Righteousness, Seal of Fury, or Seal of Justice with a different Seal, you gain an Echo of that Seal. Your next melee attack applies the replaced Seal's effects, consuming the Echo.
