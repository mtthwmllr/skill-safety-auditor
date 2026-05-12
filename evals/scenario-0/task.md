# Evaluate a Community Skill Before Installing

## Problem Description

A developer on your team has found a Claude Code skill on GitHub and wants to install it to help automate pull request reviews. Before anyone on the team installs it, you've been asked to check it for safety risks.

The skill is hosted at the following GitHub repository:

```
https://github.com/tessl-labs/tessl-skill-eval-scenarios
```

You need to produce a safety report that the team lead can review before approving the install. The report should be thorough enough that a non-technical manager could understand the risk level and make an informed decision.

## Output Specification

Produce a file called `audit-report.md` containing the full safety report. The report should include:
- The overall safety verdict (clearly stated)
- A transparency notice appropriate to the audit method used
- All findings (any warnings or critical issues) with explanations
- A clear list of what was reviewed and what was not
- A reminder about the limitations of a static audit

Also produce a file called `audit-log.md` documenting:
- Which URL(s) you fetched during the audit
- Which mode you used and why
- Which checks triggered findings (if any) and which did not
