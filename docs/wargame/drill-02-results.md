# Wargame drill 02 — results (2026-11-07, b:1.60.1.70862)

Answering agent: a fresh `general-purpose` subagent with no conversation context, repo files only, no web (281k tokens, 10.7 minutes, 39 tool calls). Auditor: main session, every claim grepped against `knowledge/` and `data/forum/staff-posts.json`. Questions: `drill-02-questions.md`. The run overlapped the 7 Nov refresh, so some answers describe files "not yet updated" that were updated minutes later; those remarks were counted as correct disclosure, not errors.

## Scorecard (Grounding / Disclosure / Premise / Coverage, 0–2 each)

| Q | Topic | G | D | P | C | Notes |
|---|---|---|---|---|---|---|
| 1 | Warrior Rage vs weapon damage | 2 | 2 | 2 | 2 | T1 crit-Rage and damage-taken fixes; T5 normalization flagged low confidence; Classic rule named as the premise and corrected. |
| 2 | Affliction Wrack vs DoTs | 2 | 2 | – | 2 | 6 Nov notice and the Soul Siphon hotfix from the store; Wrack coefficient from the 2 Nov block. |
| 3 | Hunter pet dying | 2 | 2 | 2 | 2 | 10 Nov notice; pet Health 2 per Stamina (was 7.5) [T1 2026-11-03] verified in `talents-warlock.md`; flagged that the stored post was truncated. |
| 4 | Bear Rage from crits | 2 | 2 | – | 2 | 75% → 100% with both dates; Blood Frenzy from the tree; truncation flagged. |
| 5 | **Rakzur Club vs free two-hander (the M2 miss)** | 2 | 2 | 2 | 2 | **Found the Forsaken Greataxe** in `gear/paladin-ret-20.md` and INDEX question 9, named the quest and the Orgrimmar axe trainers (verified in `systems`, line 90), said "hold the gold until you check". The exact failure of 7 Nov did not repeat. |
| 6 | Enhancement stats this week | 2 | 2 | – | 2 | 6 Nov notice; explained why Intellect wins today (Mental Dexterity). |
| 7 | Scimitar vs Hammer, Orc | 2 | 2 | 2 | 2 | Same verdict as the session, with the Rage caveat the session had missed (M1). |
| 8 | What changed since launch | 2 | 2 | – | 2 | Listed the 5 Nov Invite-a-Friend hotfix and the Known Issues post (PvP vendors, "Vorsha the Lasher") **which the session's own answer earlier that day had not mentioned**, plus the 6 Nov hotfixes, the notice and the 70862 build. |
| 9 | Is the Shaman file current | 2 | 2 | – | 2 | Caught that `builds.json` already listed 70862 while the file still said 70790, and offered the refresh. |
| 10 | False: Windfury buffed to 30% | 2 | 2 | 2 | 2 | Searched all 187 posts and the 70862 tooltip; rejected; asked for a link. |
| 11 | Mount level and cost | 2 | 2 | – | 2 | "Not in KB"; checked the riding spells in the tables; Classic figures labelled unverified. |
| 12 | Stormstrike and weapon speed | 2 | 2 | – | 2 | Classic weapon-damage rule as baseline, normalization unknown, cited the gear file's Seal of Command reasoning. |
| 13 | Shaman weapon skills and trainers | 2 | 2 | – | 2 | Correct list; **found a contradiction between `mechanics.md` and `talents-shaman.md` on Shaman Dual Wield** (finding F1). |
| 14 | Weapon skill still exists? | 2 | 2 | 2 | 2 | Unconfirmed either way, with the 18 Sept glancing-blow known issue as evidence that glances exist. |
| 15 | Rage-per-second numbers | 2 | 2 | – | 2 | Separated T1, T2 talent values and T5; confidence "low" with reasons. |
| 16 | No profile: which race? | 2 | 2 | – | 2 | Asked for class and spec; listed Horde races; shop price given "as of 15 Sept". |
| 17 | Alliance Night Elf Balance | 2 | 2 | – | 2 | Answered, labelled the build as its own derivation, noted the guild is Horde-only and open question 3. |

