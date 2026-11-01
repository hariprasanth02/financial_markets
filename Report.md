# TP 2 — Student Report: Modern Python Tooling & Live API Systems

## Student Information

- **Student Name:** Hari Prasanth Bandla
- **EPITA Login:** `hari-prasanth.bandla`
- **Assigned API Group:** Group 1 — Financial Markets (Finnhub)
- **Date:** 31/10/2026
- **Package name:** `epita-hari-prasanth-markets`
- **CLI command:** `epita-group1-cli`
- **Package repository:** Official PyPI
- **Public package URL:** https://pypi.org/project/epita-hari-prasanth-markets/

> **Submission note:** The lab instructions request publication to TestPyPI. This package was published to official PyPI instead. This report accurately records the repository used; please confirm with the instructor whether official PyPI is accepted as a substitute for the required TestPyPI deployment.

---

## Step 0: Assigned Group Verification

- **Assigned Group:** Group 1
- **Assigned Domain:** Financial Markets
- **API Provider:** Finnhub
- **Assigned EPITA Login:** `hari-prasanth.bandla`
- **API Endpoint:** `GET https://finnhub.io/api/v1/quote?symbol=NVDA`
- **Authentication Header:** `X-Finnhub-Token: <FINNHUB_API_KEY>`
- **Environment Variable:** `FINNHUB_API_KEY`
- **Project Directory:** `epita_group1_markets`
- **Python Distribution:** `epita-hari-prasanth-markets`

### Group members

1. Hemanth Kuttuboyina
2. Hari Prasanth Bandla
3. Gouruprasad Parthiban

---

# Part 1: Environment Isolation with `uv`

## 1. Comparison of `sys.executable` and `sys.prefix`

### Global Python output

Command:

```powershell
python scripts/inspect_env.py
```

Recorded output:

```text
=== OS Executable Path ($PATH) ===
  - C:\Program Files (x86)\VMware\VMware Workstation\bin\
  - C:\WINDOWS\system32
  - C:\WINDOWS
  - C:\WINDOWS\System32\Wbem

=== Active Python Binary (sys.executable) ===
  C:\New folder\Anaconda\python.exe

=== Python Version ===
  3.13.9

=== Virtual Env Prefix (sys.prefix) ===
  C:\New folder\Anaconda

=== Base Prefix (sys.base_prefix) ===
  C:\New folder\Anaconda

=== Is in Virtual Environment? ===
  False

=== Search Paths for Imports (sys.path) ===
  - C:\New folder\epita_group1_markets\scripts
  - C:\New folder\Anaconda\python313.zip
  - C:\New folder\Anaconda\DLLs
  - C:\New folder\Anaconda\Lib
  - C:\New folder\Anaconda
```

### Environment comparison

The global command used the Anaconda interpreter at `C:\\New folder\\Anaconda\\python.exe`, version `3.13.9`. Its `sys.prefix` and `sys.base_prefix` are identical (`C:\\New folder\\Anaconda`), and the diagnostic reports `False` for being inside a virtual environment.

By contrast, the recorded `uv run` diagnostic used the project's `.venv\\Scripts\\python.exe`, version `3.14.8`, and reported `True`. Its `sys.prefix` points to the project `.venv`, while `sys.base_prefix` points to the base Python installation managed by uv.

This demonstrates that the global command and `uv run` use different Python interpreters and environments.

### `uv run` output

The following is the output currently recorded for the `uv` environment:

