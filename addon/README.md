# WFATest — in-game snapshot addon

Read-only. Any class. Saves your stats, buffs, talents, Legacy perks, gear, spellbook and live tooltips so the agent can check datamined numbers against the real game, and keeps a small session log while you play. Background and rules: `docs/addon-feasibility.md`.

**Status: v0.3.0, written against the Forever UI source (build 1.60.1.69893) and syntax-checked. v0.1.0 loaded in the beta client (it wrote its SavedVariables file on 18–19 Sept 2026), so addons are enabled; no command has been run in game yet.** Expect a first-run fix or two.

## Three ways it collects data
1. **`/wfa probe` — find out what can be logged.** It calls about 60 game functions (health, mana, XP, stats, target, threat, cooldowns, auras, casting, pet) and records for each one whether the game answered, answered with a *secret*, or does not have the function. It does this out of combat straight away, then again by itself at the start of your next fight and 3 seconds in. `python scripts/read_addon_data.py --probe` prints the two columns side by side. Run it once per class and once inside a dungeon: the rules may differ there.
2. **Session log — on by default, nothing to type.** One small record on plain game events: entered combat (with the mob's name and level, never a player), left combat, XP gained, level up, zone change, death, login. Each record holds level, XP, health, mana, money and zone. Level-ups, gear changes and talent changes also store a full stat snapshot, your gear and your spellbook. `python scripts/read_addon_data.py --session` turns it into fights, fight length, downtime, mana and health spent per fight, kill XP vs quest XP and XP per hour, per character and level. `/wfa auto off` stops it. It keeps the newest 4,000 records.
3. **`/wfa spells` — every spell you know with its live tooltip.** `python scripts/read_addon_data.py --spells fireball` shows the text. This is how the agent checks datamined spell numbers for a Mage, Paladin or anything else without a list of spell IDs.

What it cannot do, on any class: see individual casts, hits, heals or procs. The game does not give combat log events to addons, and most numbers turn secret in combat. For that, use the game's own log (last section).

## Install or update
```
python scripts/install_addon.py
```
At character select, open AddOns. If WFATest shows "Out of date", tick **Load out of date AddOns**.

## The easy way: one command
Stand anywhere in the open world, out of combat, and type:

```
/wfa go
```
It records status, a baseline with your gear, your talents, your whole spellbook, an out-of-combat probe (plus the Riptide / Water Shield / Mana Tide tooltips on a Shaman), then starts a 25-second watch. You do three things: **press Blood Fury** when it tells you (any spell power buff if you are not an Orc), **attack one mob** afterwards (the addon takes the in-combat snapshot by itself), then type **`/reload`**. Tell the agent "addon data is ready".

On a low-level character the Blood Fury healing answer will come back INCONCLUSIVE: 10% of almost no spell power rounds to nothing. That is expected; see `docs/ingame-theory.md` for what each level range can answer.

## The same thing by hand
Do these in the open world, out of combat, in this order. Each takes seconds.

1. `/wfa status` — read the chat output. Note the **interface** number and whether it says stats are secret.
2. `/wfa snap baseline`
3. `/wfa talents`
4. **Blood Fury test (Orc only):** `/wfa watch 25 bloodfury`, wait 3 seconds, press Blood Fury, let the watch finish.
   Any other race: do the same with a trinket or buff that raises spell power, under a different label.
5. `/wfa tip 408521` (Riptide) and `/wfa tip 408510` (Water Shield).
6. Attack a mob, and during the fight type `/wfa snap incombat`. This measures whether open-world combat hides your stats.
7. `/reload` — nothing is written to disk until you do this or log out.

Then tell the agent "addon data is ready". It runs:
```
python scripts/read_addon_data.py --verdict
python scripts/read_addon_data.py --watch bloodfury
python scripts/read_addon_data.py --probe
python scripts/read_addon_data.py --session
```

## Also worth doing, no addon needed
Options → turn on **Advanced Combat Logging**, then type `/combatlog` before casting tests. The game writes `Logs/WoWCombatLog.txt`, which the agent can read directly.

## What it will never do
Cast, target, chat, automate input, listen to combat log events, record other players, compute anything in game, or try to recover a value the game has marked secret. A secret is stored as the word `SECRET` and the analysis skips it.

## Commands
`/wfa go` · `/wfa status` · `/wfa probe` · `/wfa auto on|off` · `/wfa spells` · `/wfa snap [label]` · `/wfa watch <sec> [label]` · `/wfa talents` · `/wfa tip <spellID>` · `/wfa clear`

## Second machine or second player
SavedVariables are per account and per computer. For another member's character: copy `addon/WFATest` into their `Interface/AddOns`, and after a session have them send their `WTF/Account/<account>/SavedVariables/WFATest.lua` over; the agent reads it with `--file`.
