"""Validation tests."""

import logging
import multiprocessing
import time
from datetime import datetime, timezone

from freezegun import freeze_time

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


def _check_timestamps(sources: list):  # pylint: disable=W0613
    """Ensure timestamps are all within a given threshold from now."""
    validation_timestamp = datetime.now(timezone.utc)
    comparison = "2015-07-12 12:30:00"
    logger.error("timestamp is: %s (should be: '%s')", validation_timestamp, comparison)
    assert str(validation_timestamp).startswith(comparison)


@freeze_time("2018-02-14 11:00:00")
def test_multi_processing():
    """Another multiprocessing test."""
    with multiprocessing.Pool(processes=2) as _:
        validation_timestamp = datetime.now(timezone.utc)
        logger.error("ts multi: %s", validation_timestamp)
