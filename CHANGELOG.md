# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] — April 2026

### Added
- Initial release of `skill-safety-auditor`
- Two audit modes: Pre-download (Mode A) and Local file (Mode B)
- 14 security checks across 4 categories: Frontmatter, Script Content, Prompt Injection, Source Provenance
- Structured report template with severity tiers: Critical / Warning / Info
- Interactive remedy walkthrough — guides users step by step through clearing each warning
- Bundled reference files: `security-checks.md` and `report-format.md`
- Support for all common skill install methods: GitHub URLs, git clone, npx, npm, pip, curl/wget, marketplace names, .skill files