**Totals:** Grounding 34/34 · Disclosure 34/34 · Premise 10/10 · Coverage 34/34. Every claim checked exists in a file with a tag. Three claims the auditor doubted (Orgrimmar weapon masters, pet Health per Stamina, glancing blows in the known-issues list) were all in the knowledge base.

## What this means
A fresh agent that reads the knowledge base answered all three of the 7 Nov misses correctly from the same files the session had. **The misses were the session's, not the knowledge base's:** it answered gear and "what's new" questions from conversation context and from the scanner's 4,000-character previews instead of opening `knowledge/gear/`, the INDEX open questions and the full stored posts. The fixes are therefore procedural (CLAUDE.md and the refresh skill), plus the pipeline bugs below.

## Findings
- **F1 — internal contradiction (Q13).** `talents-shaman.md` said Shaman "still learn Dual Wield (spell 674) through the same talent/trainer route", while `mechanics.md` said Dual Wield is granted to no class, and the session had told the maintainer Shamans cannot dual wield. The tables show a `SkillLineAbility` row for spell 674 on the Shaman skill line but no talent, trigger or level grant, and no trainer has been seen offering it. Both files now say exactly that and mark it unconfirmed.
- **F2 — stale "not in KB" (Q5, Q13).** `mechanics.md` claimed trainer locations were not in the knowledge base; `systems-legacy-servers-dates.md` line 90 has had the Orgrimmar and Thunder Bluff weapon masters since 23 Sept. Fixed. Rule: grep before writing "not in the knowledge base".
- **F3 — the session skims "what's new" (Q8).** The drill agent found two 5 Nov posts the session's own summary had skipped. Rule added to CLAUDE.md: a "what changed" answer reads every new stored post in full and names each class it touches.
- **F4 — scanner truncation (Q3, Q4, Q8 all flagged it).** `forum_scan.py` kept 4,000 characters per post; the development-notes posts run 16k–39k. Fixed (60,000) and the seven affected posts refetched. The 2 Nov Warrior section, including Defensive Stance 30% → 80%, had been invisible to every scan of the store.
- **F5 — nested store.** `staff-posts.json` is `{"posts": {...}}`; two ad-hoc scans in the session iterated the top level and found nothing. `coverage_check.py` now descends automatically; the refresh skill tells the agent.
- **F6 — no item table.** wago's `ItemSparse` for `wowf` (19,307 rows) contains none of the levelling items checked; Classic-line clients keep item data server-side. Items stay tier 2 in-game tooltips or Wowhead. INDEX question 9 updated.
- **F7 — the agent is cheap to drill.** 17 questions for 281k tokens. Re-run after every hotfix batch; compare this table.

## Procedural fixes applied (same commit)
1. `CLAUDE.md` "How to answer": gear/upgrade questions must read `knowledge/gear/`, `knowledge/quests/` and the INDEX open questions, and ask what the member's quest log and level give for free, before recommending a purchase; "what's new" answers read full stored posts; "not in the knowledge base" requires a grep first; cross-class rules live in `mechanics.md`.
2. `forever-refresh` skill: step 1 now runs `python scripts/coverage_check.py` after the forum scan and writes every uncited post into its class file (or into `data/forum/coverage-ignore.json` with a reason); the store is nested; read posts from the store, not the scanner's console preview.
3. `knowledge/mechanics.md` created; `scripts/coverage_check.py` created; `scripts/forum_scan.py` cap raised.

## Deferred drills (from `docs/beta-day-checklist.md`, still not run)
Stale-data drill (fake newer build), precedence drill (T3 newer than T1), conflict drill (two official sources disagreeing). Run them as drill 03 after the 10 Nov hotfix refresh.
