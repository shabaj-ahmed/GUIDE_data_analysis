# GUIDE Data Analysis
This repository contains the Python analysis pipeline for the GUIDE survey study.

The pipeline processes categorical survey data exported as CSV files and generates preprocessing outputs, descriptive summaries, exploratory comparisons, and figures.

## Study background
The survey was conducted with two respondent groups:
1. People with dual sensory loss, including people with combined sight and hearing impairment.
2. Carers or supporters of people with dual sensory loss.

The aim of the analysis is to understand how participants access visual or auditory travel information, what barriers they experience when using buses, and whether vibration-based or haptic navigation support may improve confidence, independence, and journey safety.

## Setup
Create and activate a virtual environment.

### On macOS or Linux:
~~~ shell
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
~~~

### On Windows PowerShell:
~~~ shell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
~~~

Install the project and development tools:
~~~ shell
python -m pip install -e ".[dev]"
~~~

### Expected input format
Export the survey data as CSV UTF-8.

Place the exported files in:
~~~
data/raw/
~~~
The expected filenames are:
~~~
data/raw/GUIDE_deafblind_participants_results.csv
data/raw/GUIDE_carers_results.csv
~~~
The project expects these filenames by default.

CSV files can be inspected in VS Code using the Edit CSV extension.

### Running the analysis
Run the analysis from the project root:
~~~ shell
python -m guide_analysis --config config/analysis.toml
~~~
Duration thresholds can be changed in `config/analysis.toml` according to the expected completion time for each survey.

Flagged responses should be reviewed manually before deciding whether to exclude them from the final analysis.

## Data workflow
The raw CSV exports are kept as the source data. The analysis code loads these files into pandas, cleans the data in memory, and then writes preprocessing outputs, summary tables, exploratory cross-tabulations, optional effect size estimates, and figures.

The pipeline writes generated outputs to the `outputs/` directory.

### Preprocessing outputs
The preprocessing stage writes:
~~~
outputs/preprocessing/dataset_overview.csv
outputs/preprocessing/duration_summary.csv
outputs/preprocessing/deafblind_participants__duration_threshold_flags.csv
outputs/preprocessing/carers__duration_threshold_flags.csv
~~~
| Output | Purpose |
|---|---|
| `dataset_overview.csv` | Shows how many responses and columns were loaded for each survey. |
| `duration_summary.csv` | Summarises completion duration for each survey. |
| `deafblind_participants__duration_threshold_flags.csv` | Lists deafblind participant responses outside the chosen duration thresholds. |
| `carers__duration_threshold_flags.csv` | Lists carer responses outside the chosen duration thresholds. |

### Descriptive analysis outputs
The descriptive analysis outputs are:
~~~
outputs/tables/deafblind_participants__categorical_summary.csv
outputs/tables/deafblind_participants__ordinal_summary.csv
outputs/tables/deafblind_participants__rating_distribution.csv
outputs/tables/deafblind_participants__multi_select_summary.csv

outputs/tables/carers__categorical_summary.csv
outputs/tables/carers__ordinal_summary.csv
outputs/tables/carers__rating_distribution.csv
outputs/tables/carers__multi_select_summary.csv
~~~

