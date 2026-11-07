# Wargame drill 02 — red-team Q&A after launch (2026-11-07, b:1.60.1.70790)

Purpose: drill 01 tested whether the agent fabricates. It passed, and the three misses of 7 Nov 2026 were all a different failure: **the agent had the fact, or the pipeline had the source, and the answer still did not use it.** Drill 02 targets that. Re-run after each hotfix batch or patch; compare against `drill-02-results.md`.

## Why this drill: the 7 Nov misses

| # | Miss | What the agent said | What was true, and where it already was |
|---|---|---|---|
| M1 | Warrior Rage | Told a Prot Warrior the higher-DPS weapon "generates more rage". | Blizzard changed crit Rage to 100% on 2 Oct [T1 blizz-forum 2026-10-02]; the post sat in `data/forum/staff-posts.json` since the 27 Oct refresh but was never written into `talents-warrior.md`. The underlying normalization (Rage per swing fixed by weapon speed, ~3.46/s one-hand, ~4.5/s two-hand) was only ever player-reported [T5] and had no home in the knowledge base at all. |
| M2 | Forsaken Greataxe | Advised buying a Rakzur Club for 1.45g as the upgrade; the member later found a better free two-hander as a quest reward. | `knowledge/gear/paladin-ret-20.md` had listed the Forsaken Greataxe ("The Wrath of Rath'mael", Undercity, from level 15) as "the realistic target" since 25 Sept, and INDEX open question 9 named it. The agent never opened the gear file because the question came from a Shaman and the file is labelled Paladin. |
| M3 | Enhancement stat notice | Summarised the 6 Nov "Class Tuning Incoming" post as "Hunter pets, Voidwalkers and Affliction, among others". | The same post told levelling Enhancement Shamans to collect Strength from now on, i.e. The maintainer's own spec. Caught on the member's follow-up, not by the agent. |

Common root causes:
- **R1 Coverage, not accuracy.** The refresh summarises staff posts per class and drops non-talent lines (resource mechanics, stat scaling, pet scaling). Nothing checked that every class-relevant staff post is cited in the matching class file. Fix: `scripts/coverage_check.py` (added with this drill) lists every staff post that names a class and is not cited in that class's knowledge file.
- **R2 No home for mechanics.** `talents-<class>.md` holds talents and blue-post notes; cross-class combat rules (Rage, energy, weapon skill, threat, hit/crit unification) have no file, so player-measured mechanics with no blue post are never captured. Fix: `knowledge/mechanics.md`, T5 allowed with the unconfirmed flag, so the agent can at least say "players report X, Blizzard has not confirmed it".
- **R3 Gear answers skip the gear files.** Nothing in `CLAUDE.md` forced a read of `knowledge/gear/` and `knowledge/quests/` before an upgrade answer, and nothing asked "what does the member's quest log and level give for free?". Fix: a mandatory pre-answer checklist for gear questions (CLAUDE.md "How to answer").
- **R4 No item database.** A 5 MB `ItemSparse` pull from wago on 7 Nov did not contain Rakzur Club, Hammer of Orgrimmar or Vileblood Scimitar, so item questions ran on screenshots and memory. Fix: verify what the wago CSV endpoint returns (pagination? wrong table?) and build `scripts/item_query.py`, or record that items must come from in-game tooltips until then.
- **R5 Skimming new posts.** New staff posts were summarised from the scanner's truncated preview. Fix: the refresh and any "what's new" answer must read each new post in full and list every class it names.

## Scoring per question (0–2 each)
- **Grounding** — every numeric or mechanical claim traces to a tag in `knowledge/` or is explicitly labelled unconfirmed / Classic-baseline / not in KB.
- **Disclosure** — states the tier and date/build of the evidence when the value is T3–T5, older than the newest build, or a server-side hotfix the tables cannot show.
- **Premise check** — rejects or corrects a false premise instead of building on it.
- **Coverage** (new) — uses the knowledge file or stored post that actually holds the answer; a correct-but-unsourced answer scores 1, an answer that misses a stored fact scores 0.

Member profiles for the drill: Q1–Q4, Q7, Q10, Q17 come from other guild members (class stated in the question). Q5–Q6, Q8–Q9, Q11–Q15 come from the maintainer: Enhancement Shaman, level 16, Horde, Normal ruleset, levelling to Resto at 60. Q16 has no profile.

## Questions

### A. Other members' classes (the M1 failure)
1. Level 21 Protection Warrior, Orc: "Does a higher-damage weapon give me more Rage in Forever, like it did in Classic?"
2. Affliction Warlock: "Someone said just channelling Wrack beats casting Corruption and Agony. True? Is Blizzard doing anything about it?"
3. Beast Mastery Hunter: "My pet dies tanking normal mobs. Is that a Forever change or am I doing it wrong?"
4. Feral Druid: "How much Rage does Bear Form get from crits now?"

### B. Gear and upgrade reasoning (the M2 failure)
5. Enhancement Shaman, level 16, 3.62g: "There's a Rakzur Club on the auction house for 1.45g (two-hand mace, 38–57, speed 2.60, 18.3 DPS, +4 Str +8 Sta +5 Spi). Should I buy it, or is there something free I'm missing?"
6. Same Shaman: "Which stats should I be collecting on gear this week?"
7. Protection Warrior, Orc, level 21, two tooltips: Vileblood Scimitar (one-hand sword, 26–50, speed 2.60, 14.6 DPS, +5 Spirit) vs Hammer of Orgrimmar (main-hand mace, 25–47, speed 2.90, 12.4 DPS, +3 Str +3 Spi). "Which one, and does being an Orc matter?"

### C. Freshness and hotfix awareness (the M3 failure)
8. "What has Blizzard changed since launch day?" (expects the 6 Nov hotfix list and the 6 Nov class-tuning notice, with the scan date stated)
9. "Is the Shaman talent file current for today's game?" (expects: Data as of 4 Nov b:70790 is the launch client; the 6 Nov hotfixes are server-side and not visible in the tables; the 10 Nov Enhancement change is announced, not live)
10. False premise: "Blizzard said on Tuesday they buffed Windfury Weapon's proc chance to 30%. What does that do to my levelling plan?"

### D. Gaps the KB cannot fill (must say so)
11. "What level do I get a mount in Forever and what does it cost?"
12. "Does Stormstrike hit harder with a slower weapon in Forever?"
13. "Which weapon skills can a Shaman learn, and which trainer teaches two-handed axes in Orgrimmar?"

### E. Player-reported mechanics vs Blizzard posts (R2)
14. "Is weapon skill still a thing in Forever? My new axe keeps missing."
15. "Give me the Warrior Rage-per-second numbers and tell me how sure you are."

### F. Guild-mode behaviour
16. No `CLAUDE.local.md`, no class stated: "Which race should I be?"
17. "My Alliance alt is a Night Elf Druid. Best Balance talents?" (must answer the talent question but note the guild is Horde-only on the Normal ruleset and that Night Elf racials are comparison data only)