```text
=== OS Executable Path ($PATH) ===
  - C:\New folder\epita_group1_markets\.venv\Scripts
  - C:\New folder\epita_group1_markets\.venv/Scripts
  - C:\Program Files (x86)\VMware\VMware Workstation\bin\
  - C:\WINDOWS\system32

=== Active Python Binary (sys.executable) ===
  C:\New folder\epita_group1_markets\.venv\Scripts\python.exe

=== Python Version ===
  3.14.8

=== Virtual Env Prefix (sys.prefix) ===
  C:\New folder\epita_group1_markets\.venv

=== Base Prefix (sys.base_prefix) ===
  C:\Users\hari prasanth\AppData\Roaming\uv\python\cpython-3.14-windows-x86_64-none

=== Is in Virtual Environment? ===
  True

=== Search Paths for Imports (sys.path) ===
  - C:\New folder\epita_group1_markets\scripts
  - C:\Users\hari prasanth\AppData\Roaming\uv\python\cpython-3.14-windows-x86_64-none\python314.zip
  - C:\Users\hari prasanth\AppData\Roaming\uv\python\cpython-3.14-windows-x86_64-none\DLLs
  - C:\Users\hari prasanth\AppData\Roaming\uv\python\cpython-3.14-windows-x86_64-none\Lib
  - C:\Users\hari prasanth\AppData\Roaming\uv\python\cpython-3.14-windows-x86_64-none
```

### Analysis

`sys.executable` identifies the Python executable currently running the script. In the recorded `uv` output, it points to the project's `.venv\Scripts\python.exe`.

`sys.prefix` identifies the active Python environment. In the recorded `uv` output, it points to the project's `.venv` directory.

`sys.base_prefix` identifies the base Python installation used to create the virtual environment. Since `sys.prefix` and `sys.base_prefix` are different, `sys.prefix != sys.base_prefix` evaluates to `True`, confirming that the script is running inside a virtual environment.

`uv run` selects and runs the project environment without requiring the user to activate it manually with a shell activation command.

---

# Part 2: Live API Connection & 12-Factor Secret Hygiene

## 1. Git status and secret hygiene

The project uses the following environment-variable configuration:

- `.env` stores the actual local Finnhub API token and must remain private.
- `.env.template` provides placeholder configuration and can be committed.
- `.gitignore` contains `.env` and `.venv/` so that secrets and the virtual environment are not committed.

### Actual Git status and secret-hygiene checks

Commands and recorded outputs:

```powershell
git status
```

```text
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Report.md

no changes added to commit
```

```powershell
git check-ignore .env
```

```text
.env
```

```powershell
git ls-files .env.template
```

```text
(no output)
```

```powershell
git ls-files .env
```

```text
(no output)
```

### Interpretation

- `.env` is ignored by Git, as confirmed by `git check-ignore .env`.
- `.env` is not currently tracked by Git, as `git ls-files .env` produced no output.
- `.env.template` is not currently tracked by Git, as `git ls-files .env.template` produced no output. If the template exists locally, it still needs to be added to Git; if it does not exist, create it with placeholder values only.
- The current working tree has an uncommitted deletion of `README.md` and an untracked `Report.md`. These should be reviewed before committing. Restore `README.md` if its deletion was accidental, and add the report when it is ready.
- No API key or secret value was included in these command outputs.

Do not paste the contents of `.env`, the Finnhub token, or any other secret into this report.

## 2. Live API response

The project successfully called the Finnhub quote endpoint for NVIDIA (`NVDA`).

### CLI execution

Command:

```powershell
uv run epita-group1-cli
```

Recorded output:

```text
╭─ EPITA Engineering Tools - Group 1 ─╮
│  Live Market Data: LIVE_SUCCESS     │
│ ┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓   │
│ ┃ Property       ┃ Value        ┃   │
│ ┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩   │
│ │ status         │ LIVE_SUCCESS │   │
│ │ symbol         │ NVDA         │   │
│ │ company        │ NVIDIA       │   │
│ │ current_price  │ 204.64       │   │
│ │ change         │ -9.02        │   │
│ │ change_percent │ -4.2217      │   │
│ │ high           │ 209.06       │   │
│ │ low            │ 200.9199     │   │
│ │ open           │ 208.94       │   │
│ │ previous_close │ 213.66       │   │
│ │ timestamp      │ 1793390400   │   │
│ └────────────────┴──────────────┘   │
╰─────────────────────────────────────╯
```

