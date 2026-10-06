# Contributing

Install [uv](https://docs.astral.sh/uv/) and prepare the checkout:

```sh
make bootstrap
uv run --no-env-file pre-commit install --install-hooks
```

`make bootstrap` installs locked dependencies. In a linked worktree it may link
the primary checkout's ignored `.env` if one exists and creates an ignored
`.env.worktree` for local settings. Neither file is loaded by this library.
The command does not replace an existing local `.env`.

Run `make check` for non-mutating lint, format, type, dependency and workflow
checks. Run `make verify` before proposing changes; it also runs tests, builds
the distributions and checks the documentation. Run `make hooks` after changes
to apply the repository's pre-commit hooks.

The source code lives in `src/reuters_style/`; tests live in `tests/`.
Document public behavior in `docs/` and add an `Unreleased` changelog entry
for user-facing changes.

## Documentation

Use `make docs-check` to build the Sphinx documentation with warnings treated
as errors, or `make serve-docs` to preview it locally. The documentation
workflow builds on pull requests and checks external links weekly. Publishing
to the existing documentation URL requires a protected `docs-production`
environment, AWS OIDC role and `DOCS_DEPLOY_ENABLED=true` repository variable.

## Releases

Follow [RELEASING.md](RELEASING.md). A version tag triggers trusted PyPI
publication; do not create a tag until the PyPI trusted publisher is configured
and the release is approved.
