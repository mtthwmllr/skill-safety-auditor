# skill-safety-auditor

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

Invoke the skill by telling Claude: *"Audit this skill before I install it"* and paste the GitHub URL, install command, or local file path. Claude will ask whether you want a pre-download audit (Mode A) or a local file audit (Mode B), then walk you through the findings and any remedies step by step.

---

## Sample output

See a real audit of a real public skill: [audit-sample/sample-report.md](./audit-sample/sample-report.md)

---

## Is this skill itself safe?

This section runs the auditor's own checks against itself, publicly.

**Frontmatter**

```yaml
name: skill-safety-auditor
version: 1.0.0
description: >
  Audits a Claude Code skill for security risks BEFORE or AFTER download.
```

No `allowed-tools` field is declared. That triggers check A3 (No allowed-tools Declared) in the auditor's own taxonomy. Here is why it is not a concern in this case, and how to verify it yourself:

The skill uses two tools in practice:
- **Read** — to read local skill files when running a local audit (Mode B)
- **web_fetch** — to retrieve remote SKILL.md content for pre-download audits (Mode A)

Neither tool grants shell access, file write access, or credential access. The skill does not call Bash, does not write files, and does not read environment variables or system paths.

**Scripts**

There are no scripts bundled with this skill. The `references/` directory contains two markdown files — `security-checks.md` and `report-format.md` — which are documentation only. No `.py`, `.sh`, `.js`, or `.bash` files are present.

**Prompt injection**

The SKILL.md does not attempt to override Claude's safety behaviour, does not claim special Anthropic permissions, and does not instruct Claude to conceal anything from the user. Every instruction in the file relates directly to the stated purpose: auditing skill files.

**Source provenance**

This skill was built by [mtthwmllr](https://github.com/mtthwmllr) and published directly to this repository. There is no mirror or aggregator involved.

**Self-audit verdict: Appears Safe.**

The two tools this skill uses (Read and web_fetch) are appropriate to its function. No scripts, no credential access, no prompt injection patterns.

---

## Contributing / issues

Found a gap in the checks, or a false positive? Open an issue at [github.com/mtthwmllr/skill-safety-auditor/issues](https://github.com/mtthwmllr/skill-safety-auditor/issues).

Pull requests welcome for new check categories or improvements to the remedy guidance.

---

## Licence

MIT — see [LICENSE](./LICENSE)
