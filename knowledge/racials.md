# WoW Forever — Races and Racial Abilities
Data as of: 2026-11-07 b:1.60.1.70862 (first post-launch client build, racial lines unchanged from the launch-day client 1.60.1.70790, wago product wowf; racial lines re-read from it, and the 26-27 Oct staff 'final pass' is now in the client except where noted per line). Race/class matrix, Priest racial spells and anything not tagged T2/T1 below: 2026-09-15 b:blizzcon-demo.
Provenance tags: `[T<tier> <source-id> <date> b:<build>]`, see docs/sop-provenance.md and sources.md. Build labels in data/builds.json.

Sources: Blizzard Deep Dive recap (rule: every race has 2 active + 2 passive racials on a similar offensive budget; Dwarf and Undead detailed officially), Warcraft Tavern BlizzCon floor hands-on (12 Sept 2026), classicwowforever.com racial reference (13 Sept 2026). Values are demo-build and may change in beta. **17 Sept 2026:** racial lines were first re-read from the beta client (`python scripts/wago_query.py racials`); every cooldown is known. **27 Oct 2026:** re-read again from b:1.60.1.70634 and compared with the 1, 8, 16, 26 and 27 Oct staff notes (topic 2360696). **4 Nov 2026 (launch day):** re-read from b:1.60.1.70790 and compared with the Beta Development Notes updated 2 Nov (topic 2360696, post 9, which restates the 26-27 Oct racial notes in one list).

Global changes [T1 blizz-deepdive 2026-09-12]: all +10 resistance racials removed; weapon-skill racials now give crit that applies to spells and abilities while that weapon is equipped; hit and crit are unified across spell/melee/ranged.

## Race / class matrix (56 combos, 28 per faction)
*Provenance: [T1 blizz-deepdive 2026-09-12; T3 cwf 2026-09-13]. Skyborne pack requirement and price: [T1 bnet-shop 2026-09-15].*

| Race | Faction | Classes |
|---|---|---|
| Human | Alliance | Warrior, Paladin, **Hunter (new)**, Rogue, Priest, Mage, Warlock |
| Dwarf | Alliance | Warrior, Paladin, Hunter, Rogue, Priest, **Shaman (new)** |
| Night Elf | Alliance | Warrior, Hunter, Rogue, Priest, Druid |
| Gnome | Alliance | Warrior, Rogue, **Priest (new)**, Mage, Warlock |
| Skyborne (High Order) | Alliance | Warrior, Hunter, Rogue, Mage, Druid |
| Orc | Horde | Warrior, Hunter, Rogue, Shaman, **Mage (new)**, Warlock |
| Undead | Horde | Warrior, **Paladin (new)**, Rogue, Priest, Mage, Warlock |
| Tauren | Horde | Warrior, Hunter, Shaman, Druid |
| Troll | Horde | Warrior, Hunter, Rogue, Priest, Shaman, Mage, **Warlock (new)** |
| Skyborne (Windshaper) | Horde | Warrior, Hunter, Rogue, Shaman, Druid |

Skyborne require the Skyborne Heroic Pack ($29.99) or higher. Skyborne pick faction at creation; faction sets one class (Mage/Alliance, Shaman/Horde) and one racial.

## Horde
*Provenance: [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03]. Every racial below was re-read from b:1.60.1.70790 (4 Nov 2026). The 26-27 Oct "final pass on racials", restated in the 2 Nov development notes, is in that client for every race except the one item flagged per line (Skysight duration). Lines whose tag still names b:1.60.1.70634 did not change in b:1.60.1.70790.*

### Orc
*Provenance: [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-16; T3 wtavern-handson 2026-09-12; T3 cwf 2026-09-13 b:blizzcon-demo; T3 cwf 2026-10-27 b:beta]. Cooldowns: SpellCooldowns table.*
- **Blood Fury** (active) — +10% Attack Power and Spell Power for 15 sec, **2 min CD**. No healing-received penalty in the data. [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] (was: 3 min CD [T2 wago 2026-10-27 b:1.60.1.70634])
  - *Open question (still open): whether this boosts healing.* b:1.60.1.70790 is unchanged on this: three effects (auras 166 melee AP %, 167 ranged AP %, 317 percent Spell Power), no healing-done aura. Other "increases spell power" buffs pair a damage aura with a healing aura. How the server applies aura 317 to healing is not visible in the tables. The 2 Nov notes do not mention healing. Needs an in-game test on the live game. [T2 wago 2026-11-04 b:1.60.1.70790]
