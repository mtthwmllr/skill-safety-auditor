# Verify a Recently Installed Skill Is Safe

## Problem Description

A developer on your team installed a Claude Code skill last week from a trusted colleague's GitHub repo. Now your security team has asked everyone to verify that all installed skills are safe, as part of a new audit policy. You need to audit the skill and produce documentation confirming it was reviewed.

The skill was installed and its files are provided below. Treat these as files from the installed skills directory on the local system.

## Input Files

Extract these files before beginning:

=============== FILE: installed-skill/SKILL.md ===============
---
name: git-commit-summarizer
description: Summarizes recent git commits into a human-readable changelog entry. Use when preparing release notes or summarizing recent changes.
allowed-tools: Bash Read
---

# Git Commit Summarizer

Reads recent git commit messages and produces a formatted changelog section.

## How to Use

Ask me to summarize commits since a given date or tag. I'll run git log to fetch the messages and format them into a readable changelog entry.

## What I Do

1. Run `git log` with appropriate flags to fetch commit messages
2. Group commits by type (feat, fix, docs, etc.)
3. Format into a changelog-style markdown block
4. Return the result directly — no files are written unless you ask

## Limitations

- Only reads commits from the current repository
- Does not access remote repos or external services
- Requires git to be installed
=============== END FILE ===============

## Output Specification

Produce a file called `compliance-audit.md` containing:
- The overall safety verdict
- The transparency notice appropriate for auditing an already-installed skill
- All checks performed and their results (both findings and clean checks)
- A list of what was reviewed
- The standard reminder about static analysis limitations

The compliance team will use this document as evidence that the skill was reviewed. Make it thorough enough to stand on its own.
