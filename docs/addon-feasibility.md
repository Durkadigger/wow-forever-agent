# Addon feasibility for WoW Forever: rules, limits, red-team

Researched 17 Sept 2026 against client build 1.60.1.69893, before any addon code was written. Nothing here is written into `knowledge/`; this is an engineering note. Re-check after every beta build, because Blizzard has said further restrictions will reach Forever.

## 1. What is confirmed

| Fact | Source | Tier |
|---|---|---|
| "The addon disarmament changes introduced in Midnight, including secrets, will also be active in Forever." Forever shares retail's UI architecture with the vast majority of 12.1.5 APIs. Future UI changes reach both games. | Blizzard post in the WoW UI dev Discord, quoted by Wowhead, 16–17 Sept 2026. https://www.wowhead.com/news/wow-forever-will-have-addon-changes-from-midnight-382921 | T1 statement read through a T2 outlet; staff poster unnamed |
| In-combat restrictions are brought over so players will not have "computational add-ons". No specifics given. | Mike Nuthals (lead encounter designer), Kotaku interview, 14 Sept 2026. https://kotaku.com/new-things-learned-world-of-warcraft-forever-2000734005 | T1 quote via press |
| Restrictions and features are one-for-one with retail and kept in sync in both directions, so a new retail restriction reaches Forever in its next patch. Display is fine, telling the player what to do is not. Under the aura container model an addon registers an icon or sound with Blizzard and Blizzard shows it, so the addon itself never learns the buff is present. The Blizzard damage meter is built into Forever; Details can restyle it but only with the data Blizzard shares. A boss-warnings option was visible in the BlizzCon demo build. Retail addons should run on Forever within the first days of beta after small tweaks, and addon authors were put on a beta access list. Profession addons are the exception because the systems differ. Classic Era, Anniversary and Mists stay on the unrestricted legacy API. Quest helpers, arrows and map notes are unaffected; any updates they need are API differences, not restrictions. | MysticalOS (Deadly Boss Mods author), 15 Sept 2026. https://www.youtube.com/watch?v=THPNc8X1UkU . Read from YouTube auto-captions for 00:00–08:27 and 13:16–14:34, supplied by the maintainer via Gemini on 17 Sept. Authenticity check: caption timings line up with the video's published chapters at 05:25, 06:32 and 13:25, and the text has speech-recognition errors a summary would not invent. 08:27–13:16 and 14:34 onward not retrieved. | T4 |
| Forever's own UI source carries the full retail secret-value annotations. Classic Era, Anniversary, Mists Classic and Titan carry none. Forever's internal game type is "camelot". | `forever` branch of https://github.com/Gethe/wow-ui-source at 1.60.1 (69893), checked locally | T2 |
| The Forever client contains the addon manager UI, a "User addons disabled" state, and secret-value strings. | GlobalStrings table, wago.tools, b:1.60.1.69893 | T2 |

**Scope wording, unresolved.** MysticalOS says restrictions "only matter really when it comes to combat" and that they apply to PvP, dungeons and raids, with outdoor addons typically untouched. The Forever source lists a plain Combat restriction type next to Encounter, PvPMatch and Map, and on retail auras and cooldowns go secret in any combat. Reading both together: out-of-combat open-world reads are very likely fine; open-world *in-combat* reads must still be assumed restricted until Phase 0 measures it.

Not confirmed by Blizzard: whether addons are enabled in the beta (addon authors expect so, T4), the interface version number (toolmakers guess 16000/16001), where secrets apply in Forever (all combat or only instances), and per-category rulings on meters, boss mods, auction and quest addons.

## 2. How the restriction system works

A *secret value* is a number or string an addon may hold, pass to Blizzard's UI for display, and concatenate, but may not do arithmetic on, compare, index, or use as a table key. **A secret written to SavedVariables is saved as nil.**

Restriction types in the Forever source (`Enum.AddOnRestrictionType`): Combat, Encounter, ChallengeMode, PvPMatch, Map (a map that applies restrictions), Chat. Out of combat in the open world none should be active.

Verified in the Forever source:

- `GetSpellBonusHealing`, `GetSpellBonusDamage`, `GetCritChance`, `GetSpellCritChance`, `GetHaste`, `GetCombatRating`, `GetManaRegen`, `UnitAttackPower`, `UnitSpellHaste`, `UnitStat`: marked `SecretWhenUnitStatsRestricted`. The exact trigger is not documented.
- `C_UnitAuras.*` and the `UNIT_AURA` event: secret when aura restrictions are active.
- `COMBAT_LOG_EVENT_UNFILTERED`: `HasRestrictions = true`. The function that reads combat log events has moved to Blizzard-only namespaces. On retail, registering the event from an addon raises an error.
- No secret conditions on: trait/talent reads, `C_TooltipInfo.GetSpellByID`, `C_Spell.GetSpellDescription`.
- Still present: `/combatlog` writing `WoWCombatLog.txt` to disk, and the Advanced Combat Logging option.
- `Blizzard_DamageMeter` loads for Forever, so the built-in damage meter ships.
- Runtime checks available to an addon: `issecretvalue(v)`, `C_Secrets.HasSecretRestrictions()`, `C_Secrets.ShouldUnitStatsBeSecret()`, `C_RestrictedActions.IsAddOnRestrictionActive(type)`, event `ADDON_RESTRICTION_STATE_CHANGED`.

