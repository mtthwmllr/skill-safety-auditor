# Changelog

All notable changes to this project will be documented in this file.

## [1.6.0] — May 2026

### Changed
- Refactored three workflows into a shared Audit Procedure section — each mode now only specifies its unique setup steps
- Consolidated three inline transparency notices into a single lookup table
- Collapsed Known Risks and Self-Audit Limitation into one inline note
- Removed Common Install Methods Reference section (duplicated Workflow 1 resolution table)
- Collapsed speculative resolution rows (npm, pip, marketplace) into a single fallback entry
- Tightened Fetch Safety Boundary to explicitly cover credential values in fetched content (W007)
- SKILL.md reduced from ~300 lines to 131 lines

### Fixed
- Declared `references/` files as docs in tile.json so Tessl bundler includes them
- Renamed `.tileignore` to `.tesslignore` (deprecation fix)
- Excluded `test-fixtures/` from published bundle via `.tesslignore`
- Fixed allowed-tools format (`Read,WebFetch,Glob` → `Read WebFetch Glob`)
- Added `tile.json` and publish workflow (tile was not previously auto-publishing)

### Added
- `references/index.md` as docs entrypoint linking security-checks.md and report-format.md
- Known risks documentation for Tessl security findings W007, W011, W012

## [1.0.0] — April 2026

### Added
- Initial release of `skill-safety-auditor`
- Three audit modes: Pre-download (Mode 1), Downloaded not installed (Mode 2), Already installed (Mode 3)
- 14 security checks across 4 categories: Frontmatter, Script Content, Prompt Injection, Source Provenance
- Structured report template with severity tiers: Critical / Warning / Info
- Bundled reference files: `security-checks.md` and `report-format.md`
- Support for all common skill install methods: GitHub URLs, git clone, npx, npm, pip, curl/wget, marketplace names, .skill files