- **Shatter Curse** (active, new) — Removes all Curses and Banes (no more immunity) and reduces Magical damage taken by 5% for 8 sec. 3 min CD. [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-16]
- **Savage** (passive) — removed: no longer in the Orc racial skill line. [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] (was: +1% crit with all spells and abilities, no weapon needed [T2 wago 2026-10-27 b:1.60.1.70634])
- **Command** (passive, re-added) — +5% damage dealt by Hunter and Warlock pets (spell ids 20575, 20576, 21563 are back in the client). 6 Nov hotfix: some Warlock pet abilities benefited too much from Command, fixed [T1 blizz-forum 2026-11-06]; the client's second effect on spell 20575 went 5 → 0 while the +5% line stays [T2 wago 2026-11-07 b:1.60.1.70862]. [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03]
- **Hardiness** (passive) — Stuns on you last 20% less. *(Classic: 25% resist chance)* [T2 wago 2026-10-27 b:1.60.1.70634]

### Troll
*Provenance: [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-16; T3 wtavern-handson 2026-09-12; T3 cwf 2026-09-13 b:blizzcon-demo; T3 cwf 2026-10-27 b:beta]. Cooldowns: SpellCooldowns table.*
- **Berserking** (active) — +10% attack and casting speed for 15 sec, 3 min CD. Flat value; no low-health scaling in the data. [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] (was: 10 sec [T2 wago 2026-10-27 b:1.60.1.70634])
- **Rapid Regeneration** (active, new) — Regenerate 50% of max Health over 6 sec, 3 min CD. Any movement, action, or damage taken cancels it. [T2 wago 2026-10-27 b:1.60.1.70634]
- **Regeneration** (passive) — Health regen **+20%**; 20% of regen continues in combat. [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-16]
- **Beast Slaying** (passive) — +5% damage to Beasts. [T2 wago 2026-10-27 b:1.60.1.70634]
- Bow/Throwing Specialization: not in the Troll racial skill line in b:1.60.1.70634. Treat as removed unless a later build adds it. [T2 wago 2026-10-27 b:1.60.1.70634]

### Tauren
*Provenance: [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-16; T3 wtavern-handson 2026-09-12; T3 cwf 2026-09-13 b:blizzcon-demo; T3 cwf 2026-10-27 b:beta]. Cooldowns: SpellCooldowns table.*
- **War Stomp** (active) — Stun up to 5 enemies within 8 yd for 2 sec. 0.5 sec cast, **90 sec CD**. [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-16]
- **Cultivation** (active, new) — Cultivate a nearby herb, growing a duplicate that can be harvested without Herbalism skill. Each herb can be cultivated once. **15 min CD.** [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-16]
- **Plainsrunning** (passive, new) — 5 Nov hotfix: can no longer stack during a battleground's preparation phase, and stacks are cancelled while carrying a flag [T1 blizz-forum 2026-11-06] (hotfix post, 5 Nov section). Speed: **+2% movement speed per 5 sec spent moving, up to +60%; no mounted speed bonus.** Taking damage or standing still reduces it; Blizzard says stutter-stepping no longer keeps it up (a minimum distance per second is required). [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] Works in Bear Form [T3 wtavern-handson 2026-09-12]. (was: +1% per stack, up to +30%, and +3% mounted speed [T2 wago 2026-10-27 b:1.60.1.70634])
- **Endurance** (passive) — **+5% total health only**; no hit or critical-bonus modifier. [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] (was: +5% health and +2% critical strike bonus to damage and healing [T2 wago 2026-10-27 b:1.60.1.70634])

