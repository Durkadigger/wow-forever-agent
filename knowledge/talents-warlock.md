# WoW Forever — Warlock Talents
Data as of: 2026-11-07 b:1.60.1.70862 (Overrides block: datamined, tier 2). Generated lines below the block: 2026-10-27 b:beta, tier 3, superseded wherever the block covers the same talent.
Source: classicwowforever.com talent calculator chunk. Rank-1 captured tooltips; higher ranks are the site's estimates. Values change with each build.
Provenance: [T3 cwf 2026-10-27 b:beta] applies to every talent line below unless an Overrides entry says otherwise. The tag date is the date this script fetched the site; the site's own capture may be earlier. Provenance tags: `[T<tier> <source-id> <date> b:<build>]`, see docs/sop-provenance.md and sources.md. Build labels in data/builds.json.

<!-- overrides -->
## Overrides (tier 1–2 values that outrank the generated lines)
*Full datamined tree, TraitTree 1116. [T2 wago 2026-11-07 b:1.60.1.70862] applies to every line in this block. Values written a/b/c are ranks 1/2/3, each read from the client's per-rank curves (TraitDefinitionEffectPoints), not extrapolated.*

### 24 Sept 2026 blue-post class changes (not talent-rank values)
*[T1 blizz-forum 2026-09-24] (Kaivax, WoW Forever Beta Development Notes – Updated September 24, https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-updated-september-24/2360696)*
- Life Tap tooltip corrected to show the amount of Life converted and only states it scales with Spirit (no functional change stated).
- Voidwalker Sacrifice now correctly scales with 10% of the Warlock's spell healing (bug fix).

### 1–27 Oct 2026 blue-post class changes, checked against b:1.60.1.70634 (not talent-rank values; layered on the tree below)
*[T1 blizz-forum 2026-10-16] unless a line carries its own tag. Source: Kaivax, WoW Forever Beta Development Notes (topic 2360696): posts of 1 Oct [T1 blizz-forum 2026-10-01], 8 Oct [T1 blizz-forum 2026-10-08] and 16 Oct. Where the 27 Oct datamine shows the same change the line also carries [T2 wago 2026-10-27 b:1.60.1.70634]. These notes supersede the 24 Sept block above wherever they overlap. Class deep-dive articles of 30 Sept to 15 Oct (blizz-news 24301515, 24301514, 24302097, 24310968, 24302099) describe the same beta changes and were not stored line by line.*
- **Affliction:** Malediction replaced by Grim Reach (range of Affliction spells +10 / 20%); Shadow Mastery doubled to 2 / 4 / 6 / 8 / 10%; Soul Harvesting renamed Soul Harvest [T1 blizz-forum 2026-10-16; T2 wago 2026-10-27 b:1.60.1.70634]. **Destruction:** Destructive Reach affects Destruction spells only; Hellfire can crit [T1 blizz-forum 2026-10-16; T1 blizz-forum 2026-10-01; T2 wago 2026-10-27 b:1.60.1.70634]. Drain Soul now stops when another spell starts [T1 blizz-forum 2026-10-01].

### 2 Nov 2026 development notes, checked against b:1.60.1.70790 (launch client; supersedes the 1-27 Oct block above wherever they overlap)
*[T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] unless a line carries its own tag. Source: Kaivax, WoW Forever Beta Development Notes, updated 2 Nov (topic 2360696, post 9, https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9). Per-rank talent numbers are in the datamined tree below.*
- **Affliction:** Wrack spell power coefficient doubled to 0.286 and base damage per second up to 86 at level 60 (was 36) [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] (was: coefficient 0.143, 36 per sec [T2 wago 2026-10-27 b:1.60.1.70634]). Improved Drains now raises Drain Mana's mana drained and no longer raises Wrack damage. Amplify Curse now also affects Curse of Exhaustion and Bane of Agony. Bane of Agony updates its damage dynamically. Drain Soul's chance to grant a Soul Shard on damage (not a kill) is reduced significantly [T1 blizz-forum 2026-11-03].
- **Destruction:** Shadow and Flame bonuses are 4 / 8 / 12 / 16 / 20% (was 2 / 4 / 6 / 8 / 10%) [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] (was: 2 / 4 / 6 / 8 / 10% [T2 wago 2026-10-27 b:1.60.1.70634]).
- **Pets and items:** pets gain 2 Health per point of the master's Stamina (was 7.5). Spellstones now increase only Shadow damage [T1 blizz-forum 2026-11-03]. Orc Command (+5% Warlock and Hunter pet damage) is back for Orc Warlocks [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03].

