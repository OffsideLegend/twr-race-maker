# python
import logging
from typing import Optional

_app_logger: Optional[logging.Logger] = None

def initialize(level: int) -> logging.Logger:
    """
    Configure and return the module-level logger. Safe to call multiple times.
    """
    global _app_logger
    if _app_logger is not None:
        return _app_logger

    logger = logging.getLogger("selenium")
    logger.setLevel(level)

    # Add a StreamHandler only if the logger has no handlers yet to avoid duplicates
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    # Optionally set more verbose sublogger levels
    logging.getLogger("selenium.webdriver.remote").setLevel(logging.INFO)

    _app_logger = logger
    return _app_logger

def get_logger(level: int = logging.INFO) -> logging.Logger:
    """
    Return the configured logger, initializing it if necessary.
    """
    if _app_logger is None:
        return initialize(level)
    return _app_logger
