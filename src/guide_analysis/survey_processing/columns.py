"""Survey column definitions.

lists of survey columns grouped by analysis type, such as single-choice questions, multi-select questions, rating questions, and
open-ended questions.
"""

"""Column definitions shared across GUIDE survey processing."""

"""Shared column names for GUIDE survey processing."""

RESPONSE_ID_COLUMN = "Response ID"
START_DATE_COLUMN = "Start Date"
COMPLETION_DATE_COLUMN = "Completion Date"

PARSED_START_DATE_COLUMN = "start_date_parsed"
PARSED_COMPLETION_DATE_COLUMN = "completion_date_parsed"
COMPLETION_DURATION_MINUTES_COLUMN = "completion_duration_minutes"

METADATA_COLUMNS = (
    RESPONSE_ID_COLUMN,
    START_DATE_COLUMN,
    COMPLETION_DATE_COLUMN,
)