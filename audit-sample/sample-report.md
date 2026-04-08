# Sample Audit Report

This is a real audit produced by `skill-safety-auditor` v1.0.0 on a live public skill.

---

```
═══════════════════════════════════════════════
  SKILL SAFETY AUDIT REPORT
═══════════════════════════════════════════════

Skill:         hundred-million-offers
Source:        wondelai/skills (via NeverSight/skills_feed mirror)
Audited on:    April 8, 2026
Scripts found: 0

───────────────────────────────────────────────
OVERALL VERDICT
───────────────────────────────────────────────

🟡 PROCEED WITH CAUTION — Warnings found.

───────────────────────────────────────────────
🟡 WARNINGS  (2)
───────────────────────────────────────────────

A3 — No allowed-tools Declared
Found in: SKILL.md frontmatter
Detail: No allowed-tools field present in frontmatter. Access scope undefined.
Why this matters: Without an allowed-tools declaration, there is no way to confirm
  what tools this skill can invoke. It may be harmlessly read-only, or it may have
  broader access than expected.
Remedy: Check the repo directly to confirm intent. Request explicit
  `allowed-tools: []` from maintainer if the skill is genuinely read-only.

D1 — Fetched from Unverified Mirror
Found in: Source provenance
Detail: Retrieved from NeverSight/skills_feed aggregator, not directly
  from github.com/wondelai. Mirror may diverge from canonical source.
Why this matters: Aggregator mirrors are not always in sync with the original
  repository. Content may differ from what the original maintainer published.
Remedy: Verify at https://github.com/wondelai/skills directly before installing.

───────────────────────────────────────────────
🟢 INFO / NOTES  (2)
───────────────────────────────────────────────

Note: Affiliate links present in Further Reading section.
Note: references/ directory not audited (markdown content docs only,
  no script references observed).

───────────────────────────────────────────────
WHAT WAS REVIEWED
───────────────────────────────────────────────

✅ SKILL.md frontmatter (allowed-tools, name, description)
✅ SKILL.md body (instructions, prompt injection patterns)
✅ No scripts referenced — script checks not applicable

───────────────────────────────────────────────
WHAT WAS NOT REVIEWED
───────────────────────────────────────────────

- Runtime behaviour (this audit is static analysis only)
- Canonical source at github.com/wondelai (mirror was used)

───────────────────────────────────────────────
REMINDER
───────────────────────────────────────────────

This is a static pre-install review, not a guarantee of safety.
Even a clean audit does not protect against:
- Supply chain attacks (repo contents changed after audit)
- Runtime behaviour not visible in source
- Skills updated after you install them

When in doubt, don't install.
═══════════════════════════════════════════════
```
