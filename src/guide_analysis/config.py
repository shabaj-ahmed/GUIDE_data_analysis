"""Configuration loading for the GUIDE analysis pipeline."""

from dataclasses import dataclass
from pathlib import Path
from typing import Any
import tomllib


@dataclass(frozen=True)
class DurationThresholds:
    """Duration threshold settings for one survey respondent group."""

    min_minutes: float | None
    max_minutes: float | None


@dataclass(frozen=True)
class ExcludedResponseIds:
    """Response IDs explicitly excluded from analysis."""

    deafblind_participants: frozenset[str]
    carers: frozenset[str]


@dataclass(frozen=True)
class AnalysisConfig:
    """Configuration for one analysis run."""

    deafblind_csv: Path
    carers_csv: Path
    output_dir: Path

    deafblind_duration_thresholds: DurationThresholds
    carers_duration_thresholds: DurationThresholds

    excluded_response_ids: ExcludedResponseIds



def load_analysis_config(path: Path) -> AnalysisConfig:
    """Load analysis configuration from a TOML file."""
    with path.open("rb") as file:
        data = tomllib.load(file)

    paths = data["paths"]
    
    duration_thresholds = data.get("duration_thresholds", {} )
    deafblind_thresholds = duration_thresholds.get( "deafblind_participants", {} )
    carers_thresholds = duration_thresholds.get( "carers", {} )

    excluded_response_ids = data.get("excluded_response_ids", {} )

    return AnalysisConfig(
        deafblind_csv=Path(paths["deafblind_csv"]),
        carers_csv=Path(paths["carers_csv"]),
        output_dir=Path(paths["output_dir"]),
        deafblind_duration_thresholds=parse_duration_thresholds(
            deafblind_thresholds
        ),
        carers_duration_thresholds=parse_duration_thresholds(
            carers_thresholds
        ),
        excluded_response_ids=ExcludedResponseIds(
            deafblind_participants=frozenset(
                str(response_id)
                for response_id in excluded_response_ids.get( "deafblind_participants", [], )
            ),
            carers=frozenset(
                str(response_id)
                for response_id in excluded_response_ids.get( "carers", [], )
            ),
        ),
    )


def parse_duration_thresholds(
    data: dict[str, Any],
) -> DurationThresholds:
    """Parse optional duration thresholds from configuration data."""
    return DurationThresholds(
        min_minutes=parse_optional_float(data.get("min_minutes")),
        max_minutes=parse_optional_float(data.get("max_minutes")),
    )


def parse_optional_float(value: object) -> float | None:
    """Convert a configured value to an optional float."""
    if value is None:
        return None

    return float(value)