## 3. Terms of Service

Blizzard's UI Add-On Development Policy: addons must be free, code visible and unobfuscated, must not harm realms or players, no ads, no in-game donation requests, nothing beyond the game's rating, must obey the EULA, and Blizzard may disable any addon. The EULA bans cheats, bots, automation, hacks, and unauthorized third-party software that alters or interacts with the running game.

Assessment (inference; no explicit Blizzard ruling found):

- A personal, free, plain-Lua, read-only logging addon: compliant.
- Reading SavedVariables or `WoWCombatLog.txt` from disk with our own scripts: compliant. Nothing touches the running client, and Warcraft Logs works the same way.
- Never do: memory reading, input automation, anything that reads or drives the live client from outside, modifying game files, trying to defeat or work around secret values.

**Rule for this project:** if a value comes back secret, record that it was secret and stop. Do not look for a side channel. Working around the restriction is the one thing here that could plausibly put the account at risk.

## 4. Red-team of the original addon plan

Original plan: an addon that listens to the combat log, records every heal with stats at cast time, and saves structured test runs.

| # | Attack on the plan | Verdict | Response |
|---|---|---|---|
| 1 | Combat log events are unavailable to addons. | **Kills the core of the plan.** | Move per-heal logging out of the addon. Use the game's own `/combatlog` file and parse it in this repo. |
| 2 | Stat reads return secrets in combat. | Partly kills "stats at cast time". | Sample only out of combat. Blood Fury is a self-buff usable out of combat, so that test survives. |
| 3 | The stats trigger is undocumented; it may also fire on some maps or always in instances. | Unknown. | Check `issecretvalue` on every read and log the restriction state with it. Test in the open world first. |
| 4 | Secrets saved to disk become nil silently. We would read a clean-looking file with holes and draw wrong conclusions. | **Highest data-integrity risk.** | Never save a raw API value. Save `{value=..., secret=false}` or the string `"SECRET"`. The reader treats a missing field as an error, never as zero. |
| 5 | Addons may be disabled in the beta, or the interface number unknown. | Blocks everything. | Phase 0 below needs no addon. |
| 6 | API names differ from Classic (trait system, retail namespaces). Code written from Classic memory will error. | Certain. Forever is one-for-one with retail's API. | Write it as a retail addon against the Forever UI source, feature-detect every call, wrap in `pcall`. |
| 7 | Blizzard has said more restrictions are coming. | Certain over time. | Keep the addon tiny; keep all computation in the repo scripts, which no restriction can touch. |
| 8 | Statistical validity: heals have variance, crits, and talent multipliers. A sloppy test "proves" the wrong thing. | Real. | Prefer the direct stat read (no statistics). For log-based tests: same spell rank, same target, exclude crits, at least 20 casts per arm, record talents and gear. |
| 9 | ToS exposure. | Low if we stay read-only and never circumvent. | See section 3 rule. |
| 10 | Wasted build effort if one slash command already answers the question. | True for Blood Fury. | Phase 0. |

## 5. Revised plan

**Phase 0 — no addon. Run these in chat once the servers are up.**

```
/dump select(4, GetBuildInfo())
/dump C_Secrets and C_Secrets.HasSecretRestrictions()
/dump GetSpellBonusHealing(), GetSpellBonusDamage(2)
```

Then use Blood Fury (out of combat) and run the third line again. If healing moves by about 10%, open question #1 is answered with no addon and no statistics. If the output shows a secret, that is itself a finding: stats are restricted even out of combat.

Also turn on Advanced Combat Logging in the options and type `/combatlog` before any casting test. On retail the advanced log records the caster's spell power on every event, so the log file alone may show the Blood Fury change.

**Phase 1 — snapshot addon (small). Built 17 Sept 2026 as `addon/WFATest`, v0.1.0: syntax-checked and installed, not yet run in game. Test card in `addon/README.md`.** Out of combat only. Slash command saves: build and interface number, restriction state, all stat reads with secret flags, own buffs, talent picks, and the rendered tooltip text of chosen spells. Purpose: verify datamined numbers against the live client.

