"""Test freezegun."""

from freezegun import freeze_time

from src.validation.validation import _check_timestamps, check_timestamps


def test_freeze_gun():
    """Test freezegun."""

    with freeze_time("2015-07-12T12:30:00Z"):
        check_timestamps()


@freeze_time("2015-07-12T12:30:00Z")
def test_freeze_gun_okay():
    """Test freezegun."""
    _check_timestamps([])