### Undead
*Provenance: [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-16; T1 blizz-deepdive 2026-09-12; T3 wtavern-handson 2026-09-12; T3 cwf 2026-09-13 b:blizzcon-demo; T3 cwf 2026-10-27 b:beta]. Cooldowns: SpellCooldowns table.*
- **Will of the Forsaken** (active) — Removes Charm, Fear and Sleep. 2 min CD. *(Classic 5 sec immunity removed)* [T2 wago 2026-10-27 b:1.60.1.70634] Not available under Scatter Shot [T1 blizz-forum 2026-10-16]; works while asleep or charmed (fixed 8 Oct) [T1 blizz-forum 2026-10-08].
- **Cannibalize** (active) — Humanoid/Undead corpse within 5 yd: 7% of total Health and 7% of total Mana every 2 sec for 10 sec (35% each). 2 min CD. Movement, action or damage cancels it. Per the 2 Nov notes it can once again be used while immune to Physical damage [T1 blizz-forum 2026-11-03] (the datamine cannot show this restriction). [T2 wago 2026-10-27 b:1.60.1.70634] (was: cannot be used while immune to Physical damage [T1 blizz-forum 2026-10-01])
- **Underwater Breathing** (passive) — +300%. [T2 wago 2026-10-27 b:1.60.1.70634]
- **Touch of the Grave** (passive, new) — Spells and attacks have a chance to drain Health from the target, up to 5% of your maximum Health. **20% chance** for Paladins, Rogues and Warriors (id 1260189) and **30%** for casters (id 1260201), **15 sec internal cooldown**; no longer scales with Shadow bonuses and no longer reduced when a lower spell rank is used. [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] (was: 25 sec internal cooldown [T2 wago 2026-10-27 b:1.60.1.70634])
- Priest-only: Dark Sacrifice (720 health → 720 mana over 15 sec, 10 min CD, level 38 rank 2 values).

### Skyborne (Windshaper, Horde)
*Provenance: [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-16; T1 blizz-news 2026-09-12; T3 wtavern-handson 2026-09-12; T3 cwf 2026-09-13 b:blizzcon-demo]. Cooldowns: SpellCooldowns table. Pack requirement: [T1 bnet-shop 2026-09-15].*
- **Walk on Air** (active) — Glide downward for 10 sec with steering. **90 sec CD.** [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-16]
- **Skysight** (active) — **+15% movement and mounted speed** (was +10%), 0.5 sec cast, 2 min CD. At an elemental convergence it also grants "Charged" for 1 hour (+100% to the effect, so +30%) [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03]. **Duration is NOT confirmed as announced:** the 2 Nov notes say 15 sec, but the client's buff (Elemental Blessing, 1259688) still has a 30 sec duration and the tooltip reads "for 30 sec". The 30 sec value stands as the client value; 15 sec is Blizzard's stated intent [T1 blizz-forum 2026-11-03]; client value [T2 wago 2026-11-04 b:1.60.1.70790]. Charged persists through death and is removed on entering a raid [T1 blizz-forum 2026-11-03] (not visible in the tables). (was: +10%, 30 sec with no convergence, 15 min if one is found [T2 wago 2026-10-27 b:1.60.1.70634])
- **Wind Blessed** (passive) — **+2%** melee, ranged, and spell haste. [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] (was: +3% [T2 wago 2026-10-27 b:1.60.1.70634])
- **Elemental Insight** (passive) — +5% damage to Elementals. [T2 wago 2026-10-27 b:1.60.1.70634]

## Alliance

### Human
*Provenance: [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-16; T3 wtavern-handson 2026-09-12; T3 cwf 2026-09-13 b:blizzcon-demo]. Cooldowns: SpellCooldowns table.*
- **Will to Survive** (active, new) — Removes all Stun effects. 3 min CD. [T2 wago 2026-10-27 b:1.60.1.70634]
- **Perception** (active) — Stealth detection for 20 sec. 3 min CD. [T2 wago 2026-10-27 b:1.60.1.70634]
- **Ruthless** (passive) — +1% crit with all spells and attacks, no weapon needed. [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] (was: +2% [T2 wago 2026-10-27 b:1.60.1.70634])
- **The Human Spirit** (passive) — +10% Spirit. [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] (was: +5% [T2 wago 2026-10-27 b:1.60.1.70634])
- Diplomacy, Mace Specialization: not in the Human racial skill line in b:1.60.1.70634. (A Legacy perk named Diplomat gives reputation gains to any race; see the systems file.) [T2 wago 2026-10-27 b:1.60.1.70634]
- Priest-only: Divine Grace (removes Weakened Soul and heals).

