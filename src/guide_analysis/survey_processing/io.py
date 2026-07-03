"""File input and output utilities for GUIDE survey data."""

from pathlib import Path

import pandas as pd

INPUT_CSV_ENCODING = "utf-8-sig"
OUTPUT_CSV_ENCODING = "utf-8"


def read_survey_csv(path: Path) -> pd.DataFrame:
    """Read a survey CSV file into a dataframe."""
    if not path.is_file():
        raise FileNotFoundError(f"Survey CSV file not found: {path}")

    return pd.read_csv(
        path,
        encoding=INPUT_CSV_ENCODING,
    )


def write_csv(df: pd.DataFrame, path: Path) -> None:
    """Write a dataframe to a CSV file."""
    path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(
        path,
        index=False,
        encoding=OUTPUT_CSV_ENCODING,
    )