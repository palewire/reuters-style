# Agent Guide

This is an open-source Python library for Reuters editorial formatting.
The existing public API is in `src/reuters_style/__init__.py`; keep its
behavior stable unless a change explicitly calls for it.

## Setup and checks

Use `make bootstrap` to install the locked uv dependency groups. In linked
worktrees, the bootstrap preserves existing local environment files. The
library does not load dotenv files.

- `make check`: non-mutating Ruff, ty, dependency and workflow checks.
- `make verify`: checks, serial pytest, source manifest, distribution build
  and strict Sphinx documentation build.
- `make package-verify PACKAGE=reuters_style`: wheel import and coverage.
- `make hooks`: pre-commit hooks; may format or modify files.

Run pre-commit after edits. Run the relevant tests and docs build when changing
public behavior. Keep tests serial unless parallel execution is useful.

## Project layout

- `pyproject.toml` and `uv.lock`: package metadata and locked dependencies.
- `src/reuters_style/`: package source and typed public API.
- `tests/`: tests for formatting, validation and worktree setup.
- `docs/`: Sphinx documentation and autosummary API reference.
- `Makefile`: local checks and builds.
- `.github/workflows/`: checks, docs, security and release workflows.

Keep development-only tools in dependency groups rather than public runtime
dependencies. Follow Ruff and ty output; do not add a second lint or type
system. Document all function inputs, outputs and examples in Google-style
docstrings. Add a changelog entry for user-facing changes.

## Releases

See `RELEASING.md`. The documentation deploy needs the protected
`docs-production` environment, AWS OIDC variables and
`DOCS_DEPLOY_ENABLED=true`. PyPI publication needs a trusted publisher.
Do not create version tags, releases or deployments without explicit approval.

## Worktrees

Edit only this checkout. Preserve other worktrees and untracked files; do not
run broad cleanup commands. Never commit credentials or generated artifacts.
