import logging
import os
import sys
from logging.handlers import RotatingFileHandler

# Define log directory and file
LOG_DIR = "/app/logs"
LOG_FILE = os.path.join(LOG_DIR, "app.log")

# ✅ Ensure the logs directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Define log format
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s"

# Configure logger
def setup_logger():
    logger = logging.getLogger("AppLogger")
    logger.setLevel(logging.INFO)

    # Prevent duplicate log handlers
    if logger.hasHandlers():
        return logger

    # Console Handler (logs to console)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT))

    # File Handler (logs to file, ensures log rotation)
    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=5)
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT))

    # Add handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

# Initialize logger
logger = setup_logger()
