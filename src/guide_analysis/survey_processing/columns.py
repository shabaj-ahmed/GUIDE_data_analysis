"""Survey schema definitions for GUIDE quantitative analysis."""

# ---------------------------------------------------------------------------
# Shared metadata columns
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Respondent group names
# ---------------------------------------------------------------------------

DEAFBLIND_RESPONDENT_GROUP = "deafblind_participants"
CARER_RESPONDENT_GROUP = "carers"


# ===========================================================================
# Deafblind participant survey
# ===========================================================================

# ---------------------------------------------------------------------------
# Nominal single-choice questions
# ---------------------------------------------------------------------------

DEAFBLIND_NOMINAL_QUESTIONS: dict[
    str,
    tuple[str, ...],
] = {

    (
        "15. Do you currently use any technology to support navigation when travelling?"
    ): (
        "Yes",
        "No",
    ),

    (
        "20. Have you previously used vibration-based alerts?"
    ): (
        "Yes",
        "No",
    ),

    (
        "21. Where would you prefer to receive vibration alerts from a haptic device?"
    ): (
        "Smartphone (i.e., in your hand or pocket)",
        "On your wrist from a wrist-worn device",
        "Other handheld device",
        "Other (please specify)",
    ),
}


# ---------------------------------------------------------------------------
# Categorical ordinal questions
#
# Values must be listed from lowest to highest.
# ---------------------------------------------------------------------------

DEAFBLIND_ORDINAL_CATEGORICAL_QUESTIONS: dict[
    str,
    tuple[str, ...],
] = {
    "1. What is your age?": (
        "18 - 24",
        "25 - 34",
        "35 - 44",
        "45 - 54",
        "55 - 64",
        "Over 64",
    ),

    (
        "2. How would you describe your vision impairment?"
    ): (
        "Refractive impairment (not Sight Impaired)",
        "Sight Impaired",
        "Severely Sight Impaired",
        "Certificate of Visual Impairment",
        "Prefer to self-describe",
    ),

    (
        "3. How would you describe your hearing impairment?"
    ): (
        "Mild",
        "Moderate",
        "Severe",
        "Profound",
        "Prefer to self-describe"
    ),

    (
        "6. In a typical week, how many bus journeys do you make?"
    ): (
        "0",
        # Export artefacts:
        # "01-Feb" means "1-2"
        # "03-Apr" means "3-4"
        # "05-Jun" means "5-6"
        "01-Feb",
        "03-Apr",
        "05-Jun",
        "7 or more",
    ),

    (
        "7. Of these bus journeys, how many usually involve assistance from another person?"
    ): (
        "None",
        "Some",
        "Most",
        "All",
        "Not relevant",
    ),

    (
        "14. How confident do you feel using mobile applications?"
    ): (
        "Not confident",
        "Slightly confident",
        "Moderately confident",
        "Very confident",
    ),
}


# ---------------------------------------------------------------------------
# Numeric ordinal questions
# ---------------------------------------------------------------------------

DEAFBLIND_ORDINAL_NUMERIC_QUESTIONS: dict[
    str,
    tuple[int, ...],
] = {
    (
        "22. If reliable, how likely are you to consider using a vibration-based bus navigation tool? (1-5 numeric rating)"
    ): (
        1,
        2,
        3,
        4,
        5,
    ),

    (
        "23. How likely is this type of system to increase your independence in travel? (1-5 numeric rating)"
    ): (
        1,
        2,
        3,
        4,
        5,
    ),
}


# ---------------------------------------------------------------------------
# Nominal multi-select questions
# ---------------------------------------------------------------------------

DEAFBLIND_MULTI_SELECT_QUESTIONS: dict[
    str,
    tuple[str, ...],
] = {
    (
        "4. What communication methods do you normally use? (Select all that apply)"
    ): (
        "Spoken communication",
        "Written/text-based communication",
        "Tactile (such as Braille, vibration-based communication)",
        "Sign language",
    ),

    (
        "5. What modes of transportation do you commonly use? (Select all that apply)"
    ): (
        "Walk",
        "Drive yourself in a car",
        "Driven in car by a friend/family member/carer",
        "Driven in a taxi or uber",
        "Bus",
        "Train",
        "Bicycle",
    ),

    (
        "8. What assistance does this other person provide? (Select all that apply)"
    ): (
        "Planning the journey",
        "Taking me to the bus stop",
        "Tells me when to get on and/or off the bus",
        "Supports me in physically getting on and/or off the bus",
        "Provides me with information about the route",
    ),

    (
        "9. How do you plan journeys you make by bus? (Select all that apply)"
    ): (
        "Using a maps app on my phone (e.g., Google maps, Apple maps)",
        "Using a maps website on my computer (e.g., Google maps)",
        "Using the bus provider's mobile app",
        "Using the information at the bus stop",
        "Someone else plans the journey for me",
    ),

    (
        "10. Which aspects of bus travel do you find challenging? (Select all that apply)"
    ): (
        "Identifying the correct bus",
        "Locating the correct stop",
        "Knowing when to disembark",
        "Receiving information about changes to services/routes",
        "Communicating with staff or passengers",
        "Other (please specify)",
    ),

    (
        "13. Which of the following technologies do you currently use? (Select all that apply)"
    ): (
        "Smartphone accessibility features",
        "Screen reader software",
        "Hearing devices",
        "Vibration alerts",
        "None",
        "Other (please specify)",
    ),
}


# ---------------------------------------------------------------------------
# Ranking questions
# ---------------------------------------------------------------------------

