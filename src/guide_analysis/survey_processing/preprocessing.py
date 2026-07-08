"""Preprocessing and duration summaries for GUIDE survey exports."""

from pathlib import Path

import pandas as pd

from guide_analysis.survey_processing.columns import (
    COMPLETION_DATE_COLUMN,
    COMPLETION_DURATION_MINUTES_COLUMN,
    PARSED_COMPLETION_DATE_COLUMN,
    PARSED_START_DATE_COLUMN,
    RESPONSE_ID_COLUMN,
    START_DATE_COLUMN,
)


def parse_datetime_column(series: pd.Series) -> pd.Series:
    """Parse a required survey date/time column.

    The pipeline raises an error when values cannot be parsed or are missing,
    because start and completion timestamps are expected in the source export.
    """
    try:
        parsed = pd.to_datetime(
            series,
            errors="raise",
            dayfirst=True,
        )
    except (TypeError, ValueError) as error:
        raise ValueError(
            f"Unable to parse date/time values in column '{series.name}'."
        ) from error

    missing_count = int(parsed.isna().sum())

    if missing_count > 0:
        raise ValueError(
            f"Column '{series.name}' contains "
            f"{missing_count} missing date/time value(s)."
        )

    return parsed


def add_completion_duration(df: pd.DataFrame) -> pd.DataFrame:
    """Add parsed timestamps and completion duration in minutes."""
    processed = df.copy()

    processed[PARSED_START_DATE_COLUMN] = parse_datetime_column(
        processed[START_DATE_COLUMN]
    )

    processed[PARSED_COMPLETION_DATE_COLUMN] = parse_datetime_column(
        processed[COMPLETION_DATE_COLUMN]
    )

    duration = (
        processed[PARSED_COMPLETION_DATE_COLUMN]
        - processed[PARSED_START_DATE_COLUMN]
    )

    processed[COMPLETION_DURATION_MINUTES_COLUMN] = (
        duration.dt.total_seconds() / 60
    )

    negative_duration_count = int(
        (
            processed[COMPLETION_DURATION_MINUTES_COLUMN]
            < 0
        ).sum()
    )

    if negative_duration_count > 0:
        raise ValueError(
            f"Found {negative_duration_count} response(s) "
            "with a negative completion duration."
        )

    return processed


def build_dataset_overview_row(
    respondent_group: str,
    csv_path: Path,
    cleaned_dataframe: pd.DataFrame,
    analysis_dataframe: pd.DataFrame,
) -> dict[str, object]:
    """Create a high-level overview for one survey dataset."""
    return {
        "respondent_group": respondent_group,
        "csv_path": str( csv_path ),
        "all_response_count": len( cleaned_dataframe ),
        "excluded_response_count": ( len(cleaned_dataframe) - len(analysis_dataframe) ),
        "analysis_response_count": len( analysis_dataframe ),
        "column_count": len( cleaned_dataframe.columns ),
    }


def build_duration_summary_row(
    df: pd.DataFrame,
    respondent_group: str,
) -> dict[str, object]:
    """Summarise completion durations for one respondent group."""
    processed = add_completion_duration(df)

    durations = processed[
        COMPLETION_DURATION_MINUTES_COLUMN
    ]

    return {
        "respondent_group": respondent_group,
        "response_count": len(processed),
        "mean_minutes": round(
            float(durations.mean()),
            2,
        ),
        "median_minutes": round(
            float(durations.median()),
            2,
        ),
        "min_minutes": round(
            float(durations.min()),
            2,
        ),
        "max_minutes": round(
            float(durations.max()),
            2,
        ),
        "q1_minutes": round(
            float(durations.quantile(0.25)),
            2,
        ),
        "q3_minutes": round(
            float(durations.quantile(0.75)),
            2,
        ),
    }


def build_duration_threshold_flags_table(
    df: pd.DataFrame,
    respondent_group: str,
    min_duration_minutes: float | None,
    max_duration_minutes: float | None,
) -> pd.DataFrame:
    """Return responses outside the configured duration review thresholds."""
    validate_duration_thresholds(
        min_duration_minutes=min_duration_minutes,
        max_duration_minutes=max_duration_minutes,
    )

    processed = add_completion_duration(df)

    rows: list[dict[str, object]] = []

    for _, row in processed.iterrows():
        duration_minutes = float(
            row[COMPLETION_DURATION_MINUTES_COLUMN]
        )

        flag_reasons: list[str] = []

        if (
            min_duration_minutes is not None
            and duration_minutes < min_duration_minutes
        ):
            flag_reasons.append(
                "below_min_duration_threshold"
            )

        if (
            max_duration_minutes is not None
            and duration_minutes > max_duration_minutes
        ):
            flag_reasons.append(
                "above_max_duration_threshold"
            )

        if not flag_reasons:
            continue

        rows.append(
            {
                "respondent_group": respondent_group,
                "response_id": row[RESPONSE_ID_COLUMN],
                "completion_duration_minutes": round(
                    duration_minutes,
                    2,
                ),
                "flag_reason": "; ".join(flag_reasons),
                "min_duration_threshold_minutes": (
                    min_duration_minutes
                ),
                "max_duration_threshold_minutes": (
                    max_duration_minutes
                ),
                "start_date": row[START_DATE_COLUMN],
                "completion_date": row[
                    COMPLETION_DATE_COLUMN
                ],
            }
        )

    return pd.DataFrame(
        rows,
        columns=[
            "respondent_group",
            "response_id",
            "completion_duration_minutes",
            "flag_reason",
            "min_duration_threshold_minutes",
            "max_duration_threshold_minutes",
            "start_date",
            "completion_date",
        ],
    )


def exclude_responses(
    df: pd.DataFrame,
    excluded_response_ids: set[str] | frozenset[str],
) -> pd.DataFrame:
    """Remove explicitly excluded responses from the analysis dataset."""
    if not excluded_response_ids:
        return df.copy()

    response_ids = df[
        RESPONSE_ID_COLUMN
    ].astype("string")

    available_response_ids = set(
        response_ids.dropna().tolist()
    )

    normalised_exclusion_ids = {
        str(response_id)
        for response_id in excluded_response_ids
    }

    unknown_exclusion_ids = (
        normalised_exclusion_ids
        - available_response_ids
    )

    if unknown_exclusion_ids:
        raise ValueError(
            "Configured exclusion IDs were not found "
            "in the survey dataset: "
            f"{sorted(unknown_exclusion_ids)}"
        )

    return df.loc[
        ~response_ids.isin(normalised_exclusion_ids)
    ].copy()


def validate_duration_thresholds(
    min_duration_minutes: float | None,
    max_duration_minutes: float | None,
) -> None:
    """Validate configured minimum and maximum duration thresholds."""
    if (
        min_duration_minutes is not None
        and max_duration_minutes is not None
        and min_duration_minutes > max_duration_minutes
    ):
        raise ValueError(
            "Minimum duration threshold cannot be greater "
            "than maximum duration threshold."
        )