**Phase 1b — probe, session log, spellbook (v0.3.0, 19 Sept 2026). Syntax-checked, not yet run in game.** Observation the same day: the v0.1.0 addon wrote its SavedVariables file from the beta client, so addons are enabled in the beta and the TOC loads (interface number still unread).
- `/wfa probe` measures section 1's open scope question instead of guessing: about 60 reads, out of combat and in combat, each stored as value, SECRET, MISSING or error. Run per class, in the open world and in a dungeon. The reader's `--probe` report is the list of what can be logged.
- Session log: records on `PLAYER_REGEN_DISABLED/ENABLED`, `PLAYER_XP_UPDATE`, `PLAYER_LEVEL_UP`, `PLAYER_DEAD`, `ZONE_CHANGED_NEW_AREA`, `PLAYER_ENTERING_WORLD`, and debounced out-of-combat snapshots on gear and talent changes. These are state events, not combat log events. The handler stores values through the secrecy check and does no arithmetic or comparison on them; all analysis is in `read_addon_data.py --session`. Targets are recorded only when `UnitIsPlayer` returns false.
- Red-team of 1b: (a) a secret hp or mana at combat end would leave a hole, so a second record is taken 2 sec later and the reader counts, never fills, what stays secret; (b) if Blizzard later makes any of these events or reads restricted, the pcall and secrecy check turn that into recorded markers, not errors; (c) it still answers nothing about individual casts. That remains Phase 2.

**Measured 19–20 Sept 2026, b:1.60.1.69913, open world, level 1–6 Mage (348 records):** interface number is 16001. Current `UnitHealth("player")` and `UnitPower("player")` are secret at all times, out of combat too, even with `ShouldUnitStatsBeSecret()` false and no restriction type active; target `UnitHealthMax` is secret. Max health/mana, XP, money, level, zone, target name/level/type, every stat read, gear links and tooltips are readable out of combat. In-combat column still unmeasured: `/wfa probe` has not been run.

**Measured 20–25 Sept 2026, b:1.60.1.69913 and b:1.60.1.70009, level-20 Undead Paladin, 202 fights, 644 session records — this answers the scope question in section 1.** Restrictions in Forever are keyed to **instances, not to combat**:

| Read | Open world (Durotar, Barrens, Tirisfal) | Inside an instance (Ruins of Lordaeron, Wailing Caverns) |
|---|---|---|
| Target name and creature type | readable (38/38 fights) | **secret** (110/110 fights) |
| Target max health | readable | secret |
| Target level and classification (elite) | readable | readable |
| Own current health and mana | **secret, always** | secret |
| Own max health and mana, level, XP, money, zone, all stat reads, gear links, tooltips | readable | readable |

- The open-world / instance split is clean: zone "The Barrens" and the outdoor "The Wailing Caverns" gave 38 readable target names, while the instances "Ruins of Lordaeron" and "Wailing Caverns" gave 110 secret ones and not a single readable one. `C_Secrets.ShouldUnitStatsBeSecret()` reported false and no `Enum.AddOnRestrictionType` was active in either case, so **those two flags do not predict what is actually secret** — only an attempted read does.
- Current health and mana are secret everywhere, at all times, including standing still in a starting zone. Anything that needs them (mana per fight, health per fight, healing throughput) cannot come from an addon on any class. Recorded as secret and left alone per section 3.
- Consequence for the roadmap: out-of-combat stat snapshots, gear, talents, spellbook tooltips and XP-rate work are all viable anywhere. Per-fight resource analysis needs the game's own `/combatlog` file, which is still Phase 2 and still unwritten because no `WoWCombatLog.txt` has been produced yet.

**Phase 2 — log parser in this repo.** `scripts/combatlog_parse.py` reads `WoWCombatLog.txt` and answers questions like heal size with and without a buff, coefficients, proc rates. This is where all computation lives.

**Not building:** anything that listens to combat log events, computes in combat, tracks other players, or automates input.

**24 Sept 2026 beta update (b:1.60.1.70009), addon-relevant items** [T1 blizz-forum 2026-09-24] (Kaivax, WoW Forever Beta Development Notes – Updated September 24, https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-updated-september-24/2360696):
- New built-in **Cooldown Manager** (default off, Options → Gameplay Enhancement), currently testable only on Druid, Mage, Priest, Warrior, Warlock. It reads from the buff bar or action bar, same class of data WFATest already reads out of combat; no new secret-value surface implied.
- New known issues named for the Cooldown Manager itself (not WFATest): Banes/Curses don't retrack after dropping and reacquiring a target with an existing debuff; Healthstone, Arcane Blast, and pet cooldowns cannot be tracked; Priest tracks all spells by default; Mana Gem needs an extra cast before it tracks; item enhancements (Windfury, rogue poisons) cannot be tracked; Personal Resource Display doesn't show combo points.
- No interface-number change stated or observed; WFATest's 20 Sept reading of **16001** stands until re-measured on this build.
- No mention of secret-value rules changing for `UnitHealth`/`UnitPower`. Not re-tested in this refresh (no addon run against b:1.60.1.70009 yet).
