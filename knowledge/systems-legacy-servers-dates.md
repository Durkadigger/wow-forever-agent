# WoW Forever — Legacy, Servers, Camping, Dates
Data as of: 2026-11-07 b:1.60.1.70862 for the Legacy and Camping sections (datamined; the Legacy tree is identical to b:1.60.1.70634, every rank value unchanged since b:1.60.1.69913). Key dates, Realmless servers and World content refreshed 2026-11-04 from Blizzard posts and news. All other sections: 2026-09-15 b:blizzcon-demo (12 Sept 2026 captures).
Provenance tags: `[T<tier> <source-id> <date> b:<build>]`, see docs/sop-provenance.md and sources.md. Build labels in data/builds.json.

## Key dates (Blizzard official)
*Provenance: [T1 blizz-news 2026-09-12; T1 bnet-shop 2026-09-15]. Where two official sources disagree both are listed.*
- Reveal: 12 Sept 2026 (BlizzCon)
- Live Q&A: Thu 17 Sept 2026, 10:00 a.m. PDT modern WoW segment, **10:30 a.m. PDT WoW Forever segment**, Warcraft Twitch/YouTube (VOD after) [T1 blizz-news 2026-09-15]
- Beta start clock time: **not published**. Blizzard says only "begins September 17, 2026, PST" [T1 blizz-news 2026-09-12] and the Q&A article gives no beta time [T1 blizz-news 2026-09-15]. "Servers open after the Forever Q&A" is fan-site inference only [T5 secondhand 2026-09-16].
- **Beta ended Fri 23 Oct 2026, 10:00 a.m. PDT** ("The WoW Forever Beta will end 24 hours from now, at 10:00 a.m. PDT on Friday, October 23" [T1 blizz-forum 2026-10-22]; "The WoW Forever Beta is now closed", five weeks of testing [T1 blizz-forum 2026-10-23]). This settles the 21 vs 22 Oct question: neither was the shutdown day. A stress test on production regional hardware ran 21 Oct, 2:00–6:00 p.m. PDT in the Americas; its characters and names were wiped and the beta reopened afterwards [T1 blizz-forum 2026-10-20]. All beta progress is wiped.
- Beta end, third official wording: "available through October 21, the last full day of testing" [T1 blizz-news 2026-09-17] (article 24304160). Reads as 21 Oct last full day, shutdown on the 22nd, which would reconcile the two dates above; Blizzard has not said so outright.
- **Launch: Wed 4 Nov 2026, 3:00 p.m. PST, simultaneously in all regions** (1:00 p.m. HST, 4:00 p.m. Denver, 6:00 p.m. EST Montreal; 10:00 a.m. Sydney and 12:00 noon Wellington on 5 Nov) [T1 blizz-forum 2026-11-04] (Kaivax, "World of Warcraft: Forever Launch Time", posted 4 Nov). Matches the 4 Nov date and 3 p.m. PST already recorded [T1 blizz-news 2026-10-22].
- **"World of Warcraft: Forever Now Live!"** news article (24315820), shown on the news page on 4 Nov [T1 blizz-news 2026-11-04]; the matching forum thread carries a created_at of 29 Oct 2026 [T1 blizz-forum 2026-10-29], so the forum timestamp and the 4 Nov article date disagree: both recorded. Content: four rulesets at launch (Normal, PvP, Roleplay, Roleplay PvP), Hardcore "sometime after launch", Classic or Enhanced preset at first login, nine five-player dungeons, and three raids opening 9 Dec (Barrow Deeps, Hyjal Summit, Onyxia's Lair) [T1 blizz-news 2026-11-04]. Access is included with an active subscription or Game Time; Skyborne needs the Skyborne Heroic Pack or higher [T1 blizz-news 2026-10-29] ("Return to Azeroth in World of Warcraft: Forever", article 24315643).
- No server outage, queue or launch-day issue was found in Blizzard posts as of the 4 Nov refresh: the news page lists no status post, and the 30 Oct hotfix article covers retail and other Classic lines, not Forever [T1 blizz-hotfix 2026-11-04]. The Battle.net shop needs a login and was not checked; no price or pack content is restated here.
- 27 Oct name-check fix: the restricted-name list was overly restrictive (for example names containing "con") and was fixed with the next realm restarts [T1 blizz-forum 2026-10-28].
- Beta week 1: level cap 20, "later increased to 30". Testable: Skyborne, Zephras Isle, The Hall of Thanes (13–18), Ruins of Lordaeron (15–20), all zone content to 20. More zones, dungeons and the new battleground open as the beta continues. Server Slam planned, dates not announced. Invites roll out through the test. [T1 blizz-news 2026-09-17] (article 24304160)
- Level cap was still 20 as of 25 Sept 2026 (superseded 1 Oct, see below): The maintainer's level-20 Paladin held 167/23,200 XP unchanged across 202 fights and `PLAYER_XP_UPDATE` never fired, so the cap stops XP gain outright rather than banking it. [T2 in-game 2026-09-25 b:1.60.1.70009]
- **Level cap raised to 30 in the beta build of 1–2 Oct 2026**: "Players can now level up to a maximum of level 30." [T1 blizz-forum 2026-10-01] (Kaivax, Beta Development Notes, topic 2360696). The 1 Oct announcement post said the beta would go offline the next morning PDT and resume with the cap at 30 [T1 blizz-forum 2026-10-01]. Razorfen Downs (25+) and Uldaman (30+) opened the same day; Excavation Site: Wetlands opened as a new dungeon, City of Dalaran opened 8 Oct [T1 blizz-forum 2026-10-01; T1 blizz-forum 2026-10-08]. Question 7 resolved.
- Earlier report, superseded: cap raise to 30 "after a couple of weeks" in a developer interview, with no date given; the raise is also reported to unlock Excavation Site (24–29) and City of Dalaran (28–33). Reported only, not announced by Blizzard: [T5 press-icyveins 2026-09-23]. The cap-30 plan itself is official [T1 blizz-news 2026-09-17]; the timing and the two extra zones are not. Watch the beta forum for the announcement; tracked as question 7 in `knowledge/INDEX.md`.
- Beta participants: community veterans, press, fansites, friends and family, plus pack owners and opt-ins. [T1 blizz-news 2026-09-18] (WoW Weekly, article 24304074)
- Invite-A-Friend codes emailed from 20 Oct 2026
- Early Name Reservation: 27 Oct – 3 Nov 2026, any upgrade purchase, up to 3 characters, first-come [T1 blizz-news 2026-10-20] (article 24303866). Character creation and the ruleset choice opened Tue 27 Oct [T1 blizz-forum 2026-10-23]. Known bug 27 Oct: Oceanic players on Australian servers must create Roleplay or Roleplay-PvP characters before any Normal or PvP one, or those rulesets disappear for later characters; Blizzard is fixing it [T1 blizz-forum 2026-10-27].
- Launch: Wed 4 Nov 2026, 3:00 p.m. PST [T1 bnet-shop 2026-09-15]. The October Blizzard posts and news pages say "November 4" with no clock time [T1 blizz-forum 2026-10-23; T1 blizz-news 2026-10-22]; the shop page needs a login and could not be re-fetched on 27 Oct, so the time of day is not re-verified.
- Invite-A-Friend launch window: 4–11 Nov 2026 (no sub needed)
- New raids unlock: 9 Dec 2026 [T1 blizz-news 2026-10-20] (article 24303009): The Barrow Deeps (level 60, 10 players), Hyjal Summit (level 60, 20 players), Onyxia's Lair (level 60, 40 players; Drakefire Amulet attunement: Horde start with Warlord Goretooth in the Badlands, Alliance with Helendis Riverhorn in the Burning Steppes).
- Hardcore ruleset: after launch (date TBD). Roleplay-PvP ruleset added for launch on 4 Nov [T1 blizz-forum 2026-10-22] (Aggrend); four rulesets at launch: Normal, PvP, Roleplaying, Roleplay-PvP.
- Roadmap: more raids, dungeons, PvP, world content, a revamped iconic raid, 2027 updates

## Editions
*Provenance: [T1 blizz-news 2026-09-12; T1 bnet-shop 2026-09-15]. Where two official sources disagree both are listed.*
- Base game: included with WoW sub or Game Time. No purchase required for launch.
- Skyborne Heroic Pack $29.99: Skyborne race + Zephras Isle, name reservation, Prideclaw mount, transmog, toy, 1 invite code. Housing decor is modern-WoW only.
- Skyborne Epic Pack $59.99: Heroic + beta access + 30 days Game Time (from 4 Nov) + bear mount, transmog, tabards, pets + 3 invite codes total.
- Warcraft Forever Collection $79.99: Epic + Warcraft III: Reforged (full game) + the Forsaken Kingdom campaign. Limited-time, through 11 Jan 2027 [T1 blizz-news 2026-09-12].
  - Forsaken Kingdom is a campaign expansion, not a standalone game: "requires Warcraft III: Reforged to play" [T1 blizz-news 2026-09-12] (news.blizzard.com article 24302499). Sold separately on the shop; reported standalone price $29.99, or $49.99 bundled with Reforged [T5 secondhand 2026-09-13] — shop page needs login, not verified.
- Collector's Edition: Collection code + statue, mousepad, prints, pins, journal.

## Realmless servers
*Provenance: [T1 blizz-news 2026-09-12; T3 cwf 2026-09-13 b:blizzcon-demo].*
- No realm list. Choose a ruleset: Normal, PvP, Roleplaying; Hardcore later as a closed ecosystem.
- Each ruleset is a large ecosystem, not one global mega-server. No cross-ruleset grouping. Horde and Alliance cannot group.
- PvP ruleset has SoD-style faction balance controls (creation locks for the over-represented faction); thresholds unpublished.
- Two-part character names, unique per region. Language preference and "Familiar Faces" system to keep community feel.
- Chat commands take the full two-part name with the space: `/invite Firstname Lastname` worked; the friends-list invite did not. [T2 in-game 2026-09-17 b:1.60.1.69893] (one invite)
- Beta known issue: character friends list disabled; invite by name or by portrait instead. Still listed on 18 Sept. [T1 blizz-forum 2026-09-18] (Kaivax, Beta Known Issues Sept 18, topic 2352687)
- Other beta known issues, 18 Sept list [T1 blizz-forum 2026-09-18]: character pane hides level/class/titles; Glancing Blow numbers on the character sheet are wrong (caster chance and penalty wrong at all levels; melee chance correct, penalty wrong only against higher-level targets); Legacy hotkey Y opens before level 25 with Lua errors; guild charters can be handed in with no signatures as a workaround; Cooldown Manager incomplete and varies by class; resurrection sickness duration wrong at low levels; Waylaid Crates broken for small-stack items (fixed next build); barber chairs throw a Lua error. Class-specific entries are in the talents files.
- 17 Sept developer Q&A, as recapped by Warcraft Tavern; not yet checked against the VOD, so treat as reported: no GDKP raiding allowed; every raid tier has 10- and 20-player versions with some raids at 40, no flex, no heroic, no cross-faction; new seasonal Honor track, no rated PvP planned; ruleset is chosen per character with no later transfer between Normal/PvP/Roleplay (Hardcore exit excepted); default UI includes a damage meter, cooldown tracker and swing timer; addon API blocks gameplay automation. [T5 secondhand 2026-09-17]
- Hardcore death: character can transfer out to another ruleset (including PvP); nothing flows into Hardcore.
- Choose-your-ruleset rules [T1 blizz-news 2026-10-22] (article 24302070, updated 22 Oct): grouping, dungeons and raids are limited to the same ruleset; battlegrounds may mix rulesets except Hardcore; Horde and Alliance cannot group; no free ruleset switching (make a new character); Collections and Legacy Points are account-wide; **on the PvP ruleset each account can create characters for one faction only**; the account Preferred Online Language setting has a 24 hour cooldown between changes.
- **Unpublished:** whether one account can hold both factions in the Normal and Roleplaying rulesets (the PvP answer is now official, above); guilds, AH, layering details.

## Legacy (account-wide progression)
*Provenance: [T2 wago 2026-10-27 b:1.60.1.70634; T1 blizz-deepdive 2026-09-12]. Every rank of every perk is read from the client (`python scripts/wago_query.py legacy`). Values written a/b/c are ranks 1/2/3. Re-checked 27 Oct: no rank value changed since b:1.60.1.69913; several perks moved one column right (layout only) and Master Chef and Luremaster moved one row left, which Blizzard calls a visual change [T1 blizz-forum 2026-10-16]. All beta players were granted 16 Legacy points on 8 Oct via a completed Legacy Challenge and cheap respecs, beta only [T1 blizz-forum 2026-10-08; T1 blizz-forum 2026-10-01].*
Earn Legacy points via class, profession, and world challenges; spend them in three trees (TraitTree 1187 Professions, 1188 Adventure, 1189 Resourcefulness). The Legacy currency is capped at 16 points in this build, against 69 points of revealed perks (23 per tree), so choices are real. Each tree also holds two placeholder nodes reading "To be added in a future update."

### Adventure
- Well Rested [5] — Rested XP builds 4/8/12/16/20% faster and the rested cap is +4/8/12/16/20%.
- Talented [5] — Talent points start at level 9/8/7/6/5 instead of 10; still capped at 51 total. (requires Well Rested)
- Thrill of Adventure [5] — Killing blow on a non-trivial enemy restores 1/2/3/4/5% of max Health and Mana over 10 sec. Not in dungeons, raids, or battlegrounds.
- Field Guide [3] — Camp feature cooldown −8/17/25%.
- Frequent Flier [1] — Flight paths cost 50% less and fly 20% faster. (requires Field Guide)
- Field Medicine [2] — Recently Bandaged lasts 5/10 sec less. Not in dungeons, raids, or battlegrounds.
- High Alert [2] — Detect Stealth as if 1/2 levels higher. Not in battlegrounds.

### Resourcefulness
- Diplomat [5] — Reputation gains +2/4/6/8/10%.
- Permanence [2] — Long-duration party/raid class buffs and camp rest benefits last 50/100% longer. (requires Gourmand)
- Reagent Economy [1] — Class abilities need no vendor reagents; Tier 1 camping features cost no reagents. (requires The Quick and the Dead) (Shaman: no Ankh purchases)
- Gourmand [3] — Food buffs last 33/67/100% longer.
- For Great Honor [5] — Honor Points +2/4/6/8/10%.
- The Quick and the Dead [2] — +5/10% speed while dead; after resurrection, helpful spells cost nothing for 1/2 min or until combat.
- Reinforce [5] — Durability loss on death −8/16/24/32/40%.

### Professions
- Bartering [2] — Vendor prices −5/10%.
- Working Overtime [5] — Skill-up chance +4/8/12/16/20% on any primary, secondary, or class tradeskill.
- Dedicated Study [1] — 25 sec cast, 23 hr CD: +1 skill to your lowest primary or secondary tradeskill; if all are at 300, gain 2–4 of a random Elemental Essence. (requires Bartering)
- Bountiful Harvest [5] — +20/40/60/80/100% chance to discover Scarce materials from Mining, Herbalism, and Skinning.
- Performance Bonus [3] — Supply-crate turn-ins have a 5/10/15% chance for double Merchant's Favor (Azeroth Commerce Authority / Durotar Supply and Logistics). (requires Bountiful Harvest)
- Luremaster [2] — With a lure active, 25/50% chance to catch an extra fish.
- Master Chef [5] — Cooking has a 10/20/30/40/50% chance to create an extra result.

Superseded on 17 Sept 2026: the demo capture had rank-1 values only, with higher ranks estimated by the fan site. The datamined ranks above match a same-increment-per-point pattern except Field Guide (8/17/25) and Gourmand (33/67/100).

## Quests, respecs and vendors (beta, level-20 cap)
*Provenance: [T2 in-game 2026-09-23 b:1.60.1.69913] — the maintainer's own observation in the live beta client. Profession-table and recipe levels are tagged inline.*
- Quest log holds **40** quests.
- Talent respecs are bought from a class trainer (Garen Largo for Horde Paladins) and the trainer sells **two separate resets, one for class talents and one for Legacy talents**. Each reset's cost escalates with use.
- **Waylaid Crates** return from Season of Discovery. "Waylaid Crate: Apprentice Textiles" accepts **40 Linen or 20 Light Leather**, either bundle alone. Hand in to Durotar Supply and Logistics for the Horde; a filled crate is worth more than an empty one. Turn-ins pay **Merchant's Favor**, which buys profession plans. The Legacy perk Performance Bonus gives a chance of double Merchant's Favor.
- Weapon masters are in their Classic locations and their skill tables look unchanged: Orgrimmar (Hanashi, Sayoc) two-handed axes; Thunder Bluff (Ansekhwa) two-handed maces, which Paladins already start with; Undercity (Archibald) two-handed swords and polearms, level 20, 1 gold.

## Camping
*Provenance: [T1 blizz-deepdive 2026-09-12; T3 cwf 2026-09-13 b:blizzcon-demo]. Rank-1 perk values only.*
- Basic Campfire creates a campsite: rest for buffs, contribute crafted objects, refresh food buffs.
- Up to 3 nearby players each add one object. Professions learn first campsite objects at skill 20; dungeon-boss Blueprints unlock advanced objects.
- Cooking can upgrade camps to 5 or 10 objects. 600+ new recipes; crafted food with XP or stat benefits.
- Campsites offer vendors, repairs, crafting stations, and one-hour buffs (secondary reporting).
- **Adventurer's Tent reworked in client build 1.60.1.70862** [T2 wago 2026-11-07 b:1.60.1.70862]: 10 sec cast, 1 hour cooldown, 8 yd; builds a tent that raises Rested experience for you and party members sitting nearby to 20% of a level (no effect if already above that); requires a Campfire nearby (was: a cosmetic summon that changed the look of Camp Tents [T2 wago 2026-11-04 b:1.60.1.70790]). No staff post describes the change.
- The Quick and the Dead Legacy talent sometimes did not work; fixed [T1 blizz-forum 2026-11-06] (Kaivax, "WoW: Forever Hotfixes - November 6, 2026", https://us.forums.blizzard.com/en/wow/t/wow-forever-hotfixes-november-6-2026/2403040/4).

## Combat and itemization rules (Deep Dive)
*Provenance: [T1 blizz-deepdive 2026-09-12; T3 cwf 2026-09-13 b:blizzcon-demo].*
- Spell, melee, and ranged hit chance are one stat; same for crit. Improves reliability of Taunts, Poisons, Traps.
- No flying, no level scaling. Level cap 60.
- Opt-in transmog. BoP Uncommon/Rare dungeon drops grant appearance to all eligible looters; Epic raid appearances only to the recipient. Same-armor-type rule; level 60 removes level restrictions.
- Classic or modern visual presets; HD/SD models; restored Classic animations for HD; gamepad support.

## World content
*Provenance: [T1 blizz-news 2026-09-12; T3 cwf 2026-09-13 b:blizzcon-demo].*
- New regions: Mount Hyjal (60), Shen'dralas, Riverglades (~35–45, 150+ quests), Zephras Isle (1–12, Skyborne start). 1,000+ new quests across 1–60.
- Nine new dungeons with official level ranges [T1 blizz-forum 2026-09-15] (Kaivax, correcting BlizzCon materials that showed a wrong range for Krol'dok):

| Dungeon | Levels |
|---|---|
| The Hall of Thanes | 13–18 |
| Ruins of Lordaeron | 15–20 |
| Excavation Site: Wetlands | 24–29 |
| City of Dalaran | 28–33 |
| The Drowned City | 35–40 |
| Krol'dok Stronghold | 40–45 |
| Alcaz Prison | 48–53 |
| Blackmaw Hold | 55–60 |
| Shaper's Terrace | 58–60 |

- Raids: Hyjal Summit (20), Barrow Deeps (10), Onyxia's Lair (40); all unlock 9 Dec 2026 [T1 blizz-news 2026-10-20].
- Dungeon ranges, second official wording: the 20 Oct dungeon article repeats the table above [T1 blizz-news 2026-10-20] (article 24301455), but the 1 Oct beta notes list Excavation Site: Wetlands as (26–31) [T1 blizz-forum 2026-10-01]. Two official sources disagree on Excavation Site (24–29 vs 26–31); both recorded. Razorfen Downs is listed as 25+ and Uldaman as 30+ [T1 blizz-forum 2026-10-01].
- PvP numbers in the beta: Honor cap raised from 15,000 to 25,000 and most PvP gear and token costs up about 50% [T1 blizz-forum 2026-10-01]; critical strikes in PvP no longer have reduced efficacy [T1 blizz-forum 2026-10-08]; Marks of Honor stack to 30 (was 20) [T1 blizz-forum 2026-10-16]. Horde characters are attacked on sight in Dalaran city; the Horde sewer-key questline no longer gives open-world access [T1 blizz-forum 2026-10-16].
- Battlegrounds: WSG, AB, AV, plus Darkspear Islands (15v15, control points, AB-style flags).
