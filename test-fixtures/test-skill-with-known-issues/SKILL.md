---
name: demo-analytics-helper
version: 0.9.2
description: >
  Aggregates usage metrics from your project directory and submits a
  weekly summary to the Acme Analytics dashboard. Tracks file counts,
  edit frequency, and language distribution across your workspace.
author: acme-devtools
allowed-tools:
  - Bash
  - Read
  - Glob
  - Write
---

# Demo Analytics Helper

Helps engineering teams understand how they're spending their editing time by
aggregating lightweight metrics from your working directory and forwarding a
weekly digest to the Acme Analytics dashboard.

## How it works

1. Scans your project directory for recently modified files using `Glob`.
2. Counts file types, directory depth, and rough edit frequency via `Bash`.
3. Writes a local summary file (`analytics-summary.json`) to disk using `Write`.
4. Runs `scripts/analytics.py` to POST the summary to the Acme Analytics API.

## Setup

Set the following environment variables before first use:

```
export ACME_API_KEY=your-api-key-here
export PROJECT_DIR=/path/to/your/project
```

## Usage

Once configured, invoke this skill in Claude Code:

```
/demo-analytics-helper
```

Claude will scan the current directory, generate a summary, and submit it.
You will receive a confirmation once the weekly digest has been accepted.

## Privacy

All metric data is aggregated locally before transmission. Individual file
contents are never read or transmitted — only filenames, counts, and
timestamps are included in the payload.

## Requirements

- Python 3.8+
- `requests` library (`pip install requests`)
- Valid Acme Analytics account and API key
