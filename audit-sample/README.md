# audit-sample

Contains a sample report produced by `skill-safety-auditor` to demonstrate
the format and range of findings the tool can surface.

## About the sample

The report in `sample-report.md` was produced by auditing the purpose-built
test skill at `test-fixtures/test-skill-with-known-issues/`.

**Previous version:** The original sample was produced against a live public
third-party skill (`hundred-million-offers` from wondelai/skills). That report
only produced warnings (no critical findings) and referenced an external source
that readers could not easily verify themselves.

**Current version:** The sample now audits a test fixture that lives in this
repository. This means:

- Anyone can verify the report by running the auditor against the same target
- No third-party skill or author is implicated
- The report shows a more complete range of findings (Criticals + Warnings + Passes)
- The test fixture is stable and won't change unexpectedly

See `test-fixtures/README.md` for a full description of the fixture and how to
use it to verify the auditor's output on your own machine.
