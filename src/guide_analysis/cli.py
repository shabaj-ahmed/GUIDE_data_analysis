"""Command-line entry point for running the GUIDE survey analysis."""

import argparse
from pathlib import Path

from guide_analysis.config import load_analysis_config
from guide_analysis.survey_processing.processor import run_analysis


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Run GUIDE survey data analysis."
    )

    parser.add_argument(
        "--config",
        type=Path,
        default=Path("config/analysis.toml"),
        help="Path to the analysis configuration TOML file.",
    )

    return parser


def main() -> int:
    """Run the analysis from the command line."""
    parser = build_parser()
    args = parser.parse_args()

    config = load_analysis_config(args.config)

    run_analysis(config)

    return 0