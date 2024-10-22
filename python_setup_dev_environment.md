# Setup Development Environment

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
