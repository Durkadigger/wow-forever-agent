# Set up wow-forever-agent on a second machine (Windows PC)

**Instructions for Claude Code.** the maintainer is giving you this file on his PC. Follow it top to bottom, run the verification at the end, and report what passed. Ask the maintainer only where a step says so. The repo is public under his GitHub account `Durkadigger`; he must be the one who signs in so he can push to `main`. His personal `CLAUDE.local.md` is not in git and must be copied over by hand.

## 0. What this is
A Claude Code agent project for World of Warcraft: Forever. The Mac copy lives at `~/wow-forever-agent` and pushes to `https://github.com/Durkadigger/wow-forever-agent` (public). This PC will be a second working copy that stays in sync through that remote.

## 1. Install the tools

Check each first; install only what is missing. Use `winget` (built into Windows 10/11).

```powershell
git --version
gh --version
python --version
```

Install any that are missing:

```powershell
winget install --id Git.Git -e
winget install --id GitHub.cli -e
winget install --id Python.Python.3.12 -e
```

After installing, **close and reopen the terminal** so PATH updates. Re-run the three version checks. Python must be 3.9 or newer.

## 2. Sign in to GitHub (the maintainer does this part)

```powershell
gh auth login
```

Pick: **GitHub.com → HTTPS → Yes, authenticate Git with GitHub credentials → Login with a web browser.** the maintainer completes the browser step himself. Then confirm:

```powershell
gh auth status
```

It must show account `Durkadigger` with scope `repo`. If it shows a different account, stop and tell the maintainer.

## 3. Clone

Clone into the maintainer's home directory, same folder name as the Mac:

```powershell
cd $HOME
gh repo clone Durkadigger/wow-forever-agent
cd wow-forever-agent
```

## 4. Git identity for this repo only

The maintainer's personal email address is also a Battle.net login and must never appear in commits. Set the GitHub no-reply address **locally in this repo**, not globally, so his other projects are unaffected:

```powershell
git config user.name "<your GitHub username>"
git config user.email "<id>+<username>@users.noreply.github.com"   # from github.com/settings/emails
git config pull.rebase true
git config --get user.email
```

The last line must print the no-reply address.

## 5. Python dependency

Only one third-party package is used, by `scripts/fetch_talents.py`:

```powershell
python -m pip install --user requests
```

`scripts/forum_scan.py`, `scripts/wago_diff.py`, and `scripts/lint_knowledge.py` are standard library only.

## 6. Verify

Run all four. Each should finish without a traceback.

```powershell
python scripts/lint_knowledge.py
python scripts/forum_scan.py --categories
python scripts/wago_diff.py --list-products
python scripts/fetch_talents.py --dry-run
```

Expected: lint reports `0 error(s)`; the forum scan lists category 346 and its subcategories; wago prints a product table; the talent dry-run prints a parsed-talent count and a diff summary (it may say the chunk was not found if the fan site changed its build; that is not a setup failure).

Then start Claude Code in the folder:

```powershell
claude
```

It reads `CLAUDE.md` automatically. Skills in `.claude/skills/` and subagents in `.claude/agents/` load on demand. Ask it "what is the newest build in data/builds.json?" as a smoke test.

## 7. How sync works

`CLAUDE.md` tells the agent to `git pull` at the start of every session and to commit and push at the end of any session that changed files. Both machines follow the same rule, so whichever machine worked last, the other picks it up on its next session. If a pull ever reports a conflict, the agent resolves it by keeping both CHANGELOG entries and taking the newer `Data as of` build for knowledge files, then tells the maintainer.

Manual equivalents, if ever needed:

```powershell
git pull
```

```powershell
git add -A; git commit -m "describe the change"; git push
```

## 8. Things that do not carry over from the Mac

- **Claude's memory directory** is per machine. The Mac has notes about the beta-day checklist and the no-reply rule; the PC starts empty. The important reminders are also in `CLAUDE.md` and `docs/beta-day-checklist.md`, which do sync.
- **Apple connectors** (Calendar, Contacts, iMessage) referenced in the Mac's global `~/.claude/CLAUDE.md` do not exist on the PC. Nothing in this repo depends on them.
- **The 17 Sept calendar reminder** is on the Mac's Calendar.app only.
- **`.claude/settings.local.json`** is ignored by git on purpose; permissions are per machine.

## 9. Report back
Tell the maintainer: which tools were already present, which were installed, the `gh auth status` account, the result of each verification command, and the commit hash `git log --oneline -1` shows. Do not paste tokens or the Gmail address anywhere.