### Dwarf
*Provenance: [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-16; T1 blizz-deepdive 2026-09-12; T3 wtavern-handson 2026-09-12; T3 cwf 2026-09-13 b:blizzcon-demo]. Cooldowns: SpellCooldowns table.*
- **Stoneform** (active) — Removes and grants immunity to Bleed, Poison, and Disease, and reduces Physical damage taken by 10%, for 8 sec. 3 min CD. [T2 wago 2026-10-27 b:1.60.1.70634]
- **Find Treasure** (active) — Treasure on minimap, and a chance for additional items in most chests. [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-16]
- **Artisan's Precision** (passive, replaces Earth Fury) — +1% chance to hit with all spells and attacks (spell id 1259719; the auras changed from the two critical-bonus auras to hit auras 54 and 55). [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03] (was: Earth Fury, +2% critical strike bonus to damage and healing [T2 wago 2026-10-27 b:1.60.1.70634])
- **Big Game Hunter** (passive, new) — +5% damage to Beasts. [T2 wago 2026-10-27 b:1.60.1.70634]
- Priest-only: Chastise (Holy damage + root), Desperate Prayer.

### Night Elf
*Provenance: [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-16; T3 wtavern-handson 2026-09-12; T3 cwf 2026-09-13 b:blizzcon-demo]. Cooldowns: SpellCooldowns table.*
- **Elune's Light** (active, new) — +10% crit with all spells and attacks for 15 sec. 3 min CD. [T2 wago 2026-10-27 b:1.60.1.70634]
- **Shadowmeld** (active) — Stealth while immobile, 10 sec CD. Used in combat it discourages enemies from attacking you, but the cooldown becomes 2 min. [T2 wago 2026-10-27 b:1.60.1.70634]
- **Quickness** (passive) — +1% dodge, +2% movement speed (now stacks with other movement speed increases); Night Elf Rogues and Druids are 1 level harder to detect in Stealth. [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-16]
- **Wisp Spirit** (passive) — +75% speed while dead; shields no longer show in Wisp Form. [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-16]
- Priest-only: Elune's Grace (melee/ranged hit against you −50% for 15 sec or 3 misses), Starshards.
  - Beta known issue: Starshards does not benefit from the Twilight Focus talent. Announced: fixed in the next beta build. [T1 blizz-forum 2026-09-18] (Kaivax, Beta Known Issues Sept 18, topic 2352687)

### Gnome
*Provenance: [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-16; T3 wtavern-handson 2026-09-12; T3 cwf 2026-09-13 b:blizzcon-demo]. Cooldowns: SpellCooldowns table.*
- **Eureka!** (active, new) — An **8 sec buff with no charges**: your non-periodic damaging abilities (for the healer version, damaging or healing) deal 10% more damage/healing and cost 10% less Mana, Rage, or Energy. Channeled spells do not count as periodic. Now also boosts Power Word: Shield; cannot be used while stealthed or invisible. 2 min CD. [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-16]
- **Escape Artist** (active) — Escape movement-impairing effects and become immune to them for 3 sec. 2 min CD. [T2 wago 2026-10-27 b:1.60.1.70634]
- **Expansive Mind** (passive) — +5% max Mana, Rage, or Energy. [T2 wago 2026-10-27 b:1.60.1.70634]
- **Engineering Specialization** (passive) — Engineering devices fail or backfire 20% less often (no skill points). [T2 wago 2026-10-27 b:1.60.1.70634]
- Priest-only: Confounding Flash (AoE CC), Contingency Plan (death prevention + heal).

### Skyborne (High Order, Alliance)
*Provenance: [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-16; T1 blizz-news 2026-09-12; T3 wtavern-handson 2026-09-12; T3 cwf 2026-09-13 b:blizzcon-demo]. Cooldowns: SpellCooldowns table. Pack requirement: [T1 bnet-shop 2026-09-15].*
- Walk on Air, Wind Blessed, Elemental Insight as above.
- **Read Leyline** (active; the 25 Sept client called it Read Ley Line) — **+50% Health and Mana regeneration for 15 sec**, 0.5 sec cast, 2 min CD. At a Ley Line it also grants "Attuned" for 1 hour (+100% to the effect, so +100% regeneration) [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03]. Cannot be used while Innervate is active; Attuned persists through death and is removed on entering a raid [T1 blizz-forum 2026-11-03] (not visible in the tables). (was: +100% regeneration, 30 sec with no leyline nearby, 15 min if one is found, 2 sec cast [T2 wago 2026-10-27 b:1.60.1.70634])

