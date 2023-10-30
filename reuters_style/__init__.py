"""Format dates, numbers and text to conform with the Reuters Style Guide, the standards that guide the world's largest independent newsroom."""
from __future__ import annotations

from datetime import datetime, timezone


def dayofweek(dt: datetime, tabular: bool = False) -> str:
    """Format the day of the week according to Reuters style.

    Args:
        dt: The datetime to format. (datetime)
        tabular: Whether to format the day of the week for a tabular display. (bool)

    Returns:
        The formatted day of the week. (str)

    Example:
        >>> import reuters_style
        >>> reuters_style.dayofweek(datetime(2021, 9, 1))
        'Wednesday'
    """
    if tabular:
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    else:
        days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
    return days[dt.weekday()]


def date(dt: datetime) -> str:
    """Format a date according to Reuters style.

    Args:
        dt: The datetime to format. (datetime)

    Returns:
        The formatted date. (str)

    Example:
        >>> import reuters_style
        >>> reuters_style.date(datetime(2021, 9, 1))
        'Sept. 1, 2021'
        >>> reuters_style.date(datetime(2021, 3, 1))
        'March 1, 2021'
    """
    months = [
        "Jan.",
        "Feb.",
        "March",
        "April",
        "May",
        "June",
        "July",
        "Aug.",
        "Sept.",
        "Oct.",
        "Nov.",
        "Dec.",
    ]
    return f"{months[dt.month - 1]} {dt.strftime('%-d')}, {dt.strftime('%Y')}"


def time(dt: datetime, include_timezone: bool = True) -> str:
    """Format a time according to Reuters style.

    Args:
        dt: The datetime to format. (datetime)
        include_timezone: Whether to include the timezone in the result. (bool)

    Returns:
        The formatted time. (str)

    Example:
        >>> import reuters_style
        >>> reuters_style.time(datetime(2021, 9, 1, 12, 0))
        'noon GMT'
        >>> reuters_style.time(datetime(2021, 9, 1, 12, 0), include_timezone=False)
        'noon'
        >>> reuters_style.time(datetime(2021, 9, 1, 12, 30))
        '12:30 p.m. GMT'
        >>> reuters_style.time(datetime(2021, 9, 1, 12, 30), include_timezone=False)
        '12:30 p.m.'
        >>> tz = pytz.timezone('Africa/Johannesburg')
        >>> reuters_style.time(tz.localize(datetime(2021, 9, 1, 12, 30)))
        '12:30 p.m. SAST'
    """
    # Pull the hour and minute
    hour = dt.hour
    minute = dt.minute

    # Special case noon and midnight
    if minute == 0 and hour == 0:
        formatted_time = "midnight"
    elif minute == 0 and hour == 12:
        formatted_time = "noon"
    else:
        # Set a.m. or p.m. period
        if hour < 12:
            period = "a.m."
            if hour == 0:
                hour = 12
        else:
            if hour > 12:
                hour -= 12
            period = "p.m."

        # Put it together
        if minute == 0:
            formatted_time = f"{hour} {period}"
        else:
            formatted_time = f"{hour}:{minute:02d} {period}"

    # Do we want to include the timezone in the output string?
    if include_timezone:
        # If the datetime has a timezone, add it to the output
        if dt.tzinfo:
            # Get the timezone
            abbreviation = dt.strftime("%Z")
            # We call it GMT, not UTC
            if abbreviation == "UTC":
                abbreviation = "GMT"
            # Add the timezone to the output
            formatted_time += f" {abbreviation}"
        else:
            # If there is no timezone, we assume GMT
            formatted_time += " GMT"
    # If we don't want to include the timezone ...
    else:
        # ... we need to append GMT in cases where we have a local datetime ...
        # ... assuming it's not already UTC.
        if dt.tzinfo and dt.tzinfo != timezone.utc:
            gmt_time = dt.astimezone(timezone.utc)
            formatted_time += f" ({gmt_time.strftime('%H%M')} GMT)"

    # Format the time
    return formatted_time
