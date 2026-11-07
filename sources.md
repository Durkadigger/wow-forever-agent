# Sources

How to cite any of these inside `knowledge/`: see `docs/sop-provenance.md`. Every tag uses the **source-id** column below.

## Tier 1 — Blizzard official

| source-id | What | Where | Read by |
|---|---|---|---|
| `blizz-news` | News posts, patch notes, recaps | https://worldofwarcraft.blizzard.com/en-us/news (filter "Forever"). Key posts: What's Next https://worldofwarcraft.blizzard.com/en-us/news/24303862 · Deep Dive https://worldofwarcraft.blizzard.com/en-us/news/24303313 · Upgrades/beta https://worldofwarcraft.blizzard.com/en-us/news/24301508 | refresh step 3 |
| `blizz-deepdive` | The BlizzCon Deep Dive recap specifically (racial rules, class changes) | https://worldofwarcraft.blizzard.com/en-us/news/24303313 | refresh step 3 |
| `blizz-forum` | Staff posts on the official forums. WoW: Forever category id **346** (subcategories 347, 348) plus **349** WoW: Forever Beta Discussion (opened 17 Sept 2026; known-issues posts: https://us.forums.blizzard.com/en/wow/c/in-development/wow-forever-beta-discussion/349). Staff feed: https://us.forums.blizzard.com/en/wow/groups/blizzard-tracker/posts.json | https://us.forums.blizzard.com/en/wow/c/wow-forever/346 | `scripts/forum_scan.py` |
| `blizz-hotfix` | Hotfix notes (post-launch these change numbers before patch notes do) | https://worldofwarcraft.blizzard.com/en-us/news (title "Hotfixes") and the Support hotfix article | refresh step 3 |
| `blizz-launcher` | Beta/PTR build notes shown only in the Battle.net client | The maintainer pastes them in on patch days | manual |
| `blizz-video` | Developer Q&A, interviews on Warcraft Twitch/YouTube. Q&A 17 Sept 2026 10:00 PDT | https://www.twitch.tv/warcraft · https://www.youtube.com/@Warcraft | manual, VOD timestamps |
| `bnet-shop` | Editions, prices, pack contents, dates on the shop page | https://us.shop.battle.net/en-us/product/world-of-warcraft-forever | refresh step 3; always before restating a price |

BlizzCon 2026 panel VODs (indexed from Kaivax's sticky thread, 12–15 Sept 2026):

| source-id | Panel | Where | Note |
|---|---|---|---|
| `blizz-video` | World of Warcraft: Forever – New Horizons – Cinematic Trailer | https://youtu.be/xXaXYxcbA6A | VOD, from staff sticky https://us.forums.blizzard.com/en/wow/t/world-of-warcraft-forever-revealed-at-blizzcon-2026/2347170 |
| `blizz-video` | World of Warcraft: Forever – Gameplay Trailer | https://youtu.be/uQuKE0KDgiM | VOD, from staff sticky https://us.forums.blizzard.com/en/wow/t/world-of-warcraft-forever-revealed-at-blizzcon-2026/2347170 |
| `blizz-video` | Warcraft Forever Collection Trailer | https://youtu.be/OQrvLbiLXcU | VOD, from staff sticky https://us.forums.blizzard.com/en/wow/t/world-of-warcraft-forever-revealed-at-blizzcon-2026/2347170 |
| `blizz-video` | World of Warcraft: Forever - What's Next Panel – BlizzCon 2026 | https://youtu.be/OEX-i55We5c | VOD, from staff sticky https://us.forums.blizzard.com/en/wow/t/world-of-warcraft-forever-revealed-at-blizzcon-2026/2347170 |
| `blizz-video` | World of Warcraft: Forever - Creator Showcase – BlizzCon 2026 | https://youtu.be/e0B4Bw3ehHA | VOD, from staff sticky https://us.forums.blizzard.com/en/wow/t/world-of-warcraft-forever-revealed-at-blizzcon-2026/2347170 |
| `blizz-video` | World of Warcraft: Forever - Deep Dive – BlizzCon 2026 | https://youtu.be/nQPS_QSOYCU | VOD, from staff sticky https://us.forums.blizzard.com/en/wow/t/world-of-warcraft-forever-revealed-at-blizzcon-2026/2347170 |
| `blizz-video` | World of Warcraft: Forever - Evolving a Timeless World – BlizzCon 2026 | https://youtu.be/bsg2HmvLT-A | VOD, from staff sticky https://us.forums.blizzard.com/en/wow/t/world-of-warcraft-forever-revealed-at-blizzcon-2026/2347170 |
| `blizz-video` | World of Warcraft: Forever - Found Photographs – BlizzCon 2026 | https://youtu.be/wDfA_S7fXOc | VOD, from staff sticky https://us.forums.blizzard.com/en/wow/t/world-of-warcraft-forever-revealed-at-blizzcon-2026/2347170 |
| `blizz-video` | World of Warcraft: Hardcore Panel – BlizzCon 2026 | https://youtu.be/Gzo6t7xmK0Q | VOD, from staff sticky https://us.forums.blizzard.com/en/wow/t/world-of-warcraft-forever-revealed-at-blizzcon-2026/2347170 |

Forum rule: only accounts in the Blizzard staff group count as T1. Everything else on the forums is T5.

## Tier 2 — Datamined from the client

| source-id | What | Where | Read by |
|---|---|---|---|
| `wago` | Raw DB2 tables per build (Spell, SpellEffect, Talent, ChrRaces, SpellCooldowns…). The most authoritative datamine; Wowhead builds from the same data. | https://wago.tools/db2 · build list https://wago.tools/api/builds | `scripts/wago_diff.py` |
| `wowhead-forever` | Wowhead's Forever database and datamining news | https://www.wowhead.com/forever | refresh step 4 |
| `in-game` | a guild member's own observation in the live client (a stat read, a tooltip, a chat command that worked, a combat-log measurement). Tier 2 is proposed and pending the maintainer's confirmation (see `docs/ingame-test-plan.md`); the tag's note states the method and sample size. | the running client, build in the tag | `scripts/read_addon_data.py`, `addon/README.md` test card |
| `wtavern-datamine` | Warcraft Tavern datamining articles | https://www.warcrafttavern.com/forever/ | refresh step 4 |

Wago product slug for Forever: **`wowf`** from 13 Oct 2026 (probe of 1.60.1.70634 on 27 Oct: Skyborne race, Shatter Curse, Well Rested, Plainsrunning, Bountiful Harvest all present; builds 70245, 70532, 70630, 70634). The beta slug **`wow_classic_beta`** was confirmed 17 Sept 2026 by probe of build 1.60.1.69893 and its last Forever build is 1.60.1.70532 (22 Oct); the beta closed 23 Oct. `wow_cn_beta` (1.60.1.70450, 19 Oct) is the China beta line and is not snapshotted. Beta slug detail: confirmed 17 Sept 2026 by probe of build 1.60.1.69893 (Skyborne races, Shatter Curse, Well Rested, Bountiful Harvest all present). Blizzard reused the 2025 Mists Classic beta slug; Forever builds are the 1.60.x version line, so always sort builds by creation time, never by version number. `wow_classic_titan` was checked 15 Sept and again 17 Sept and ruled out. Snapshot with `python scripts/wago_diff.py --snapshot`; read it with `python scripts/wago_query.py` (talents, legacy, racials, spell). Talents and Legacy live in the Trait tables, not in the old Talent table.

## Tier 3 — Captured tooltips (demo / beta screenshots)

| source-id | What | Where |
|---|---|---|
| `cwf` | classicwowforever.com — talent calculator chunk `/_next/static/chunks/forever-talents-*.js`, racials, Legacy, class changes, each with evidence screenshots | https://classicwowforever.com |
| `wcf-info` | wowclassicforever.info — races, talents (secondary) | https://wowclassicforever.info |
| `wtavern-handson` | Warcraft Tavern BlizzCon floor hands-on (racials, 12 Sept 2026) | https://www.warcrafttavern.com/forever/news/all-racial-abilities-in-world-of-warcraft-forever/ |

## Tier 4 — Creator footage and community experts

| source-id | What | Where |
|---|---|---|
| `vod-blizzcon` | BlizzCon demo VOD | https://www.twitch.tv/videos/2872270692 |
| `creator-xaryu`, `creator-esfand`, `creator-desmephisto`, `creator-defcamp` | Videos with visible tooltips (all classes / Warrior, Hunter / Legacy / Shaman) | YouTube |
| `discord-earthshrine` | Earthshrine, the Shaman class Discord. Earliest Resto theorycraft and spreadsheets. Not scrapeable; check pinned resources by hand during beta. | https://discord.gg/earthshrine |

## Tier 5 — Secondhand

| source-id | What |
|---|---|
| `reddit` | r/classicwow, r/wowforever — leads only |
| `forum-player` | Non-staff forum posts — leads only |
| `secondhand` | lfcarry, mmojugg, quissy, masterofwarcraft, general MMO news — leads only |
| `fan-foreverchanges` | foreverchanges.pro — level-20 BiS lists per class/spec. No screenshots, no method stated. Leads only |
| `fan-wowforevertalents` | wowforevertalents.com — profession recipe and skill-level tables |
| `gold-mmoexp` | mmoexp quest and levelling guides. **Gold-seller site.** Never cite as support for a value; verify every step in game before acting on it |
| `press-icyveins` | Icy Veins articles and developer interviews. A Blizzard quote inside one is only as good as a verified Blizzard echo; do not promote it to tier 1 on the outlet's word |
| `addon-leatrix` | leatrix.com — Leatrix Plus documentation (addon behaviour, not game data) |

## Deliberately not used
- Wowpedia / Warcraft Wiki for Forever changes (lags weeks; fine for Classic baseline mechanics).
- Twitter/X (unverifiable, ephemeral). If a developer tweet matters, find the forum or news echo.
