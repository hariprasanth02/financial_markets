# EPITA Engineering Tools — Group 1: Financial Markets

A Python package and command-line interface that retrieves stock market quote data from the Finnhub API.

## Project details

- **Group:** Group 1 — Financial Markets
- **Package:** `epita-hari-prasanth-markets`
- **CLI command:** `epita-group1-cli`
- **Version:** `0.1.0`
- **Data provider:** Finnhub
- **Example ticker:** `NVDA` (NVIDIA)

## Features

- Fetches a stock quote from the Finnhub API.
- Reads the API key from the `FINNHUB_API_KEY` environment variable.
- Displays quote details in a formatted terminal table.
- Can be installed as a Python package and run through its CLI entry point.

## Requirements

- Python version supported by `pyproject.toml`
- [`uv`](https://docs.astral.sh/uv/) for dependency and environment management
- A Finnhub API key

## Setup from source

Open PowerShell in the project directory and install the project dependencies:

```powershell
uv sync
```

Create a local `.env` file in the project root. If `.env.template` exists, copy it:

```powershell
Copy-Item .env.template .env
```

Edit `.env` and set your own Finnhub key:

```env
FINNHUB_API_KEY=your_finnhub_api_key_here
```

Do not commit `.env` or share its contents.

## Run the CLI

```powershell
uv run epita-group1-cli
```

## Run the API test script

If `scripts/test_api.py` is present:

```powershell
uv run python scripts/test_api.py
```

## Install and run the published package

The package is published on official PyPI:

https://pypi.org/project/epita-hari-prasanth-markets/

To test the published package outside the source project:

```powershell
$env:FINNHUB_API_KEY = "your_finnhub_api_key_here"
uv run --no-project --with epita-hari-prasanth-markets epita-group1-cli
```

The environment variable is set only for the current PowerShell session. Do not paste the real key into source files, screenshots, reports, or Git commits.

> **Publication note:** The verified package URL is official PyPI, not TestPyPI. If the assignment specifically requires TestPyPI, confirm with the instructor whether official PyPI is acceptable.

## Useful development commands

```powershell
uv sync
uv run epita-group1-cli
uv tree
uv lock
uv build
git status
```

## Secrets and Git

- Keep the real API key in `.env` or a secure environment variable.
- Ensure `.env` is listed in `.gitignore`.
- Commit `.env.template` only when it contains a placeholder, never a real key.
- Never commit API keys, passwords, tokens, or other credentials.

## Typical project files

- `src/` — package source code
- `scripts/` — API tests and diagnostic/debugging scripts
- `pyproject.toml` — package metadata, dependencies, and CLI entry point
- `uv.lock` — locked dependency versions
- `.env.template` — safe environment-variable template
- `Report.md` — project report

The exact repository structure is determined by the files in the project.

## Author

Hari Prasanth Bandla  
EPITA — Group 1, Financial Markets
