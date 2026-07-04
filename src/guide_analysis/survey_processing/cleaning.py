"""Cleaning utilities for GUIDE survey data."""

import re

import pandas as pd


def normalise_column_name(column: object) -> str:
    """Normalise whitespace in a survey column name."""
    text = str(column)

    # Replace non-breaking spaces with regular spaces.
    text = text.replace("\u00a0", " ")

    # Collapse repeated whitespace into a single space.
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def normalise_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Normalise all survey column names."""
    cleaned = df.copy()

    cleaned.columns = [
        normalise_column_name(column) for column in cleaned.columns
    ]

    return cleaned


def normalise_text_values(df: pd.DataFrame) -> pd.DataFrame:
    """Strip surrounding whitespace and convert blank text to missing values."""
    cleaned = df.copy()

    text_columns = cleaned.select_dtypes( include=["object", "string"] ).columns

    for column in text_columns:
        cleaned[column] = cleaned[column].map(
            lambda value: value.strip() if isinstance(value, str) else value
        )

        cleaned[column] = cleaned[column].replace( "", pd.NA )

    return cleaned


def clean_survey_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Apply standard cleaning to GUIDE survey data."""
    cleaned = normalise_column_names(df)
    cleaned = normalise_text_values(cleaned)

    return cleaned
