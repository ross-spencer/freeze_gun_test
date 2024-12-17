"""Test freezegun."""

from freezegun import freeze_time

from src.validation.validation import check_timestamps


@freeze_time("2015-07-12T12:30:00Z")
def test_freeze_gun():
    """Test freezegun."""
    check_timestamps()
