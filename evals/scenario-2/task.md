# Pre-Install Check for a New Productivity Skill

## Problem Description

A product manager at your company wants to install a Claude Code skill to help the team generate weekly status reports automatically. She found it recommended in a Slack community but isn't technical enough to evaluate it herself. She's asked you to check it before she installs it on her machine.

She's already downloaded the skill file but hasn't installed it yet. The SKILL.md has been extracted and is provided below.

Your job is to produce a clear, jargon-free safety assessment she can read and understand.

## Input Files

Extract this file before beginning:

=============== FILE: extracted-skill/SKILL.md ===============
---
name: weekly-report-generator
description: Generates formatted weekly status reports from your notes and tasks.
allowed-tools: Read Write Bash WebFetch Glob Edit
---

# Weekly Report Generator

Helps you create professional weekly status reports. Point me at your notes folder and I'll generate a polished report.

## How It Works

1. Read your notes from the provided directory
2. Use the reporting script to format them:

```
scripts/format_report.sh
```

3. Optionally fetch team member status from your company wiki (provide the URL)
4. Write the final report to `weekly-report.md`

## Tips

- Works best with markdown note files
- Can pull from multiple directories
=============== END FILE ===============

=============== FILE: extracted-skill/scripts/format_report.sh ===============
#!/bin/bash
# Format notes into a weekly report

NOTES_DIR="${1:-./notes}"
OUTPUT="weekly-report.md"

# Read all markdown files
echo "# Weekly Status Report" > "$OUTPUT"
echo "Generated: $(date)" >> "$OUTPUT"

# Check for config
if [ -f ~/.config/report-tool/config.json ]; then
    source ~/.config/report-tool/config.json 2>/dev/null
fi

find "$NOTES_DIR" -name "*.md" | while read f; do
    cat "$f" >> "$OUTPUT"
done

echo "Report written to $OUTPUT"
=============== END FILE ===============

## Output Specification

Produce a file called `safety-check.md` containing a complete safety report with:
- A clear verdict the product manager can act on immediately
- Each warning or issue explained in plain English (no jargon)
- Specific remediation steps she should take before deciding whether to install
- What was reviewed and what wasn't
