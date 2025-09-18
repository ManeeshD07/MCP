# MCP Server and Client

Minimal MCP server (`main.py`) with a companion client (`client.py`). Use `uv` for reproducible environments and the MCP CLI for running and inspecting the server.

## Requirements
- Python 3.13 (see `.python-version`)
- `uv` package manager

## Setup
```bash
uv sync
```
This creates `.venv/` and installs dependencies from `pyproject.toml` / `uv.lock`.

## Run the Server
- Inspector (recommended during development):
  - `uv run mcp dev main.py`
  - Opens the MCP Inspector to explore tools/resources and send test requests.
- Direct run (no Inspector):
  - `uv run mcp run main.py`
  - For SSE transport: `uv run mcp run -t sse main.py`

## MCP Inspector Testing
Use the Inspector to discover and exercise your server’s tools/resources.

1) Launch with your server file:
```bash
uv run mcp dev main.py
# or if you expose a server object named app
uv run mcp dev main.py:app
```

2) Explore capabilities:
- Tools: open the Tools panel, pick a tool, provide params, and Execute.
- Resources: browse available resources (if your server provides any) and Fetch.
- Logs: watch request/response payloads and errors in the Logs panel.

3) Iterate on changes:
- Edit the server, then stop and rerun the command above to refresh the Inspector.
- If the Inspector shows a reload option, use it after saving files.

Notes
- The `file_spec` can be a path (`main.py`) or an import target (`main.py:app`).
- Ensure your module starts or exports an MCP server (e.g., calls `server.run()` or provides a server object) for tools/resources to appear.

## Run the Client
```bash
uv run python client.py
```
- If your client connects via SSE, start the server first with `-t sse`.
- If your client uses stdio to spawn the server, no separate server process is required.

## Project Structure
- `main.py`: MCP server entrypoint.
- `client.py`: Sample client that accesses the server.
- `pyproject.toml`: Project metadata and dependencies (`mcp[cli]`).
- `uv.lock`: Locked dependency versions (managed by `uv`).

## Development & Testing
- Add tests with `pytest`:
  - `uv add --dev pytest`
  - `uv run pytest -q`
- Style (optional): add Black/Ruff config to `pyproject.toml`, then `uv run black .` and `uv run ruff check .`.

## Troubleshooting
- Use `uv run ...` to ensure the virtualenv and deps are active.
- Verify Python version: `uv run python -V` should show 3.13.

## Contributing
See `AGENTS.md` for coding style, testing expectations, and PR guidelines.
# MCP
# MCP
