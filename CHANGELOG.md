# Changelog

All notable changes to this project will be documented in this file.

## [1.6.1] — May 2026

### Fixed
- Narrowed B1 (Credential Access) trigger: `~/.config/` alone no longer escalates to CRITICAL — only triggers when combined with credential/token/key/secret patterns. Generic app config paths now correctly classified as B5 (WARNING), preventing false DO NOT INSTALL verdicts.
- Added warning-clearing rule: warnings investigated and found to be false positives no longer count toward the verdict. A skill with all warnings cleared and no CRITICALs now correctly receives APPEARS SAFE.

### Added
- Explicit verdict label table in SKILL.md — exact emoji+phrase required (DO NOT INSTALL / PROCEED WITH CAUTION / APPEARS SAFE)
- Eval scenarios (`evals/`) covering all three audit modes, all check categories, and prompt injection resistance — 97% score, 1.28× uplift

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
