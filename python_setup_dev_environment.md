# Setup Development Environment

<!-- TOC -->

- [Setup Development Environment](#setup-development-environment)
  - [Download \& Install Python](#download--install-python)
  - [Microsoft VS Code](#microsoft-vs-code)
    - [Extensions](#extensions)
    - [Settings (My Personal preferences)](#settings-my-personal-preferences)
    - [Custom Shortcuts (My Personal preferences)](#custom-shortcuts-my-personal-preferences)
  - [Virtual Environment](#virtual-environment)
    - [Conflict between different versions](#conflict-between-different-versions)
    - [`venv`](#venv)
      - [Creating virtual environment](#creating-virtual-environment)
      - [Reproducing the same environment:](#reproducing-the-same-environment)
      - [Split requirements into multiple files:](#split-requirements-into-multiple-files)
      - [Specify the Python version used in the `venv`](#specify-the-python-version-used-in-the-venv)
    - [VS Code and Python Interpreter](#vs-code-and-python-interpreter)

<!-- /TOC -->

## Download & Install Python
- (Arabic) YouTube video
- Commands used
  ```bash
  # List installed versions of Python
  py -0
  py --list

  # List installed versions of Python with their path
  py -0p

  # Start Python interactive shell
  python
  ```
  ```py
  # Hello world
  print("Hi, Ahlan")
  ```

## Microsoft VS Code
### Extensions
- Python extensions
  - Python
    - Pylance
    - Python Debugger
  - Jupyter: for notebooks support
  - isort: Import organization support for Python files using isort.
  - Black Formatter: Formatting support for Python files using the Black formatter
    ```bash
    # check whether black is installed or not
    pip freeze | findstr black # window
    pip freeze | grep black # linux

    # install black package if not installed
    pip install black
    ```
  - Extra:
    - Ruff

- Other extensions
  - Code Spell Checker: Spelling checker for source code
  - Remote Development: An **extension pack** that lets you open any folder in a container, on a remote machine, or in WSL and take advantage of VS Code's full feature set.
  - Docker
  - Rainbow CSV: Highlight CSV and TSV files, Run SQL-like queries

### Settings (My Personal preferences)
```json
{
    /////////////////////////////
    // Terminal
    /////////////////////////////
    "terminal.integrated.fontSize": 22,
    "terminal.integrated.drawBoldTextInBrightColors": true,
    "terminal.integrated.fontWeightBold": "normal",

    /////////////////////////////
    // Editor
    /////////////////////////////
    "editor.fontSize": 20,
    "editor.wordWrap": "on",
    "editor.mouseWheelZoom": true,
    "editor.bracketPairColorization.enabled": true,
    "editor.formatOnSave": true,
    "editor.minimap.autohide": true,
    "editor.minimap.size": "fit",
    "editor.rulers": [
        {
            "column": 115,
            "color": "#ffe683"
        },
        {
            "column": 130,
            "color": "#fd7c7c"
        }
    ],

    /////////////////////////////
    // File-Specific Settings
    /////////////////////////////
    "files.insertFinalNewline": true,
    "files.trimTrailingWhitespace": true,

    // PYTHON
      "python.formatting.provider": "black",
      "python.languageServer": "Pylance",
    "[python]": {
        "editor.codeActionsOnSave": {
            // requires black package
            "source.organizeImports": "explicit"
        },
        "editor.defaultFormatter": "ms-python.black-formatter"
    },
    "notebook.lineNumbers": "on",

    /////////////////////////////
    // Colors
    /////////////////////////////
    "workbench.colorCustomizations": {
        "tree.indentGuidesStroke": "#ffd000",
        "minimapSlider.background": "#9effab38",
        "minimapSlider.hoverBackground": "#fdd8702a",
        "tab.activeForeground": "#00aeff",
        "tab.activeBorder": "#7ef859",
        "tab.activeBorderTop": "#7ef859",
    },

    /////////////////////////////
    // Others
    /////////////////////////////

    "workbench.tree.indent": 20,
    "workbench.colorTheme": "Default Dark+",
    "workbench.tree.enableStickyScroll": true,
    "workbench.activityBar.location": "top",
    "workbench.startupEditor": "none"
}

```
### Custom Shortcuts (My Personal preferences)
```json
[
    {
        "key": "alt+x",
        "command": "workbench.action.terminal.runSelectedText"
    },
    {
        "key": "alt+'",
        "command": "python.execInTerminal-icon"
    }
]
```

## Virtual Environment

### Conflict between different versions
```py
"""
pip uninstall pydantic -y
pip install pydantic<2.0
pip install pydantic==2.9.2
"""

from pydantic import BaseSettings


class Settings(BaseSettings):
    env: str = "prod"
    logging_level: str = "INFO"


settings = Settings()

print("Settings Object\n\t", settings)
print("Settings Dict\n\t", settings.dict())
```

### `venv`

#### Creating virtual environment
1. Create a virtual environment named **`.venv`**
   ```bash
   python -m venv .venv
   ```
2. Activate the virtual environment
   ```bash
   .venv/scripts/activate

   .venv/Scripts/Activate.ps1 # PowerShell
   source .venv/bin/activate # Linux
   ```
   - Fix PowerShell execution policy
     ```powershell
     # ⛔ Run with admin user, then restart the vscode
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

     # Extra commands
     Get-ExecutionPolicy -List
     Set-ExecutionPolicy -ExecutionPolicy Undefined -Scope CurrentUser -Force
     ```
3. Deactivate the virtual environment
   ```bash
   deactivate
   ```
4. Installing Python packages
   ```bash
   pip install pydantic # get the latest version
   pip install pydantic==2.9.2 # specify a version
   pip install pydantic==1.10.18 # specify a version
   pip install -U pydantic # update a package to latest
   pip install "requests>=2.31.0,<2.32"
   ```


#### Reproducing the same environment:
- Creating the `requirements.txt` file
  ```bash
  pip freeze > requirements.txt
  ```
- Install all the packages from the `requirements.txt` file
  ```bash
  pip install -r requirements.txt
  ```

#### Split requirements into multiple files:
- The main `requirements.txt` file
  ```
  pydantic==2.9.2
  pandas==2.2.3
  Jinja2==3.1.4
  ```
- The secondary `requirements-dev.txt` file(s)
  ```
  # relative path to this file
  -r ./requirements.txt

  black
  pytest
  ```
  ```bash
  pip install -r requirements-dev.txt
  ```

#### Specify the Python version used in the `venv`
- List all available versions
  ```bash
  py -0
  py -0p # with path to python.exe
  ```

- Creating a virtual environment using Python 3.10
  ```by
  py -3.10 -m venv .venv10
  py -m venv .venv_xyz

  # activate / check the version
  .venv10/Scripts/activate
  py --version
  deactivate

  .venv_xyz/Scripts/activate
  python --version
  deactivate
  ```

### VS Code and Python Interpreter
- Ctrl + Shift + P > Python: Select Interpreter
- Settings
  ```json
  {
    // the Python the extension will read values from when loading the project for the first time
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
  }
  ```

