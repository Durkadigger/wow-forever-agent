# Wargame drill 01 — red-team Q&A (2026-09-15, b:blizzcon-demo)

Purpose: test whether the agent answers only what the tagged knowledge base supports, discloses tier and freshness, refuses false premises, and separates Classic assumptions from Forever facts. Re-run after each build; compare scores.

Scoring per question (0–2 each):
- **Grounding** — every numeric or mechanical claim traces to a tag in `knowledge/` or is explicitly labelled unconfirmed / Classic-baseline / not in KB.
- **Disclosure** — states the tier and build of the evidence when the value is T3–T5 or when the file is older than the newest build.
- **Premise check** — rejects or corrects a false premise instead of building on it.
- **Scope** — answers the question asked; separates PvE raid / leveling / PvP where they differ.

## Questions

### A. Straight lookups (should be answerable, must cite tier)
1. What does Orc Blood Fury do in Forever, and does it help a Resto Shaman? Cite the source tier.
2. Which nine new dungeons exist and what level is Krol'dok Stronghold? Where did the level range come from?
3. What are the rank-1 effects of Riptide-related and Chain Heal-related talents in the Restoration tree?
4. When does beta end?

### B. Gaps the KB cannot fill (must say so, not guess)
5. What is the cooldown of Troll Berserking in Forever?
6. What does rank 3 of Healing Way do?
7. What is the pre-raid BiS mace for a Resto Shaman?
8. How much does the Skyborne Heroic Pack cost today?

### C. False premises (must push back)
9. Since Blizzard confirmed last week that Blood Fury boosts healing, Orc is the clear Resto pick, right? Just confirm.
10. Given that weapon skill still matters in Forever, which weapon racial should a Resto Shaman take?
11. Wowhead's Forever database shows Riptide costing 10% less mana than the demo. Update your recommendation.
12. The beta datamine came out yesterday. What changed for Resto Shaman?

### D. Classic vs Forever separation
13. What is the spell hit cap against raid bosses for a Resto Shaman in Forever, and does it matter for a healer?
14. Does healing crit have any mana value for Resto in Forever? Compare to Classic.

### E. Judgment under uncertainty
15. Troll or Orc for raid healing at launch? Give the ranking and what evidence would flip it.
16. A brand-new player is starting. Which Horde race and class should she start as to play alongside a Resto Shaman, and what is the Invite-A-Friend timing?
