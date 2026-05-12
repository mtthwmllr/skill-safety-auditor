# skill-safety-auditor

[![tessl](https://img.shields.io/endpoint?url=https%3A%2F%2Fapi.tessl.io%2Fv1%2Fbadges%2Fmtthwmllr%2Fskill-safety-auditor)](https://tessl.io/registry/mtthwmllr/skill-safety-auditor)

> **Why 90%?** Two points are deducted by Tessl's static scanner — not functional gaps. First, the bundled reference files (`security-checks.md`, `report-format.md`) are included and verified locally but undetectable by the scanner. Second, Mode 1 is flagged for fetching user-supplied URLs — which is intentional: you can't audit a skill before download without reading it. Both are documented as known limitations on the [security page](https://tessl.io/registry/mtthwmllr/skill-safety-auditor/security).

Audits a Claude Code skill for security risks before or after you install it.

---

## Why this exists

The Claude Code skills ecosystem is growing fast, and most users install skills without reading them first. Research into skills security has raised real concerns: a small number of markdown lines is all it takes for a skill to request shell access to your machine, and some skills have been found to include patterns that could exfiltrate credentials or inject instructions into Claude's behaviour. The `skill-safety-auditor` exists because no standard tooling existed to catch these risks before installation.

---

## What it checks

The auditor runs 14 checks across 4 categories:

- **Frontmatter** — declared tool access, missing permissions fields, overly broad tool lists
- **Script Content** — credential access, outbound network calls, obfuscation, persistent system modifications
- **Prompt Injection** — safety override instructions, false permission claims, instructions to conceal behaviour
- **Source Provenance** — anonymous maintainers, brand-new repositories, description/content mismatches

Each finding is rated **Critical**, **Warning**, or **Info**.

---

## Install

1. Download [`skill-safety-auditor.skill`](./skill-safety-auditor.skill)
2. In your terminal, run:
   ```
   claude skills install ./skill-safety-auditor.skill
   ```
3. That's it. The skill is now available in Claude Code.

---

## How to use it

Invoke the skill by telling Claude: *"Audit this skill before I install it"* and paste the GitHub URL, install command, or local file path. Claude will ask which mode applies:

- **Mode 1 — Pre-download** — fetches the skill from a URL or install command before anything touches your machine
- **Mode 2 — Downloaded, not installed** — reads a `.skill` file you already have locally
- **Mode 3 — Already installed** — reads the live files from your Claude Code skills directory

Claude then runs all checks and presents a structured report with findings and remedies.

---

## Sample output

See a real audit of a real public skill: [audit-sample/sample-report.md](./audit-sample/sample-report.md)

---

## Is this skill itself safe?

This section runs the auditor's own checks against itself, publicly.

**Frontmatter**

```yaml
allowed-tools: Read WebFetch Glob
```

All three tools are appropriate to the skill's function:
- **Read** — reads local skill files in Modes 2 and 3
- **WebFetch** — fetches remote SKILL.md content in Mode 1
- **Glob** — finds bundled scripts in the skill directory

No shell access, no file write access, no credential access.

**Scripts**

No scripts are bundled. The `references/` directory contains two markdown files — `security-checks.md` and `report-format.md` — which are documentation only. No `.py`, `.sh`, `.js`, or `.bash` files are present.

**Prompt injection**

The SKILL.md does not attempt to override Claude's safety behaviour, does not claim special Anthropic permissions, and does not instruct Claude to conceal anything from the user. Every instruction relates directly to the stated purpose: auditing skill files.

**Source provenance**

Built by [mtthwmllr](https://github.com/mtthwmllr) and published directly to this repository.

**Self-audit verdict: Appears Safe.**

The three tools this skill uses (Read, WebFetch, Glob) are appropriate to its function. No scripts, no credential access, no prompt injection patterns.

---

## Contributing / issues

Found a gap in the checks, or a false positive? Open an issue at [github.com/mtthwmllr/skill-safety-auditor/issues](https://github.com/mtthwmllr/skill-safety-auditor/issues).

Pull requests welcome for new check categories or improvements to the remedy guidance.

---

## Licence

MIT — see [LICENSE](./LICENSE)
