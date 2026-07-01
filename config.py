"""
Application Configuration

SOC Investigation Workbench
"""

from pathlib import Path

# --------------------------------------------------
# Project Information
# --------------------------------------------------

APP_NAME = "SOC Investigation Workbench"

APP_VERSION = "1.0.0"

AUTHOR = "Sahana"

# --------------------------------------------------
# Root Directories
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

UPLOAD_DIR = DATA_DIR / "uploads"

REPORT_DIR = DATA_DIR / "reports"

LOG_DIR = BASE_DIR / "logs"

DATABASE_DIR = BASE_DIR / "database"

SCHEMA_DIR = BASE_DIR / "schemas"

# --------------------------------------------------
# Database
# --------------------------------------------------

DATABASE_NAME = "soc_workbench.db"

DATABASE_PATH = DATABASE_DIR / DATABASE_NAME

# --------------------------------------------------
# Logging
# --------------------------------------------------

LOG_FILE = LOG_DIR / "soc_workbench.log"

LOG_LEVEL = "INFO"

# --------------------------------------------------
# Investigation
# --------------------------------------------------

MAX_EVENTS = 10000

DEFAULT_SEVERITY = "Low"

DEFAULT_PRIORITY = "Medium"

# --------------------------------------------------
# Dashboard
# --------------------------------------------------

DEFAULT_PAGE_SIZE = 100

MAX_TABLE_ROWS = 1000

# --------------------------------------------------
# Supported Evidence
# --------------------------------------------------

SUPPORTED_EXTENSIONS = [

    ".evtx",

    ".log",

    ".csv",

    ".txt",

    ".eml",

    ".msg",

    ".ioc",

    ".json"

]

# --------------------------------------------------
# Risk Levels
# --------------------------------------------------

RISK_LEVELS = [

    "Informational",

    "Low",

    "Medium",

    "High",

    "Critical"

]

# --------------------------------------------------
# MITRE
# --------------------------------------------------

MITRE_FRAMEWORK = "MITRE ATT&CK"