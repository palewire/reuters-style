from __future__ import annotations

from datetime import datetime, timezone


def date(dt: datetime) -> str:
    """Format a date according to Reuters style.

    In text, use the sequence month/day/year, e.g., “Iraq’s invasion of Kuwait on
    Aug. 2, 1990, led to...” or “the Aug. 2 invasion” or “the August 1990 invasion.”

    If a specific date is used, put the year inside commas. Spell out months
    in text, but abbreviate them followed by a full stop when they are used
    with a specific date – Jan.1.

    When spelling out duration, write, “The tournament runs from May 22 to 24,”
    not “…runs from May 22-24.” Write “arrived on Monday,” not “arrived Monday”
    and “on Tuesday,” rather than “yesterday,” “today,” “tomorrow.” Write
    “the 1939-45 war” but “from 1939 to 1945,” not “from 1939-45.” Write 9/11,
    not 9-11. In commodities stories, write “Brazil’s 2013/14 soybean crop”
    (conventional use), not “2013-14.”

    Abbreviate as follows, noting the dot after the abbreviation: Jan., Feb.,
    March, April, May, June, July, Aug., Sept., Oct., Nov., Dec.

    Args:
        dt: The datetime to format. (datetime)

    Returns:
        The formatted date. (str)

    Examples:
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


def dayofweek(dt: datetime, tabular: bool = False) -> str:
    """Format the day of the week according to Reuters style.

    Always precede the day of the week with the word "on" as in she said on Monday,
    not she said Monday. Do not abbreviate the days of the week, except in a
    tabular format: Sun, Mon, Tue, Wed, Thu, Fri, Sat (three letters, without periods).

    Args:
        dt: The datetime to format. (datetime)
        tabular: Whether to format the day of the week for a tabular display. (bool)

    Returns:
        The formatted day of the week. (str)

    Examples:
        >>> import reuters_style
        >>> reuters_style.dayofweek(datetime(2021, 9, 1))
        'Wednesday'
        >>> reuters_style.dayofweek(datetime(2021, 9, 1), tabular=True)
        'Wed'
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


def time(dt: datetime, include_timezone: bool = True) -> str:
    """Format a time according to Reuters style.

    Abbreviations of time zones are acceptable providing the GMT equivalent is given.
    BST (British Summer Time) = GMT +1 CET (Central European Time) = GMT +1 CDT
    (Central Daylight Time) = GMT -5 CST (Central Standard Time) = GMT -6 EST
    (Eastern Standard Time) = GMT -5 MDT (Mountain Daylight Time) = GMT -6 MST
    (Mountain Standard Time) = GMT -7 PST (Pacific Standard Time) = GMT -8.and

    When referring to times, first give the local time by the 12-hour clock (without
    using the words local time) and follow it with a bracketed conversion to a
    24-hour clock time for a specified time zone, e.g., “will meet at 10 a.m.
    (1600 GMT).”

    Use figures except for noon and midnight. Use a colon to separate
    hours and minutes, e.g., 3:15 p.m. Use the style “on Friday,” “on Saturday,”
    rather than the looser “today,” “yesterday,” “tomorrow.”

    Do not use phrases like “several months ago” or “recently,” which suggest we do not know when something
    happened or are too lazy to find out. Be precise – “last August” or “on Feb. 2.”

    Args:
        dt: The datetime to format. (datetime)
        include_timezone: Whether to include the timezone in the result. (bool)

    Returns:
        The formatted time. (str)

    Examples:
        >>> import reuters_style
        >>> reuters_style.time(datetime(2021, 9, 1, 12, 0))
        'noon GMT'
        >>> reuters_style.time(datetime(2021, 9, 1, 12, 0), include_timezone=False)
        'noon'
        >>> reuters_style.time(datetime(2021, 9, 1, 12, 30))
        '12:30 p.m. GMT'
        >>> reuters_style.time(datetime(2021, 9, 1, 12, 30), include_timezone=False)
        '12:30 p.m.'
        >>> import pytz
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
