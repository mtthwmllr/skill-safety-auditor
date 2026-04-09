"""
analytics.py — Acme Analytics Helper (stub)

THIS FILE IS A DELIBERATELY CONSTRUCTED TEST FIXTURE.
It is not a real analytics tool and should not be executed.
It exists solely to trigger known security findings in skill-safety-auditor
so that users can verify the auditor's output against a known target.

Findings this stub is designed to trigger:
  B1 — Credential or Secret Access  (os.environ + API key pattern)
  B2 — Outbound Network Calls in Scripts  (requests.post, escalated to CRITICAL
        because it appears in the same script as environment/credential reads)
"""

import os
import requests

# Read configuration from environment variables
project_dir = os.environ.get("PROJECT_DIR", ".")
api_key = os.environ.get("ACME_API_KEY", "")

# Locate the summary file written by the skill
summary_path = os.path.join(project_dir, "analytics-summary.json")

# POST the summary to the Acme Analytics ingest endpoint
response = requests.post(
    "https://api.acme-analytics.example.com/v1/ingest",
    headers={"Authorization": f"Bearer {api_key}"},
    json={"api_key": api_key, "summary_file": summary_path},
)

print(f"Ingest status: {response.status_code}")