DEAFBLIND_RANKING_QUESTIONS: dict[
    str,
    tuple[str, ...],
] = {
    (
        "12. Rank these types of information in terms of importance to you during bus travel (1 = highest importance)"
    ): (
        "Bus arrival confirmation",
        "Correct route identification",
        "Next stop notification",
        "Destination alert",
        "Route change notification",
        "Delay information",
    ),
}


# ===========================================================================
# Carer survey
# ===========================================================================

# ---------------------------------------------------------------------------
# Nominal single-choice questions
# ---------------------------------------------------------------------------

CARER_NOMINAL_QUESTIONS: dict[
    str,
    tuple[str, ...],
] = {
    (
        "1. What is your caring relationship towards a person with dual sensory loss?"
    ): (
        "Parent",
        "Partner",
        "Family member",
        "Friend",
        "Professional carer/support worker",
        "None",
        "Other (please specify)",
    ),

    (
        "10. Does the person you support use any assistive or navigation technologies?"
    ): (
        "Yes",
        "No",
        "Unsure",
    ),

    (
        "15. Would you find it helpful to receive optional journey updates (e.g., confirmation of boarding, approaching destination)?"
    ): (
        "Yes",
        "No",
        "Unsure",
    ),

    (
        "17. Would such features reduce your concern about independent bus travel?"
    ): (
        "Yes",
        "No",
        "Unsure",
    ),
}


# ---------------------------------------------------------------------------
# Categorical ordinal questions
#
# Values are listed from lowest to highest.
# ---------------------------------------------------------------------------

CARER_ORDINAL_CATEGORICAL_QUESTIONS: dict[
    str,
    tuple[str, ...],
] = {
    (
        "2. How often do you provide support related to travel"
    ): (
        "Rarely",
        "Less than once per month",
        "Monthly",
        "Several times per month",
        "Weekly",
        "Several times per week",
        "Daily",
        "Multiple times a day",
    ),

    (
        "3. Does the person you support travel independently by bus?"
    ): (
        "Never",
        "Rarely",
        "Yes, occasionally",
        "Yes, frequently",
    ),
}


# ---------------------------------------------------------------------------
# Numeric ordinal questions
# ---------------------------------------------------------------------------

CARER_ORDINAL_NUMERIC_QUESTIONS: dict[
    str,
    tuple[int, ...],
] = {
    (
        "18. How likely do you think a vibration-based navigation system is to increase the travel independence of the person you support? (1-5 numeric rating)"
    ): (
        1,
        2,
        3,
        4,
        5,
    ),
}


# ---------------------------------------------------------------------------
# Nominal multi-select questions
# ---------------------------------------------------------------------------

CARER_MULTI_SELECT_QUESTIONS: dict[
    str,
    tuple[str, ...],
] = {
    (
        "6. In what situations do you feel additional support is required? (Select all that apply)"
    ): (
        "Boarding the correct bus",
        "Knowing when to get off",
        "Route changes",
        "Delays",
        "Unexpected disruptions",
        "Crowded environments",
        "Other (please specify)",
    ),

    (
        "7. Do you use any of the following technologies to support the person you care for? (Select all that apply)"
    ): (
        "Smartphone applications",
        "GPS/navigation apps",
        "Location tracking tools",
        "Messaging or alert systems",
        "Accessibility features (e.g., vibration alerts)",
        "Hearing or visual assistive devices",
        "None",
        "Other (please specify)",
    ),

    (
        "16. What types of updates would you consider most useful? (Select all that apply)"
    ): (
        "Journey start confirmation",
        "Route deviation alerts",
        "Arrival confirmation",
        "Emergency alerts",
        "Other (please specify)",
    ),
}

# ---------------------------------------------------------------------------
# Special response markers
# ---------------------------------------------------------------------------

SPECIAL_RESPONSE_MARKERS = (
    "Other (please specify)",
    "Prefer to self-describe",
)

# ===========================================================================
# Question schemas by respondent group
# ===========================================================================

NOMINAL_QUESTIONS_BY_RESPONDENT_GROUP = {
    DEAFBLIND_RESPONDENT_GROUP: DEAFBLIND_NOMINAL_QUESTIONS,
    CARER_RESPONDENT_GROUP: CARER_NOMINAL_QUESTIONS,
}

ORDINAL_CATEGORICAL_QUESTIONS_BY_RESPONDENT_GROUP = {
    DEAFBLIND_RESPONDENT_GROUP: (
        DEAFBLIND_ORDINAL_CATEGORICAL_QUESTIONS
    ),
    CARER_RESPONDENT_GROUP: (
        CARER_ORDINAL_CATEGORICAL_QUESTIONS
    ),
}

ORDINAL_NUMERIC_QUESTIONS_BY_RESPONDENT_GROUP = {
    DEAFBLIND_RESPONDENT_GROUP: (
        DEAFBLIND_ORDINAL_NUMERIC_QUESTIONS
    ),
    CARER_RESPONDENT_GROUP: (
        CARER_ORDINAL_NUMERIC_QUESTIONS
    ),
}

MULTI_SELECT_QUESTIONS_BY_RESPONDENT_GROUP = {
    DEAFBLIND_RESPONDENT_GROUP: (
        DEAFBLIND_MULTI_SELECT_QUESTIONS
    ),
    CARER_RESPONDENT_GROUP: (
        CARER_MULTI_SELECT_QUESTIONS
    ),
}

RANKING_QUESTIONS_BY_RESPONDENT_GROUP = {
    DEAFBLIND_RESPONDENT_GROUP: (
        DEAFBLIND_RANKING_QUESTIONS
    ),
    CARER_RESPONDENT_GROUP: {},
}