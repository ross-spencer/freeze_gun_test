"""Validation tests."""

import logging
import time
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

logging.basicConfig(
    format="%(asctime)-15s %(levelname)s :: %(filename)s:%(lineno)s:%(funcName)s() :: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level="INFO",
)

# Default to UTC time.
logging.Formatter.converter = time.gmtime

logger = logging.getLogger(__name__)


def check_timestamps():
    """Ensure timestamps are all within a given threshold from now."""
    validation_timestamp = datetime.now(timezone.utc)
    logger.error("timestamp: %s", validation_timestamp)
    assert False, "all tests fail, check the log line above"
