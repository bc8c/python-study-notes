# Development Tools Guide (Black, Ruff, Pytest)

This document explains how to use the development tools included in this project:

- **Ruff** — Linter (code quality checks)  
- **Black** — Code formatter  
- **Pytest** — Test runner  

These tools improve consistency, readability, and reliability of your code.

All tools are installed as development dependencies via Poetry and managed by uv.

---

## 1. Installing Development Tools

Install via Poetry:

```bash
poetry add --group dev black ruff pytest
uv sync
```

`uv sync` installs everything into the automatically managed virtual environment.

---

## 2. Ruff — Linter

Ruff checks code for mistakes and enforces best practices.  
It detects issues such as:

- Unused imports, unused variables  
- Missing whitespace, formatting issues (E, W rules)  
- Undefined variables, logical issues (F rules)  
- Common error patterns detected by Flake8 families  

### Run Ruff

```bash
uv run ruff check .
```

### Auto-fix simple issues

```bash
uv run ruff check . --fix
```

---

## 3. Black — Formatter

Black formats Python code automatically with a consistent style.

### Format the entire project

```bash
uv run black .
```

### Format a single file

```bash
uv run black basics/example.py
```

Black focuses exclusively on code formatting.

---

## 4. Pytest — Test Runner

Example test file: `tests/test_sample.py`

```python
def test_addition():
    assert 1 + 1 == 2
```

### Run tests

```bash
uv run pytest
```

Pytest automatically discovers `test_*.py` files.

---

## 5. Recommended Workflow

```
1. Write code
2. Save → Black formats the file (if enabled in VS Code)
3. Check code quality:
   uv run ruff check .
4. Auto-fix minor issues:
   uv run ruff check . --fix
5. Run tests:
   uv run pytest
```

This workflow keeps your code consistent, clean, and safe.

---

## 6. Recommended pyproject.toml configuration (Ruff + Black)

To avoid conflicts between **Ruff** and **Black**, and to enable useful lint rules such as `F841` (unused variable),  
add the following configuration sections to your `pyproject.toml`.

```toml
[tool.black]
line-length = 88
target-version = ["py312"]

[tool.ruff]
line-length = 88
target-version = "py312"

[tool.ruff.lint]
# E: pycodestyle rules
# F: Pyflakes rules (includes unused variables)
select = ["E", "F"]
ignore = []
```

### Why this configuration is recommended

- Black and Ruff share the same `line-length` to prevent formatting conflicts.  
- Black remains the **only** formatter.  
- Ruff focuses exclusively on linting, using `E` and `F` rules.  
- Adding `"F"` enables checks like `F841`, which are not enabled by default.  

This setup ensures stable, predictable formatting and consistent linting behavior.

---

# 7. VS Code Integration (UI-First Setup)

VS Code works seamlessly with Ruff, Black, and Pytest.  
Below is a recommended setup using **UI settings only** (no manual editing of `settings.json` required).

---

## 7.1 Select Python Interpreter (.venv) — **Required**

This ensures VS Code uses your project's environment.

1. `Ctrl + Shift + P`  
2. **Python: Select Interpreter**  
3. Choose the interpreter inside `.venv`

---

## 7.2 Configure Black Formatter (VS Code + local `.venv` Black)

Black is installed as a development dependency inside this project’s `.venv`.  
VS Code can format Python files using Black, but modern VS Code versions **require the Black Formatter extension** and no longer use the old Python-extension formatting settings.

This section ensures:

- Black Formatter *extension* is installed  
- But Black execution uses **this project's `.venv` Black**, not a global or bundled one

---

### 7.2.1 Install the Black Formatter extension

1. `Ctrl + Shift + X`  
2. Search: **Black Formatter**  
3. Install the extension published by **Microsoft** (`ms-python.black-formatter`)

VS Code now recognizes “Black” as an available formatter.

---

### 7.2.2 Enable formatting in the UI

1. Open **Settings** (`Ctrl + ,`)
2. Search **Format On Save**
3. Enable **Editor: Format On Save**

(This controls *when* formatting happens, not which formatter is used.)

---

### 7.2.3 Use the project's `.venv` Black (recommended)

By default, the Black Formatter extension runs its **bundled** Black version.  
To ensure consistent formatting with `uv run black`, we point VS Code to the Black inside `.venv`.

1. `Ctrl + Shift + P`
2. Run: **Preferences: Open Workspace Settings (JSON)**
3. Add (or merge) the following:

```jsonc
{
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true
  },

  // Force Black to be executed from this project's .venv
  "black-formatter.path": [
    "${workspaceFolder}/.venv/Scripts/python.exe",
    "-m",
    "black"
  ]
}
```

**macOS/Linux users:**  
Replace the path with:

```json
"black-formatter.path": [
  "${workspaceFolder}/.venv/bin/python",
  "-m",
  "black"
]
```

---

### 7.2.4 Confirming Black is active

After saving the settings:

- `Shift + Alt + F` formats the file  
- Saving (`Ctrl + S`) auto-formats  
- Formatting output matches:

```bash
uv run black .
```

Because both VS Code and the CLI now use **the exact same Black binary** inside `.venv`.

---

### 7.2.5 Why JSON is needed (important)

Modern VS Code does **not** automatically detect formatters inside `.venv`.  
The UI alone cannot select:

- Which Black binary to use  
- Which Python environment provides it  

Thus:

> **UI = enables formatting**  
> **JSON = tells VS Code exactly which Black to run**

This ensures deterministic, project-local, CI-compatible formatting.




---

## 7.3 Enable Ruff Linting — **Extension required**

Ruff is used only for **linting** in this project (no auto-fix on save).

Install the official Ruff extension to enable real-time linting inside VS Code.

### UI Steps

1. Press `Ctrl + Shift + X`
2. Search **“Ruff”**
3. Install the extension published by **Astral / charliermarsh.ruff**

Once installed:

- Ruff automatically runs when you open or edit Python files
- Lint errors and warnings appear in the **Problems** panel
- No additional configuration is required for lint-only usage

Ruff will *not* modify files automatically unless you run:

```bash
uv run ruff check . --fix
```
This keeps Ruff focused purely on reporting issues during development.

---

## 7.4 Pytest Integration (Optional)

VS Code can automatically detect and run tests written with **pytest**.

### Enable Pytest Support

1. Press `Ctrl + Shift + P`
2. Run **Python: Configure Tests**
3. Select **pytest** as the test framework
4. Choose your test folder (e.g., `tests/`)

After configuration:

- VS Code will show test cases in the **Testing** sidebar
- You can run or debug individual tests directly from the editor
- Test output will appear in the built-in Test Results panel

This step is optional, but helpful if you plan to write automated tests.

---

## Summary

Ruff checks code quality and catches mistakes.  
Black formats code consistently.  
Pytest runs automated tests.  
All tools run using `uv run`, requiring no manual virtual environment activation.  

This setup ensures clean, safe, and maintainable Python code across the entire repository.
