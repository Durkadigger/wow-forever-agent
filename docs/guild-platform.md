# Guild platform: addon → data → website (design note, 7 Nov 2026)

Status: idea stage. Nothing here is built. Read `docs/addon-feasibility.md` first; Forever's addon rules decide what is possible.

## What the guild would actually use
Ranked by how often a guild asks for it, cheapest first:
1. **Roster gear + weapon audit.** Who is wearing what, item level per slot, empty slots, who still has a level-20 weapon at 35. Readable by addon out of instances (`GetInventoryItemLink`).
2. **Attunements and key quests.** Hyjal Summit, Barrow Deeps, Onyxia chain; the Forsaken Greataxe / Wolfsbane-style weapon chains while levelling. Quest completion flags are readable (`C_QuestLog.IsQuestFlaggedCompleted`) once we know the Forever quest IDs; the agent can collect those from members' quest logs.
3. **Professions and recipes.** Who can craft what; the Blacksmithing list in `knowledge/gear/paladin-ret-20.md` is the seed.
4. **Consumables and raid readiness** (later, for 9 Dec raids): resist gear, fire protection potions, buff food.
5. **Not possible:** damage or healing meters, threat, health in combat. Secret values. Do not try.

## Data flow
```
member's client ──WFATest addon──> SavedVariables/WFAGuild.lua
        │                                   │
        │ (opt-in) GUILD addon messages     │ export string (copy from in-game frame)
        ▼                                   ▼
 officer's client roster  ──────────>  website "paste export" form  ──> database ──> guild pages
```
Two transport options; build the second first.
- **Export string (WoWAudit model).** The addon shows a text box with a compressed, base64 export of the member's own gear, professions and attunement flags. The member copies it into a form on the website. No in-game comms, nothing to verify about `SendAddonMessage`, works even if Blizzard restricts addon chat. Members do it after each raid night or when nagged.
- **GUILD addon messages (Classic guild-addon model).** Each client broadcasts a short summary on login or on `/wfa guild sync`; any officer with the addon holds the full roster and exports once. Nicer, but `C_ChatInfo.SendAddonMessage` on the GUILD channel was never probed in the Forever beta (`docs/addon-feasibility.md` lists it as untested). Probe it first; if it is throttled or secret in instances, the export string still works.

Blizzard's addon policy applies either way: free, source visible, no obfuscation, no ads, nothing that plays the game for you. Members opt in; the addon only ever sends the member's own data.

## Website
- **Public part:** a static site generated from `knowledge/` (the talent files, racials, dates, dungeon list) plus the agent's method. Build with any static generator from the Markdown; host on GitHub Pages from this repo, rebuilt by a GitHub Action on every merge to `main`. Zero cost, no server.
- **Guild part (locked):** roster, gear audit, attunement board, profession list, raid sign-ups. Needs authentication, which GitHub Pages cannot do. Cheapest fit for a guild: **Discord login**. Members already have the guild Discord; gate the pages on "has the Plague member role". Options that do this without running a server: Cloudflare Pages + Cloudflare Access (free up to 50 users, supports Discord or email one-time-code login), or a small Next.js app on Vercel with Discord OAuth and a Postgres free tier for the roster. Cloudflare Access is the least code; the Vercel app is the one that can grow (sign-ups, loot history).
- **What the agent adds:** a nightly job turns the roster database into `knowledge/guild/roster.md` (git-ignored or in a private repo), so members can ask the agent "who still needs the Onyxia attunement?" and get a sourced answer. Member data never goes into the public repo.

## Privacy and ownership
- Character names and gear are visible to anyone in game, so a roster is low-sensitivity. Still: opt-in, members can delete their entry, and the public site never shows the roster.
- The public repo stays game facts only. Roster data lives in the website database and, if the agent needs it, in a private repo or a git-ignored file.

## Order of work
1. Probe in game: `SendAddonMessage` on GUILD; which quest flags and item links are readable outside instances at 60. (One session with the existing `/wfa probe`, extended.)
2. Extend WFATest with an export string for gear, professions and a fixed list of attunement quest IDs. Members paste it into a form.
3. Static public site from `knowledge/` on GitHub Pages.
4. Locked guild section with Discord login and the roster pages.
5. GUILD addon-message sync, only if step 1 shows it works and members want the convenience.