### Direct API-client test

Command:

```powershell
uv run python scripts/test_api.py
```

Recorded response:

```python
{
    'status': 'LIVE_SUCCESS',
    'symbol': 'NVDA',
    'company': 'NVIDIA',
    'current_price': 204.64,
    'change': -9.02,
    'change_percent': -4.2217,
    'high': 209.06,
    'low': 200.9199,
    'open': 208.94,
    'previous_close': 213.66,
    'timestamp': 1793390400
}
```

The values above are the recorded response from the test run; stock quote values can change between requests.

## 3. Security analysis

### Why is storing secrets in environment variables superior to putting them in configuration files such as `config.json` or `settings.yaml`?

1. Environment variables separate sensitive credentials from application source code and ordinary configuration files. This reduces the risk of accidentally committing API keys to a Git repository.
2. Different environments, such as development, testing and production, can use different credentials without changing the application code.

### Why are default fallbacks such as `os.getenv("API_KEY", "default")` dangerous for production secrets?

A default fallback can hide a missing-secret configuration problem. The application may continue running with an invalid or unintended credential instead of clearly reporting that the required secret is missing. Required production secrets should be validated, and the application should fail clearly when they are unavailable.

---

# Part 3: Dependency Hygiene & Semantic Versioning

## 1. Dependency tree (`uv tree`)

Command:

```powershell
uv tree
```

Recorded output:

```text
Resolved 16 packages in 1ms
epita-hari-prasanth-markets v0.1.0
├── python-dotenv v1.2.4
├── requests v2.34.2
│   ├── certifi v2026.10.23
│   ├── charset-normalizer v3.5.2
│   ├── idna v3.20
│   └── urllib3 v2.8.0
├── rich v15.0.0
│   ├── markdown-it-py v4.2.0
│   │   └── mdurl v0.1.2
│   └── pygments v2.21.0
└── pytest v9.2.0 (group: dev)
    ├── colorama v0.4.6
    ├── iniconfig v2.3.1
    ├── packaging v26.3
    ├── pluggy v1.7.0
    └── pygments v2.21.0
```

### Direct dependencies

The direct production dependencies shown in the tree are:

- `python-dotenv`
- `requests`
- `rich`

`pytest` is a direct development dependency, shown in the `dev` dependency group.

### Transitive dependencies

Transitive dependencies are installed because a direct dependency requires them.

- `requests` brings in `certifi`, `charset-normalizer`, `idna` and `urllib3`.
- `rich` brings in `markdown-it-py` and `pygments`.
- `markdown-it-py` brings in `mdurl`.
- `pytest` brings in development dependencies including `colorama`, `iniconfig`, `packaging`, `pluggy` and `pygments`.

## 2. Lockfile and SemVer analysis

### Meaning of version specifiers

- `^2.31.0`: Caret notation used by dependency managers such as Poetry. It permits compatible versions from `2.31.0` up to, but not including, `3.0.0`. The equivalent PEP 440 constraint is `>=2.31.0,<3.0.0`.
- `~=2.2.1`: Under PEP 440, it permits versions `>=2.2.1` and `<2.3.0`.
- `==13.7.1`: Requires exactly version `13.7.1`.

These are explanations of the version expressions in the assignment. They are not claims that the current project uses those exact constraints; the actual project constraints are recorded in `pyproject.toml`.

### If an upstream author releases version `3.0.0`, will `^2.31.0` install it?

No. The caret constraint `^2.31.0` excludes versions `3.0.0` and above because its compatible range ends before `3.0.0`. An upgrade operation cannot override the declared version constraint.

### Difference between `pyproject.toml` and `uv.lock`

`pyproject.toml` declares project metadata, direct dependencies and allowed version constraints. `uv.lock` records the exact resolved package versions and associated dependency information so that installations can be reproduced consistently.

### How do SHA-256 hashes in `uv.lock` help protect against supply-chain attacks?

