---
title: Skill Safety Auditor
type: case-study
tags: [security, ai-tooling, claude-code, technical-writing, product-design]
links:
  github: https://github.com/mtthwmllr/skill-safety-auditor
  resource: https://www.publicgoodalliance.org/digital-products/skill-safety-auditor
---

## The problem

The Claude Code skills ecosystem was growing fast with no standard safety tooling. Users were installing third-party skills without any way to review them for credential theft, shell access, or prompt injection attacks — the same risks that plagued browser extensions a decade ago, repeating in a new context.

## What I built

A Claude Code skill that audits other skills before or after installation. It runs 14 security checks across frontmatter, bundled scripts, prompt injection patterns, and source provenance, then produces a structured report with severity ratings and step-by-step remedies written for non-technical users. It works in two modes: pre-download (reviews remote files before anything touches your machine) and local (reviews files already on disk).

## The process

- Identified the security gap by surveying the skills ecosystem and reviewing research on AI tooling attack surfaces
- Designed the audit taxonomy from scratch — 4 check categories, 3 severity tiers, 14 individual checks with plain-language remedies for each
- Built and iterated the skill using Claude Code's skill-creator framework, validated against real edge cases
- Ran a live audit of a real public skill from wondelai to test the output format and confirm the checks fired correctly

## What makes it interesting

The skill audits itself. Its own README walks through every one of the auditor's checks applied to the auditor's own files — publicly, with the findings acknowledged. The one flag it raises (no `allowed-tools` declared) is explained in full. It's the kind of intellectual honesty that makes a security tool worth trusting: eating its own cooking in public rather than asking users to take it on faith.

## Skills demonstrated

Security thinking · Technical writing · AI tooling · Product design · Claude Code skills ecosystem

---

[See the skill →](https://github.com/mtthwmllr/skill-safety-auditor) &nbsp;&nbsp; [Read the full resource →](https://www.publicgoodalliance.org/digital-products/skill-safety-auditor)
