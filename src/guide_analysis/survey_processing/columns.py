"""Survey column definitions.

lists of survey columns grouped by analysis type, such as single-choice questions, multi-select questions, rating questions, and
open-ended questions.
"""

"""Column definitions shared across GUIDE survey processing."""

RESPONSE_ID_COLUMN = "Response ID"
START_DATE_COLUMN = "Start Date"
COMPLETION_DATE_COLUMN = "Completion Date"

METADATA_COLUMNS = (
    RESPONSE_ID_COLUMN,
    START_DATE_COLUMN,
    COMPLETION_DATE_COLUMN,
)