### 6 Nov 2026 hotfixes and the 10 Nov tuning notice
*[T1 blizz-forum 2026-11-06] (Kaivax, "WoW: Forever Hotfixes - November 6, 2026", https://us.forums.blizzard.com/en/wow/t/wow-forever-hotfixes-november-6-2026/2403040/4) unless a line carries its own tag; client build 1.60.1.70862 (7 Nov) carries the matching tooltip changes [T2 wago 2026-11-07 b:1.60.1.70862]. Builds 70840 and 70862 are the first post-launch client builds; 70840 was not snapshotted. No talent rank changed between 70790 and 70862.*
- Voidwalker base health increased by about 40 at all levels.
- Soul Siphon no longer incorrectly makes Wrack increase its own damage.
- **Announced for a 10 Nov hotfix** [T1 blizz-forum 2026-11-06] (Kaivax, "Class Tuning Incoming - November 10", https://us.forums.blizzard.com/en/wow/t/class-tuning-incoming-november-10/2404092/1): Voidwalkers tank worse than intended and will get stats raised to match Classic Era; and because always channelling Wrack currently beats also casting Siphon Life, Corruption and Bane of Agony, those DoTs will be adjusted to always be worth casting alongside Wrack without changing Affliction's total damage. Current values stand until the hotfix lands.
- Orc Command: some Warlock pet abilities benefited too much from it, fixed [T1 blizz-forum 2026-11-06]; client: Command (spell 20575) second effect 5 → 0 [T2 wago 2026-11-07 b:1.60.1.70862].

### Affliction — datamined (17 talents, 46 points)

**R1**
- Improved Life Tap [2] — Increases the amount of Mana awarded by your Life Tap spell by 10/20%. `id 18182`

**R2**
- Suppression [5] — Improves your chance to hit by 1/2/3/4/5% and reduces all threat you generate by 4/8/12/16/20%. `id 18174`
- Improved Corruption [5] — Reduces the casting time of your Corruption spell by 0.4/0.8/1.2/1.6/2 sec and increases the damage it deals by 2/4/6/8/10%. `id 17810`

**R3**
- Grim Reach [2] — Increases the range of your Affliction spells by 10/20%. `id 18218`
- Soul Harvest [2] — Killing a non-trivial target afflicted by your Drain Soul increases your Mana regeneration by 50/100% for 10 sec and allows 50/100% of normal Mana regeneration to continue while casting. `id 437032`
- Improved Drains [3] — Increases Health drained, damage done, or Mana drained by your Drain Life, Drain Soul, and Drain Mana spells by 7/13/20%. `id 403511`

**R4**
- Amplify Curse [1] — 3 min CD. Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec. `id 18288`

**R5**
- Improved Bane of Agony [2] — Increases the damage done by your Bane of Agony by 5/10%. `id 18827`
- Fel Concentration [3] — Gives your Drain Life, Drain Mana, Drain Soul, and Wrack spells a 23/47/70% chance to not lose casting time when you take damage. `id 17783`
- Pandemic [3] — Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 33/67/100%. `id 427712`

**R6**
- Malevolence [5] — Increases the critical effect chance of your Shadow spells by 1/2/3/4/5%. `id 1310949`
- Nightfall [2] — Gives your Corruption, Drain Soul, Drain Life, and Wrack spells a 2/4% chance to cause you to enter a Shadow Trance after damaging the opponent. The Shadow Trance reduces the casting time of your next Shadow Bolt spell by 100%. `id 18094`
- Curse of Exhaustion [1] — 8% of base mana, 30 yd. Reduces the target's movement speed by 30% for 12 sec. Only one Curse per Warlock can be active on any one target. *(requires Amplify Curse)* `id 18223`

**R7**
- Siphon Life [1] — 150 mana, 30 yd. Transfers 11 health from the target to the caster every 3 sec. Lasts 30 sec. `id 18265`
- Soul Siphon [3] — Increases the damage done or health drained by your Drain Life, Drain Soul, and Wrack spells by 4/8/12% per each of your other Affliction effects active on the target, up to a maximum increase of 12/24/36%. `id 17804`

**R8**
- Shadow Mastery [5] — Increases the damage dealt or life drained by your Shadow spells by 2/4/6/8/10%. `id 18271`

**R9**
- Wrack [1] — 200 mana, 30 yd, spell power coeff 0.286; numbers are level 60 with 0 spell power. Tears the target apart from within, inflicting 86 Shadow damage every 1 sec and increasing the damage they take from your other Shadow damage over time effects by 10% for 6 sec. *(requires Siphon Life)* `id 1316697`

### Demonology — datamined (19 talents, 50 points)

**R2**
- Improved Health Funnel [2] — Increases the amount of health transferred by your Health Funnel spell by 20/40%, reduces its health cost by 15/30%, and reduces all threat your Health Funnel generates by 50/100%. Allows Health Funnel to be used regardless of your demon's health. `id 18703`
- Improved Imp [3] — Increases the damage of your Imp's Firebolt spell by 10/20/30% and the effect of its Fire Shield spell by 10/20/30%. `id 18694`
- Demonic Embrace [5] — Increases your total Stamina by 3/6/9/12/15%. `id 18697`
- Unholy Power [5] — Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 2/4/6/8/10%. `id 18769`

**R3**
- Demonic Aegis [2] — Increases the effectiveness of your Demon Skin and Demon Armor spells by 15/30%. `id 1235316`
- Improved Voidwalker [3] — Increases the effectiveness of your Voidwalker's Torment, Consume Shadows, Sacrifice, and Suffering spells by 10/20/30%. `id 18705`
- Fel Vitality [3] — Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 5/10/15%, and increases your maximum Mana by 5/10/15%. `id 18731`
- Demonic Energies [2] — You heal your pet for 8/15% of all spell damage you deal. When you gain Mana from Life Tap, your summoned demon gains 50/100% of the Mana you gain. `id 1225214`

**R5**
- Improved Sayaad [3] — Increases the effect of your Succubus' and Incubus' Lash of Pain and Soothing Kiss spells by 10/20/30%, and increases the duration of your Succubus' and Incubus' Seduction and Lesser Invisibility spells by 10/20/30%. `id 18754`
- Demonic Sacrifice [1] — 100 yd. When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hr. The effect is canceled if any Demon is summoned. Imp: Increases your Shadow damage by 15%. Voidwalker: Restores 2% of your total Mana every 4 sec. Succubus/Incubus: Increases your Fire damage by 15%. Felhunter: Restores 3% of your total Health every 4 sec. `id 18788`
- Master Summoner [2] — Reduces the casting time of your Imp, Voidwalker, Succubus, Incubus, and Felhunter Summoning spells by 2/4 sec and the Mana cost by 20/40%. `id 18709`

**R6**
- Decimation [2] — Reduces the cooldown of your Soul Fire spell by 45/90%. When you cast Shadow Bolt or Searing Pain on an enemy below 35% health, they deal 3/6% increased damage, and for the next 10 sec your Soul Fire spell has its cast time reduced by 20/40% and costs no Soul Shards. `id 440870`
- Fel Domination [1] — 5 min CD. Your next Imp, Voidwalker, Succubus, Incubus, or Felhunter Summon spell has its casting time reduced by 5.5 sec and its Mana cost reduced by 50%. *(requires Master Summoner)* `id 18708`
- Demonic Brand [3] — Your Searing Pain generates 17/33/50% less threat and brands the target for 10 sec. Your pet's next 2/4/6 attacks against the target deal $<minDam> to $<maxDam> Fire or Shadow damage based on the pet. If Shadow damage is dealt, it has high threat. `id 1293695`

**R7**
- Improved Felhunter [3] — Increases the Attack Power reduction of your Felhunter's Tainted Blood, the healing of its Devour Magic, and the detection level of its Paranoia by 10/20/30%, and reduces the cooldown of its Spell Lock by 2/4/6 sec. `id 1225217`
- Soul Link [1] — 20% of base mana, 100 yd. When active, 30% of all damage taken by the caster is taken by your Imp, Voidwalker, Succubus, Incubus, or Felhunter Demon instead. In addition, both the Demon and the master will inflict 3% more damage. Lasts as long as the Demon is active. *(requires Demonic Sacrifice)* `id 19028`
- Demonic Knowledge [3] — Increases your spell damage and your Demon pet's spell damage by up to 33/67/100% of your level while you have a summoned Demon pet active. `id 412732`

**R8**
- Master Demonologist [5] — Grants both the Warlock and the summoned demon an effect as long as that demon is active. Imp - Increases Fire damage done by 2/4/6/8/10%. Voidwalker - Reduces Physical damage taken by 2/4/6/8/10%. Succubus/Incubus - Increases Shadow damage done by 2/4/6/8/10%. Felhunter - Reduces Magic damage taken by 2/4/6/8/10%. `id 23785`

**R9**
- Demonic Pact [1] — Your Demonic Sacrifice effect is no longer cancelled by summoning a different Demon pet. Resummoning the sacrificed pet will still cancel the effect. *(requires Soul Link)* `id 425464`

### Destruction — datamined (16 talents, 50 points)

**R2**
- Destructive Reach [2] — Increases the range of your Destruction spells by 10/20%. `id 17917`
- Improved Shadow Bolt [5] — Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 4/8/12/16/20% for 12 sec. `id 17793`
- Bane [5] — Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.1/0.2/0.3/0.4/0.5 sec and your Soul Fire spell by 0.4/0.8/1.2/1.6/2 sec. `id 17788`

**R3**
- Molten Skin [5] — Reduces all damage taken by 2/4/6/8/10%. `id 1225220`
- Cataclysm [3] — Reduces the Mana cost of your Destruction spells by 3/6/10%. `id 17778`
- Aftermath [5] — Increases the initial damage of your Immolate spell by 10/20/30/40/50% and your Conflagrate spell has a 20/40/60/80/100% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec. `id 18119`

**R5**
- Ruin [5] — Increases the critical strike damage bonus of your Destruction spells by 20/40/60/80/100%. `id 17959`
- Shadowburn [1] — 105 mana, 30 yd, 15 sec CD, spell power coeff 0.429; numbers are level 60 with 0 spell power. Instantly blasts the target for 65–74 Shadow damage. If a non-trivial target dies within 8 sec of being hit with Shadowburn, the caster gains a Soul Shard. `id 17877`

**R6**
- Intensity [3] — Gives your Destruction spells a 23/47/70% chance to not lose casting time when you take damage. `id 18135`
- Agonizing Flames [3] — Increases the critical strike chance of your Searing Pain spell by 3/7/10% and the damage done by all your Destruction spells by 3/7/10%. `id 17927`
- Conflagrate [1] — 100 mana, 30 yd, 10 sec CD, spell power coeff 0.429; numbers are level 60 with 0 spell power. Ignites a target that is already afflicted by your Immolate spell, dealing 87–112 Fire damage and consuming your Immolate effect. `id 1293817`

**R7**
- Pyroclasm [2] — Gives your Soul Fire spell a 13/26% chance to Stun the target for 3 sec, and your Rain of Fire and Hellfire spells a 13/26% chance over their duration to Stun targets they damage for 3 sec. *(requires Intensity)* `id 18073`
- Bane of Havoc [1] — 5% of base mana, 30 yd. Afflicts the target for 5 min, causing 15% of all damage done by the Warlock to other targets to also be dealt to the cursed target. Bane of Havoc is limited to 1 target, and only one Bane per Warlock can be active on any one target. `id 1225228`
- Fire and Brimstone [3] — Increases the critical strike chance of your Conflagrate spell by 8/17/25%. *(requires Conflagrate)* `id 412751`

**R8**
- Shadow and Flame [5] — Hitting an enemy with Conflagrate increases all Shadow damage you deal by 4/8/12/16/20% for 20 sec, and hitting an enemy with Shadowburn increases all Fire damage you deal by 4/8/12/16/20% for 20 sec. In addition, Conflagrate has a 20/40/60/80/100% chance not to consume Immolate, and Shadowburn has a 20/40/60/80/100% chance to instantly refund a Soul Shard. `id 426316`

**R9**
- Incinerate [1] — 205 mana, 30 yd, 2.5 sec cast, spell power coeff 0.714; numbers are level 60 with 0 spell power. Deals 99–115 Fire damage to your target and an additional 25% damage if the target is afflicted by Immolate. *(requires Bane of Havoc)* `id 412758`

<!-- /overrides -->

## Affliction (17 talents)

**R1**
- Improved Life Tap [2] — Increases the amount of Mana awarded by your Life Tap spell by 10%.
- Suppression [5] — Improves your chance to hit by 1% and reduces all threat you generate by 4%.
- Improved Corruption [5] — Reduces the casting time of your Corruption spell by 0.4 sec and increases the damage it deals by 2%.

**R2**
- Grim Reach [2] — Increases the range of your Affliction spells by 10%.
- Soul Harvest [2] — Killing a non-trivial target afflicted by your Drain Soul increases your Mana regeneration by 50% for 10 sec and allows 50% of normal Mana regeneration to continue while casting.
- Improved Drains [3] — Increases health drained or damage done by your Drain Life, Drain Soul, and Wrack spells by 7%.

**R3**
- Improved Bane of Agony [2] — Increases the damage done by your Bane of Agony by 5%.
- Fel Concentration [3] — Gives you a 23% chance to avoid interruption caused by damage while channeling or casting your Drain Life, Drain Mana, Drain Soul, or Wrack spells.
- Amplify Curse [1] — Instant | 3 min cooldown | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec.
- Pandemic [3] — Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 33%.

**R4**
- Malevolence [5] — Increases the critical effect chance of your Shadow spells by 1%.
- Nightfall [2] — Gives your Corruption, Drain Soul, Drain Life, and Wrack spells a 2% chance to cause you to enter a Shadow Trance after damaging the opponent. The Shadow Trance reduces the casting time of your next Shadow Bolt spell by 100%.
- Curse of Exhaustion [1] *(requires {id:warlock-affliction-amplify-curse,rank:1})* — 8% of base mana | 30 yd range | Instant | Reduces the target's movement speed by 30% for 12 sec. Only one Curse per Warlock can be active on any one target.

**R5**
- Siphon Life [1] — 150 Mana | 30 yd range | Instant | Transfers 11 health from the target to the caster every 3 sec. Lasts 30 sec.
- Soul Siphon [3] — Increases the damage done or health drained by your Drain Life, Drain Soul, and Wrack spells by 4% per each of your other Affliction effects active on the target, up to a maximum increase of 12%.

**R6**
- Shadow Mastery [5] — Increases the damage dealt or life drained by your Shadow spells by 2%.

**R7**
- Wrack [1] *(requires {id:warlock-affliction-siphon-life,rank:1})* — 200 Mana | 30 yd range | Channeled | Tears the target apart from within, inflicting 36 Shadow damage every 1 sec and increasing the damage they take from your other Shadow damage over time effects by 10% for 6 sec.

## Demonology (19 talents)

**R1**
- Improved Health Funnel [2] — Increases the amount of health transferred by your Health Funnel spell by 20%, reduces its health cost by 15%, and reduces all threat your Health Funnel generates by 50%. Allows Health Funnel to be used regardless of your demon's health.
- Improved Imp [3] — Increases the damage of your Imp's Firebolt spell by 10% and the effect of its Fire Shield spell by 10%.
- Demonic Embrace [5] — Increases your total Stamina by 3%.
- Unholy Power [5] — Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 2%.

**R2**
- Demonic Aegis [2] — Increases the effectiveness of your Demon Skin and Demon Armor spells by 15%.
- Improved Voidwalker [3] — Increases the effectiveness of your Voidwalker's Torment, Consume Shadows, Sacrifice, and Suffering spells by 10%.
- Fel Vitality [3] — Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 5%, and increases your maximum Mana by 5%.
- Demonic Energies [2] — You heal your pet for 8% of all spell damage you deal. When you gain Mana from Life Tap, your summoned demon gains 50% of the Mana you gain.

**R3**
- Improved Sayaad [3] — Increases the effect of your Succubus' and Incubus' Lash of Pain and Soothing Kiss spells by 10%, and increases the duration of your Succubus' and Incubus' Seduction and Lesser Invisibility spells by 10%.
- Demonic Sacrifice [1] — 100 yd range | Instant | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned. | Imp: Increases your Shadow damage by 15%. | Voidwalker: Restores 2% of your total Mana every 4 sec. | Succubus/Incubus: Increases your Fire damage by 15%. | Felhunter: Restores 3% of your total Health every 4 sec.
- Master Summoner [2] — Reduces the casting time of your Imp, Voidwalker, Succubus, Incubus, and Felhunter Summoning spells by 2 sec and the Mana cost by 20%.

**R4**
- Decimation [2] — Reduces the cooldown of your Soul Fire spell by 45%. When you cast Shadow Bolt or Searing Pain on an enemy below 35% health, they deal 3% increased damage, and for the next 10 sec your Soul Fire spell has its cast time reduced by 20% and costs no Soul Shards.
- Fel Domination [1] — Instant | 5 min cooldown | Your next Imp, Voidwalker, Succubus, Incubus, or Felhunter Summon spell has its casting time reduced by 5.5 sec and its Mana cost reduced by 50%.
- Demonic Brand [3] — Your Searing Pain generates 17% less threat and brands the target for 10 sec. Your pet's next 2 attacks against the target deal 65 to 68 Fire or Shadow damage based on the pet. If Shadow damage is dealt, it has high threat.

**R5**
- Improved Felhunter [3] — Increases the Attack Power reduction of your Felhunter's Tainted Blood, the healing of its Devour Magic, and the detection level of its Paranoia by 10%, and reduces the cooldown of its Spell Lock by 2 sec.
- Soul Link [1] — 20% of base mana | 100 yd range | Instant | When active, 30% of all damage taken by the caster is taken by your Imp, Voidwalker, Succubus, Incubus, or Felhunter Demon instead. In addition, both the Demon and the master will inflict 3% more damage. Lasts as long as the Demon is active.
- Demonic Knowledge [3] — Increases your spell damage and your Demon pet's spell damage by up to 33% of your level while you have a summoned Demon pet active.

**R6**
- Master Demonologist [5] — Grants both the Warlock and the summoned demon an effect as long as that demon is active. | Imp - Increases Fire damage done by 2%. | Voidwalker - Reduces Physical damage taken by 2%. | Succubus/Incubus - Increases Shadow damage done by 2%. | Felhunter - Reduces Magic damage taken by 2%.

**R7**
- Demonic Pact [1] — Your Demonic Sacrifice effect is no longer cancelled by summoning a different Demon pet. Resummoning the sacrificed pet will still cancel the effect.

## Destruction (16 talents)

**R1**
- Destructive Reach [2] — Increases the range of your Destruction spells by 10%.
- Improved Shadow Bolt [5] — Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 4% for 12 sec.
- Bane [5] — Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.1 sec and your Soul Fire spell by 0.4 sec.

**R2**
- Molten Skin [5] — Reduces all damage taken by 2%.
- Cataclysm [3] — Reduces the Mana cost of your Destruction spells by 3%.
- Aftermath [5] — Increases the initial damage of your Immolate spell by 10% and your Conflagrate spell has a 20% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec.

**R3**
- Ruin [5] — Increases the critical strike damage bonus of your Destruction spells by 20%.
- Shadowburn [1] — 105 Mana | 30 yd range | Instant | 15 sec cooldown | Reagents: Soul Shard | Instantly blasts the target for 65 to 73 Shadow damage. If a non-trivial target dies within 8 sec of being hit with Shadowburn, the caster gains a Soul Shard.

**R4**
- Intensity [3] — Gives you a 23% chance to resist interruption caused by damage while casting or channeling any Destruction spell.
- Agonizing Flames [3] — Increases the critical strike chance of your Searing Pain spell by 3% and the damage done by all your Destruction spells by 3%.
- Conflagrate [1] — 100 Mana | 30 yd range | Instant | 10 sec cooldown | Ignites a target that is already afflicted by your Immolate spell, dealing 88 to 110 Fire damage and consuming your Immolate effect.

**R5**
- Pyroclasm [2] — Gives your Soul Fire spell a 13% chance to Stun the target for 3 sec, and your Rain of Fire and Hellfire spells a 13% chance over their duration to Stun targets they damage for 3 sec.
- Bane of Havoc [1] — 5% of base mana | 30 yd range | Instant | Afflicts the target for 5 min, causing 15% of all damage done by the Warlock to other targets to also be dealt to the cursed target. Bane of Havoc is limited to 1 target, and only one Bane per Warlock can be active on any one target.
- Fire and Brimstone [3] — Increases the critical strike chance of your Conflagrate spell by 8%.

**R6**
- Shadow and Flame [5] — Hitting an enemy with Conflagrate increases all Shadow damage you deal by 2% for 20 sec, and hitting an enemy with Shadowburn increases all Fire damage you deal by 2% for 20 sec. In addition, Conflagrate has a 20% chance not to consume Immolate, and Shadowburn has a 20% chance to instantly refund a Soul Shard.

**R7**
- Incinerate [1] — 205 Mana | 30 yd range | 2.5 sec cast | Deals 99 to 113 Fire damage to your target and an additional 25% damage if the target is afflicted by Immolate.
