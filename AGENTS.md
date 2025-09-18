# Repository Guidelines

## Project Structure & Module Organization
- Root entrypoint: `main.py` (CLI/startup for the MCP server).
- Project config: `pyproject.toml` (name, Python version, deps).
- Lockfile: `uv.lock` (managed by `uv`).
- Virtual env: `.venv/` (created by `uv sync`).
- Tests (add as needed): `tests/` with `test_*.py` files.

## Build, Test, and Development Commands
- Install deps: `uv sync` — creates `.venv` and installs from `pyproject.toml`/`uv.lock`.
- Run app: `uv run python main.py` — starts the local entrypoint.
- Add dev tool (example): `uv add --dev pytest` — adds a dev dependency.
- Run tests (after adding pytest): `uv run pytest -q` — executes test suite.

## Coding Style & Naming Conventions
- Python style: follow PEP 8; 4‑space indentation.
- Naming: `snake_case` for functions/variables, `PascalCase` for classes, modules lower_snake.
- Imports: standard lib → third‑party → local, grouped with blank lines.
- Formatting tools are not yet configured; if adding Black/Ruff, configure in `pyproject.toml` and run via `uv run black .` / `uv run ruff check .`.

## Testing Guidelines
- Framework: prefer `pytest` with tests under `tests/` named `test_*.py`.
- Scope: add tests for new features and regressions; cover critical paths.
- Quick start: `uv add --dev pytest` then `uv run pytest`.

## Commit & Pull Request Guidelines
- Commits: follow Conventional Commits.
  - Examples: `feat: add healthcheck endpoint`, `fix: handle missing env var`, `chore: update deps`.
- PRs: include a clear description, linked issue (if any), steps to reproduce/verify, and screenshots or logs when relevant.
- Keep PRs focused and small; add checklists for testing and docs updates.

## Security & Configuration Tips
- Runtime: Python `3.13` (see `.python-version`). Use `uv` for reproducible environments.
- Secrets: never commit tokens or keys; load via environment variables and document required vars in `README.md`.
- Dependencies: prefer `uv add` to keep `uv.lock` up to date.
