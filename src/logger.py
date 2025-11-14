import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
import os
from datetime import datetime

LOG_DIR = Path(os.getcwd()) / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"

def get_logger(name: str = __name__) -> logging.Logger:
    """
    Returns a daily rotating logger with consistent formatting.
    Logs go to both console and file (logs/app.log).
    Each Streamlit rerun will not duplicate handlers.
    """
    logger = logging.getLogger(name)

    if getattr(logger, "_is_configured", False):
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S"
    )

    # File handler: rotates daily
    file_handler = TimedRotatingFileHandler(
        str(LOG_FILE),
        when="midnight",
        interval=1,
        backupCount=7,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger._is_configured = True
    logger.info("─────────────────────────────────────────────")
    logger.info(f"🟢 APP SESSION STARTED — {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    logger.info("─────────────────────────────────────────────")

    return logger
