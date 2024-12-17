"""Validation tests."""

import logging
import multiprocessing
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
    """Multiprocessing test..."""
    sources = [[1], [2], [3]]
    with multiprocessing.Pool() as pool:
        _ = pool.starmap(_check_timestamps, sources)


def _check_timestamps(sources: list):
    """Ensure timestamps are all within a given threshold from now."""
    logger.info("sources: %s", sources)
    validation_timestamp = datetime.now(timezone.utc)
    assert str(validation_timestamp).startswith("2015-07-12 12:30:00")
