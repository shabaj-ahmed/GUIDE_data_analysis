# GUIDE Data Analysis

This repository contains the Python analysis pipeline for the GUIDE survey study.

The survey was conducted with:

1. People with dual sensory loss, including people with combined sight and hearing impairment.
2. Carers or supporters of people with dual sensory loss.

The aim of the analysis is to understand how participants access visual or auditory travel information, the barriers they experience when using buses, and whether vibration-based or haptic navigation support may improve confidence, independence, and journey safety.

## Current response counts

| Survey group                  | Current responses |
| ----------------------------- | ----------------: |
| People with dual sensory loss |                42 |
| Carers                        |                11 |

## Expected input format

Export the survey data as **CSV UTF-8**.

Place the exported files in:

```text
data/raw/
```

The expected filenames are:

```text
data/raw/GUIDE_deafblind_participants_results.csv
data/raw/GUIDE_carers_results.csv
```

The project expects these filenames by default.

CSV files can be inspected in VS Code using the **Edit CSV** extension.

## Project structure

```text
GUIDE_data_analysis/
├── README.md
├── pyproject.toml
├── .gitignore
├── data/
│   └── raw/
│       └── .gitkeep
├── outputs/
│   ├── preprocessing/
│   ├── tables/
│   │   └── .gitkeep
│   └── qualitative/
│       └── .gitkeep
└── src/
    └── guide_analysis/
        ├── __init__.py
        ├── __main__.py
        ├── cli.py
        └── survey_processing/
            ├── __init__.py
            ├── columns.py
            ├── preprocessing.py
            ├── processor.py
            └── summaries.py
```

## Folder and file guide

| Path                                                    | Purpose                                                                    |
| ------------------------------------------------------- | -------------------------------------------------------------------------- |
| `data/raw/`                                             | Raw survey CSV exports.                                                    |
| `outputs/preprocessing/`                                | Preprocessing outputs, including duration summaries and flagged responses. |
| `outputs/tables/`                                       | Planned location for categorical, multi-select, and rating summary tables. |
| `outputs/qualitative/`                                  | Planned location for open-ended responses prepared for thematic coding.    |
| `src/guide_analysis/cli.py`                             | Defines the command-line interface.                                        |
| `src/guide_analysis/survey_processing/preprocessing.py` | Contains duration parsing, summary, and threshold flagging logic.          |
| `src/guide_analysis/survey_processing/processor.py`     | Coordinates the analysis pipeline and writes output files.                 |
| `src/guide_analysis/survey_processing/summaries.py`     | Contains reusable loading and cleaning helper functions.                   |

## Setup

Create and activate a virtual environment.

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

On Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

Install the project and development tools:

```bash
python -m pip install -e ".[dev]"
```

## Development commands

Format the code:

```bash
black src
```

Lint the code:

```bash
ruff check src
```

Automatically fix some lint issues:

```bash
ruff check src --fix
```

Type check the code:

```bash
mypy src
```