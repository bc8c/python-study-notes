# Environment Setup (uv + Poetry)

This repository uses a modern Python workflow powered by **uv** and **Poetry**.

- **Poetry** manages dependencies through `pyproject.toml`.
- **uv** installs Python, syncs dependencies, and runs commands extremely fast.
- Virtual environments are **automatically created** by `uv sync` (no manual venv needed).

---

## 1. Install Poetry

> **Windows Note:**  
> Run these commands in **Windows PowerShell (outside VS Code)**.  
> The VS Code terminal may not detect pipx or PATH updates until it is restarted.

Recommended installation using pipx:

```bash
pip install --user pipx
pipx ensurepath
pipx install poetry
```

Check:

```bash
poetry --version
```

---

## 2. Install uv

**macOS / Linux**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows PowerShell**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Check installation:

```bash
uv --version
```

---

## 3. Initialize the Project Environment

Before using `uv sync`, the project needs a `pyproject.toml` file that defines dependencies and metadata.

This repository uses **Poetry** to create and manage the `pyproject.toml`.

From the project root:

```bash
poetry init
```

Follow the prompts (you may skip optional fields or accept defaults).  
This command will generate a `pyproject.toml` file.

### Configure the project for non-package mode

Since this repository is used for learning and is **not** intended to be installed as a Python package,  
both Poetry and uv must be configured to avoid building the project as a package.

Add the following sections to your `pyproject.toml`:

```toml
[tool.uv]
package = false

[tool.poetry]
package-mode = false
```

This ensures:

- Poetry does not attempt to build the project as a package  
- uv does not attempt an editable installation  
- `uv sync` installs only dependencies and manages the virtual environment cleanly

### Initialize the environment

After updating `pyproject.toml`, run:

```bash
uv sync
```

`uv sync` will:

- Create the virtual environment automatically  
- Install all dependencies listed in `pyproject.toml`  
- Generate a `uv.lock` file for reproducible environments


---

## 4. Adding Dependencies

To add a standard Python dependency:

```bash
poetry add requests
uv sync
```

To add development tools (formatter, linter, test runner):

```bash
poetry add --group dev black ruff pytest
uv sync
```

For detailed explanations of Black, Ruff, and Pytest — including workflow and VS Code integration —  
please refer to:

**[Development Tools Guide](./tools.md)**

---

## 5. Running Scripts with uv

Run any Python script:

```bash
uv run python basics/01_example.py
```

Run development tools:

```bash
uv run ruff check .
uv run black .
uv run pytest
```

uv automatically handles environment activation and runs all tools inside the correct `.venv`.

For tool-specific commands, examples, and recommended workflows, see:

**[Development Tools Guide](./tools.md)**


---


## Summary Workflow

```
poetry add X        # Add a dependency
poetry add --group dev Y
uv sync             # Sync env + install everything
uv run python file.py
```

This setup keeps the environment clean, reproducible, and fast.