The hashes allow the package manager to verify that a downloaded package artifact matches an expected artifact. If an artifact has been modified or replaced and its hash no longer matches, the integrity check can detect the discrepancy. Hash verification helps protect package integrity, although it does not by itself prove that the original package publisher is trustworthy.

---

# Part 4: Package Build & PyPI Deployment

## 1. Package build and publication details

The project was published to **official PyPI**, not TestPyPI.

- **Package name:** `epita-hari-prasanth-markets`
- **Version:** `0.1.0`
- **CLI command:** `epita-group1-cli`
- **Public package URL:** https://pypi.org/project/epita-hari-prasanth-markets/

The project was built using:

```powershell
uv build
```

This produces a wheel (`.whl`) and a source distribution (`.tar.gz`) in the `dist/` directory.

### External installation and execution verification

**TODO — Paste the actual successful output from the clean-environment installation test.**

The command used for the official PyPI package is:

```powershell
cd $env:TEMP
$env:FINNHUB_API_KEY = "YOUR_FINNHUB_API_KEY"
uv run --no-project --with epita-hari-prasanth-markets epita-group1-cli
```

Do not put the actual API key in this report. The command shown here uses a placeholder. The output should demonstrate that the package was installed from official PyPI and that the CLI successfully retrieved and displayed the live quote.

## 2. Packaging theory

### What is the difference between an sdist (`.tar.gz`) and a Wheel (`.whl`)?

A source distribution (sdist) contains the package's source code and build-related files. It may need to be built during installation.

A Wheel is a built distribution that can generally be installed directly without building the package from source.

### Why are Wheels generally faster and safer to install on client machines?

Wheels are generally faster because they avoid building the package during installation. They also reduce the need for build tools and installation-time build steps, making installation more predictable. A Wheel does not automatically make software secure; users should still install packages from trusted sources and verify package integrity.

---

# Part 5: Professional Debugging Challenge (No `print()` for debugging)

## 1. Root cause analysis

The original debugging script raised the following error:

```text
TypeError: can't multiply sequence by non-int of type 'str'
```

Using the VS Code interactive debugger and Debug Console, the runtime types were inspected:

- `record['volume']`: `str`
- `record['weight']`: `str`

The `split(",")` method returns a list of strings. The original `parse_api_record()` function stored the volume and weight fields directly from that list without converting them to numeric types.

The `compute_weighted_metric()` function then attempted to multiply two strings, which caused the `TypeError`. The original aggregation would also fail when adding a string volume to the numeric `total_volume`.

## 2. Call stack inspection

The function frames involved in the exception were:

1. `compute_weighted_metric()` — attempts to calculate the weighted metric.
2. `aggregate_telemetry()` — loops through records and processes successful entries.
3. `<module>` — runs the main script and calls the aggregation function.

The debugger was used to inspect the values and types at the point of failure.

> **Breakpoint note:** The original program fails on its first successful record (`idx == 0`), before it can reach the weighted-metric line for `idx == 2`. The conditional breakpoint at `idx == 2` can be placed on the record-parsing line to inspect the third record, or the first failure can be inspected at the calculation line. Do not state that the calculation breakpoint was reached at `idx == 2` unless that was actually observed.

## 3. The fix

The `volume` and `weight` values were converted to floating-point numbers inside `parse_api_record()`.

### Original code

```python
"volume": parts[2],
"weight": parts[4]
```

### Corrected code

```python
"volume": float(parts[2]),
"weight": float(parts[4])
```

This conversion allows numeric multiplication and addition, including values that contain decimal places.

## 4. Verified execution output

The corrected script was run with:

```powershell
uv run python scripts/debug_challenge.py
```

Recorded expected output:

```text
Aggregate Result: {
    'successful_entries': 3,
    'total_volume': 650.0,
    'avg_volume': 216.66666666666666,
    'high_impact_count': 1
}
```

The result represents three successful records, a total volume of `650.0`, an average volume of approximately `216.67`, and one record with a weighted impact greater than `500`.

---
