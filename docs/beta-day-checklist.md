# Beta-day checklist — run on/after 17 Sept 2026

Beta opens 17 Sept 2026 (Q&A 10:00 a.m. PDT, Warcraft Twitch/YouTube). Everything below was deferred on 15 Sept because it needs a real client or the Q&A. Work top to bottom; tick as you go; each step says what it unblocks.

## Day 1 — find the client, refresh, re-drill

- [ ] **Watch or read the Q&A.** Note every date, price, and mechanic statement. Tag `[T1 blizz-video 2026-09-17]`. Resolve open question #4 (beta end 21 vs 22 Oct) if answered.
- [ ] **Forum scan.** `python scripts/forum_scan.py --pages 5`. Beta bug-report and feedback subforums will likely appear under category 346; the scanner picks up new subcategories automatically. Note any new subforum ids in `sources.md`.
- [x] **Find the Forever client on wago.** *Done 17 Sept 2026: `wow_classic_beta`, build 1.60.1.69893. It was not a new slug; Blizzard reused the old Mists Classic beta product. `--list-products` now flags that case as "new version line".* Original step: `python scripts/wago_diff.py --list-products`. Look for a new product slug created 17 Sept or later. Confirm with `--probe --product <slug>` (expects Skyborne race, Shatter Curse, Well Rested, Lava Burst). Set `wago_product` in `data/builds.json`. If nothing appears within 48 h, check Wowhead Forever / Warcraft Tavern for the build number and search wago by version.
- [x] **First snapshot.** *Done 17 Sept 2026, including the Trait, Curve and SkillLine tables that the talent trees, per-rank values and racials actually live in.* Original step: `python scripts/wago_diff.py --snapshot`. Registers the build. A second snapshot on the next build enables `--diff`.
- [ ] **Talents.** *Tier 2 half done 17 Sept 2026: `python scripts/wago_query.py talents all --write` put the full datamined trees, all ranks, in every class file's Overrides block. Still to do: the tier 3 regeneration below, and check the Overrides blocks survive it.* `python scripts/fetch_talents.py --dry-run`, then `--build <version>` once the build is known. Check the Overrides blocks survived.
- [ ] **Full refresh.** Run the `forever-refresh` skill (scout agent). Lint must pass. CHANGELOG entry.
- [ ] **Re-run drill 01.** Same 16 questions in `docs/wargame/drill-01-questions.md`. Expect Q5, Q6, Q8, Q12 to move from "not in KB" to tagged T2 answers. Record as `drill-02-results.md`. Any answer still citing `b:blizzcon-demo` when a newer build exists is a refresh failure.

## Week 1 — the deferred wargames (need a real build to be meaningful)

- [ ] **Stale-data drill.** Register a fake newer build in `data/builds.json`, ask five questions, confirm every answer discloses the files are behind. Remove the fake build.
- [ ] **Precedence drill.** Plant a T3 value newer than a T1 value in a scratch copy; run scout step 6; confirm T1 survives.
- [ ] **Conflict drill.** Two official sources disagreeing on one number; confirm both are recorded, none picked.
- [ ] **Injection re-test** with a forum-shaped payload instead of a fan-page one.

## Decisions the maintainer deferred on 15 Sept

- [ ] **Scheduling.** Weekly refresh during beta, patch-day after launch. Options: Cowork scheduled task opening this folder with "run forever-refresh", or cron `claude -p "run the forever-refresh skill"`. Decide once the beta patch cadence is visible.
- [ ] **EU forums.** Add `eu.forums.blizzard.com` to the scanner if EU-only staff rulings appear. Doubles requests; cheap.
- [ ] **Public repo.** Still private. Before flipping: re-read CLAUDE.md and INDEX.md for personal detail; commits already use the no-reply address.

## After the checklist
Update this file's title to "done <date>" or delete it and move anything still open to `knowledge/INDEX.md` open questions. Remove the standing reminder from `CLAUDE.md`.