With additional exploratory analysis and figures in:
~~~
outputs/tables/*__crosstabs.csv
outputs/tables/*__effect_sizes.csv
outputs/figures/*.png
~~~

## Quantitative analysis approach
The pipeline analyses mostly categorical survey data. These variables are treated as either ordinal or nominal categorical data.

Given the exploratory nature of the study and the relatively small sample size, the quantitative analysis focuses on descriptive statistics, exploratory comparisons, and effect size estimation where appropriate.

The aim is to identify meaningful patterns within the data rather than to test formal hypotheses.

### Ordinal categorical data
Ordinal variables have an inherent ordering, such as 1 to 5 rating questions or ordered response categories.

### Nominal categorical data
Nominal variables represent categories without an inherent ordering.

These may be:
- Single-choice questions, where each respondent selects one option.
- Multiple-choice questions, where each respondent may select more than one option.

For multiple-choice questions, each response option is summarised independently because respondents may select more than one option. Percentages are calculated using the number of valid respondents for that question as the denominator, rather than the total number of selections.

## Analysis pipeline
The quantitative analysis is performed in two main stages, with a third optional stage where appropriate.

### Stage 1: Descriptive analysis
Each survey question is analysed independently to summarise participant responses.

This stage may include:
- Number of responses, reported as *n*.
- Frequency counts.
- Percentages.
- Median and mode for ordinal questions.
- Ranking by popularity for nominal questions.
- Appropriate visualisations, such as bar charts, stacked bar charts, or diverging Likert charts.

This stage provides an overview of participant preferences, experiences, and accessibility requirements.

### Stage 2: Exploratory comparisons
Variables that are expected to be related are explored using descriptive cross-tabulations and visualisations.

These comparisons are used to identify observable trends within the sample rather than to establish statistically significant relationships.

### Stage 3: Characterising relationships (optional)
Where exploratory comparisons reveal potentially meaningful relationships, an appropriate effect size may be calculated to estimate the strength of the observed association.

Effect sizes are used to provide additional context for observed trends and are interpreted alongside descriptive statistics and visualisations rather than as evidence of statistical significance.

Given the sample size, effect sizes are used to support interpretation rather than hypothesis testing.

## Interpretation
The findings are interpreted descriptively and are intended to characterise the experiences and preferences of the participants included in this study.

Observed relationships are reported as exploratory patterns that may inform future research.

## Project structure
~~~
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
│   └── figures/
│       └── .gitkeep
├── config/
│   └── analysis.toml
└── src/
    └── guide_analysis/
        ├── __init__.py
        ├── __main__.py
        ├── cli.py
        ├── config.py
        └── survey_processing/
            ├── __init__.py
            ├── columns.py
            ├── cleaning.py
            ├── io.py
            ├── preprocessing.py
            ├── categorical.py
            ├── ordinal.py
            ├── multi_select.py
            ├── crosstabs.py
            ├── effect_sizes.py
            ├── plotting.py
            └── processor.py
~~~

## Folder and file guide
| Path	                                                  | Purpose                                                                                             |
| ----                                                    | ----                                                                                                |
| `data/raw/`	                                            | Raw survey CSV exports.                                                                             |
| `outputs/preprocessing/`                                | Preprocessing outputs, including duration summaries and flagged responses.                          |
| `outputs/tables/`	                                      | Generated categorical, ordinal, rating, multi-select, cross-tabulation, and effect size tables.     |
| `outputs/figures/`                                      | Generated charts and figures.                                                                       |
| `config/analysis.toml`                                  | Stores input paths, output paths, and configurable analysis settings.                               |
| `src/guide_analysis/cli.py`                             |	Defines the command-line interface.                                                                 |
| `src/guide_analysis/config.py`                          | Loads and validates analysis settings from the TOML configuration file.                             |
| `src/guide_analysis/survey_processing/columns.py`       |	Defines which survey columns are categorical, ordinal, rating, multi-select, metadata, or excluded. |
| `src/guide_analysis/survey_processing/cleaning.py`      | Cleans column names, text spacing, missing values, and category labels where required.              |
| `src/guide_analysis/survey_processing/io.py`            | Loads raw CSV files and writes output CSV files.                                                    |
| `src/guide_analysis/survey_processing/preprocessing.py` | Handles duration parsing, duration summaries, duplicate response ID checks, and threshold flagging. |
| `src/guide_analysis/survey_processing/categorical.py`   | Generates summaries for nominal single-choice categorical questions.                                |
| `src/guide_analysis/survey_processing/ordinal.py`       | Generates summaries for ordered categorical variables and 1 to 5 rating questions.                  |
| `src/guide_analysis/survey_processing/multi_select.py`  | Splits and summarises multi-select responses.                                                       |
| `src/guide_analysis/survey_processing/crosstabs.py`     | Creates cross-tabulations between selected variables.                                               |
| `src/guide_analysis/survey_processing/effect_sizes.py`  | Calculates effect sizes for selected exploratory comparisons where appropriate.                     |
| `src/guide_analysis/survey_processing/plotting.py`      | Creates graphs from summary tables.                                                                 |
| `src/guide_analysis/survey_processing/processor.py`     | Coordinates the analysis pipeline and writes output files.                                          |