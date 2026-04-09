# Test Fixtures

## What is this?

This directory contains purpose-built test targets for `skill-safety-auditor`.
The skills here are **deliberately constructed to trigger known findings** —
they are not real tools and should not be installed.

This follows the same convention as the [EICAR test file](https://www.eicar.org/download-anti-malware-testfile/)
used in antivirus tooling: a safe, well-documented file that looks dangerous
enough to trigger detection, so you can verify your scanner is working correctly.

---

## test-skill-with-known-issues/

A fictional skill named `demo-analytics-helper` authored by the equally fictional
organisation "Acme Devtools". It is designed to trigger the following findings
when audited by `skill-safety-auditor`:

| Finding | Severity | Triggered by |
|---------|----------|--------------|
| B1 — Credential or Secret Access | 🔴 CRITICAL | `os.environ.get("ACME_API_KEY")` in `scripts/analytics.py` |
| B2 — Outbound Network Calls (escalated) | 🔴 CRITICAL | `requests.post(...)` in same script as credential read |
| A1 — Bash / Shell Tool Access | 🟡 WARNING | `Bash` declared in frontmatter `allowed-tools` |
| A2 — Write / Edit Tool Access | 🟡 WARNING | `Write` declared in frontmatter `allowed-tools` |

The following checks pass (showing a realistic mix, not a worst-case):

- ✅ A3 — `allowed-tools` is declared (not missing)
- ✅ A4 — Tool list is under 5 entries (not overly broad)
- ✅ C1 — No safety-override instructions in SKILL.md body
- ✅ C2 — No false claims of Anthropic approval or elevated access
- ✅ C3 — No instructions to conceal behaviour from the user
- ✅ D4 — Valid YAML frontmatter with `name` and `description` present

### Structure

```
test-skill-with-known-issues/
├── SKILL.md              # Fictional skill with Bash + Write in allowed-tools
└── scripts/
    └── analytics.py     # Stub script triggering B1 and B2
```

---

## How to use these fixtures

Run `skill-safety-auditor` in Local File Mode (Mode B) against the extracted path:

```
# Audit the test skill locally
/skill-safety-auditor
# When prompted for mode, choose B (local file audit)
# Provide path: test-fixtures/test-skill-with-known-issues/
```

The resulting report should match `audit-sample/sample-report.md`.
If it does not, the auditor may have changed behaviour — or you may have
found a regression worth reporting.

---

## What these fixtures are NOT

- Not real software — do not `pip install requests` and run `analytics.py`
- Not affiliated with any real organisation named "Acme" or otherwise
- Not a reflection of any real skill, author, or GitHub account