## Priest racial spells
*Provenance: [T3 cwf 2026-09-13 b:blizzcon-demo]. Which spells survive in Forever is unconfirmed until a T1/T2 source lists them.*
Warcraft Tavern reports Fear Ward is baseline for all Priests. Troll Priest spells not yet documented.

## Maintainer's working conclusions (Horde, 14–15 Sept 2026)
- Shaman DPS: Orc > Troll > Tauren (hit) > Skyborne.
- Shaman Resto: Troll (Berserking + regen) > Orc (if Blood Fury boosts healing; axe crit feeds Water Shield) > Tauren (PvP).
- Mage: Troll PvE, Orc PvP. Rogue: Orc, Undead for PvP. Warlock: Orc, Troll as mana-efficiency alt.

### Data note for the conclusions above (17 Sept 2026; the maintainer's rankings are unchanged)
- Berserking is a flat +10% haste for 10 sec on a 3 min CD; Blood Fury is +10% for 15 sec on a 2 min CD. [T2 wago 2026-09-18 b:1.60.1.69913] (Blood Fury's cooldown has since changed; see the 27 Oct note below.)
- Whether Blood Fury reaches healing is still open (see Orc). Until it is tested in game, Troll over Orc for Resto stands on the data.

### Data note, 7 Nov 2026 (client build 1.60.1.70862; facts only)
- No racial tooltip or value changed between b:1.60.1.70790 and b:1.60.1.70862 apart from the Orc Command fix above [T2 wago 2026-11-07 b:1.60.1.70862]. Night Elf Shadowmeld no longer grants Druids Ravage and Pounce [T1 blizz-forum 2026-11-06] (Alliance; comparison only).

### Data note, 4 Nov 2026 (launch day; the maintainer's rankings are unchanged; facts only)
- In the launch client (b:1.60.1.70790) Berserking is +10% haste for **15 sec** on 3 min; Blood Fury is +10% Attack Power and Spell Power for 15 sec on **2 min**. [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03]
- Orc's +1% crit (Savage) is gone and Command (+5% Warlock and Hunter pet damage) is back. The Orc crit that the maintainer's note ties to Water Shield no longer exists. [T2 wago 2026-11-04 b:1.60.1.70790; T1 blizz-forum 2026-11-03]
- Whether Blood Fury reaches healing is still open: b:1.60.1.70790 has the same three auras (166, 167, 317) and no healing-done aura. Needs an in-game test now that the game is live. Until then, Troll over Orc for Resto stands on the data. [T2 wago 2026-11-04 b:1.60.1.70790]

### Data note, 27 Oct 2026 (the maintainer's rankings are unchanged; facts only)
- In the newest client (b:1.60.1.70634) Berserking is +10% haste for 10 sec on 3 min; Blood Fury is +10% for 15 sec on **3 min** (it was 2 min until the 16 Oct build). [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-forum 2026-10-16]
- (Superseded by the 4 Nov note above: all of this is now in b:1.60.1.70790.) Announced for launch, not in the client yet at that date: Blood Fury back to 2 min, Berserking lengthened to 15 sec (so 15 sec on 3 min against Blood Fury's 15 sec on 2 min), Orc's +1% crit (Savage) removed. [T1 blizz-forum 2026-10-26; T1 blizz-forum 2026-10-27]
- Whether Blood Fury reaches healing is still open (see Orc); no post or datamine settles it. Until it is tested in game, Troll over Orc for Resto stands on the data.
- The Orc crit that the maintainer's note ties to Water Shield was an axe-only bonus until 16 Oct, then unconditional (Savage, +1%), and is announced for removal. Water Shield itself now also triggers on any critical spell, not only critical heals (see `talents-shaman.md`). [T1 blizz-forum 2026-10-16; T1 blizz-forum 2026-10-26; T2 wago 2026-10-27 b:1.60.1.70634]
