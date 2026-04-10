## Setup

### Install uv:

[uv](https://docs.astral.sh/uv/) is a Python package manager. We'll use it for all the examples.

#### On Mac/Linux:

`curl -LsSf https://astral.sh/uv/install.sh | sh`

#### On Windows:

`powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

### Install chromium:

```bash
uv run playwright install
```

## Running scripts

```bash
uv run SCRIPTNAME.py
```
