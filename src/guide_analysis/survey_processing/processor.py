"""Survey processing pipeline for the GUIDE analysis project."""

from pathlib import Path

import pandas as pd

from guide_analysis.config import AnalysisConfig
from guide_analysis.survey_processing.cleaning import (
    clean_survey_dataframe,
)
from guide_analysis.survey_processing.io import (
    read_survey_csv,
    write_csv,
)
from guide_analysis.survey_processing.preprocessing import (
    build_dataset_overview_row,
    build_duration_summary_row,
    build_duration_threshold_flags_table,
    exclude_responses,
)


def run_analysis(config: AnalysisConfig) -> None:
    """Run preprocessing for all configured respondent groups."""
    preprocessing_dir = ( config.output_dir / "preprocessing" )

    dataset_overview_rows: list[dict[str, object]] = []
    duration_summary_all_rows: list[dict[str, object]] = []
    duration_summary_analysis_rows: list[dict[str, object]] = []


    survey_datasets = [
        (
            "deafblind_participants",
            config.deafblind_csv,
            config.deafblind_duration_thresholds,
            config.excluded_response_ids.deafblind_participants,
        ),
        (
            "carers",
            config.carers_csv,
            config.carers_duration_thresholds,
            config.excluded_response_ids.carers,
        ),
    ]

    for ( 
        respondent_group, 
        csv_path, 
        duration_thresholds, 
        excluded_response_ids,
    ) in survey_datasets:
        cleaned_dataframe = process_survey_dataset(
            respondent_group=respondent_group,
            csv_path=csv_path,
            preprocessing_dir=preprocessing_dir,
            min_duration_minutes=( duration_thresholds.min_minutes ),
            max_duration_minutes=( duration_thresholds.max_minutes ),
        )

        dataset_overview_rows.append(
            build_dataset_overview_row(
                respondent_group=respondent_group,
                csv_path=csv_path,
                df=cleaned_dataframe,
            )
        )

        duration_summary_all_rows.append(
            build_duration_summary_row(
                df=cleaned_dataframe,
                respondent_group=respondent_group,
            )
        )

        analysis_dataframe = exclude_responses(
            cleaned_dataframe,
            excluded_response_ids,
        )

        duration_summary_analysis_rows.append(
            build_duration_summary_row(
                df=analysis_dataframe,
                respondent_group=respondent_group,
            )
        )
        print( f"  Excluded responses: {len(cleaned_dataframe) - len(analysis_dataframe)}" )

        print( f"  Analysis responses: {len(analysis_dataframe)}" )

    write_csv(
        pd.DataFrame(dataset_overview_rows),
        preprocessing_dir / "dataset_overview.csv",
    )

    write_csv(
        pd.DataFrame(duration_summary_all_rows),
        preprocessing_dir / "duration_summary_all_responses.csv",
    )

    write_csv(
        pd.DataFrame(duration_summary_analysis_rows),
        preprocessing_dir / "duration_summary_analysis_sample.csv",
    )

    print( f"Preprocessing complete. Outputs written to: {preprocessing_dir}" )


def process_survey_dataset(
    respondent_group: str,
    csv_path: Path,
    preprocessing_dir: Path,
    min_duration_minutes: float | None,
    max_duration_minutes: float | None,
) -> pd.DataFrame:
    """Load, clean, and preprocess one survey dataset."""
    print( f"Processing {respondent_group}: {csv_path}" )

    raw_dataframe = read_survey_csv(csv_path)

    cleaned_dataframe = clean_survey_dataframe( raw_dataframe )

    duration_threshold_flags = (
        build_duration_threshold_flags_table(
            df=cleaned_dataframe,
            respondent_group=respondent_group,
            min_duration_minutes=min_duration_minutes,
            max_duration_minutes=max_duration_minutes,
        )
    )

    write_csv(
        duration_threshold_flags,
        preprocessing_dir / ( f"{respondent_group}" "__duration_threshold_flags.csv" ),
    )

    print( f"  Responses: {len(cleaned_dataframe)}" )
    print( f"  Columns: {len(cleaned_dataframe.columns)}" )

    return cleaned_dataframe