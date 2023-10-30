"""Test the date methods."""
from datetime import datetime, timezone

import pytz

import reuters_style


def test_dayofweek():
    """Test the dayofweek function."""
    assert reuters_style.dayofweek(datetime(2023, 10, 18)) == "Wednesday"
    assert reuters_style.dayofweek(datetime(2023, 10, 19)) == "Thursday"
    assert reuters_style.dayofweek(datetime(2023, 10, 20)) == "Friday"
    assert reuters_style.dayofweek(datetime(2023, 10, 21)) == "Saturday"
    assert reuters_style.dayofweek(datetime(2023, 10, 22)) == "Sunday"
    assert reuters_style.dayofweek(datetime(2023, 10, 23)) == "Monday"
    assert reuters_style.dayofweek(datetime(2023, 10, 24)) == "Tuesday"
    # Now do the test again for tabular display
    assert reuters_style.dayofweek(datetime(2023, 10, 18), tabular=True) == "Wed"
    assert reuters_style.dayofweek(datetime(2023, 10, 19), tabular=True) == "Thu"
    assert reuters_style.dayofweek(datetime(2023, 10, 20), tabular=True) == "Fri"
    assert reuters_style.dayofweek(datetime(2023, 10, 21), tabular=True) == "Sat"
    assert reuters_style.dayofweek(datetime(2023, 10, 22), tabular=True) == "Sun"
    assert reuters_style.dayofweek(datetime(2023, 10, 23), tabular=True) == "Mon"
    assert reuters_style.dayofweek(datetime(2023, 10, 24), tabular=True) == "Tue"


def test_date():
    """Test the date function."""
    assert reuters_style.date(datetime(2001, 9, 11)) == "Sept. 11, 2001"
    assert reuters_style.date(datetime(2021, 9, 1)) == "Sept. 1, 2021"
    assert reuters_style.date(datetime(2021, 3, 1)) == "March 1, 2021"


def test_time():
    """Test the time function."""
    assert reuters_style.time(datetime(2021, 9, 1, 12, 0)) == "noon GMT"
    assert reuters_style.time(datetime(2021, 9, 1, 0, 0)) == "midnight GMT"
    assert (
        reuters_style.time(datetime(2021, 9, 1, 12, 0), include_timezone=False) == "noon"
    )
    assert (
        reuters_style.time(datetime(2021, 9, 1, 0, 0), include_timezone=False)
        == "midnight"
    )
    assert reuters_style.time(datetime(2021, 9, 1, 12, 30)) == "12:30 p.m. GMT"
    assert reuters_style.time(datetime(2021, 9, 1, 0, 30)) == "12:30 a.m. GMT"
    assert (
        reuters_style.time(datetime(2021, 9, 1, 12, 30), include_timezone=False)
        == "12:30 p.m."
    )
    assert (
        reuters_style.time(datetime(2021, 9, 1, 12, 30, tzinfo=timezone.utc))
        == "12:30 p.m. GMT"
    )
    assert (
        reuters_style.time(datetime(2021, 9, 1, 0, 30, tzinfo=timezone.utc))
        == "12:30 a.m. GMT"
    )
    tz = pytz.timezone("Africa/Johannesburg")
    assert (
        reuters_style.time(tz.localize(datetime(2021, 9, 1, 12, 30)))
        == "12:30 p.m. SAST"
    )
    assert (
        reuters_style.time(
            tz.localize(datetime(2021, 9, 1, 12, 30)), include_timezone=False
        )
        == "12:30 p.m. (1030 GMT)"
    )
    tz = pytz.timezone("Asia/Tokyo")
    assert (
        reuters_style.time(tz.localize(datetime(2021, 9, 1, 12, 30))) == "12:30 p.m. JST"
    )
    assert (
        reuters_style.time(
            tz.localize(datetime(2021, 9, 1, 12, 30)), include_timezone=False
        )
        == "12:30 p.m. (0330 GMT)"
    )
    assert reuters_style.time(datetime(2021, 9, 1, 14, 0)) == "2 p.m. GMT"
    assert (
        reuters_style.time(datetime(2021, 9, 1, 14, 0), include_timezone=False)
        == "2 p.m."
    )
    assert reuters_style.time(datetime(2021, 9, 1, 2, 0)) == "2 a.m. GMT"
