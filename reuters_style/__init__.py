from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


def date(dt: datetime) -> str:
    """Format a date according to Reuters style.

    Style guide entry:

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

    Style guide entry:

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

    Style guide entry:

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


def validate_slug(slug: str) -> bool:
    """Check whether a full slug is valid.

    Style guide entry:

        A slug is a simple human readable method of grouping content for packaging,
        either internally or externally. By using the same slug for the same real world
        event Reuters can ensure that it is easy to find pictures, text, graphics,
        video, audio that all belong together.

        A slug has two parts:

        • a packaging slug (FERRARI-IPO/)
        • a wild slug (PROSPECTUS)

        They come together as the full slug in FERRARI-IPO/PROSPECTUS.

    Args:
        slug: The full slug to validate. (str)

    Returns:
        Whether the full slug is valid. (bool)

    Raises:
        ValueError: If the full slug is invalid.

    Examples:
        >>> import reuters_style
        >>> reuters_style.validate_slug('FERRARI-IPO/PROSPECTUS')
        True
        >>> reuters_style.validate_slug('FERRARI-IPO/PROSPECTUS REPORT')
        Traceback (most recent call last):
            ...
        ValueError: Wild slug can only contain uppercase letters, hyphens and slashes.
    """
    # Verify that the slug is a string
    if not isinstance(slug, str):
        raise ValueError("Full slug must be a string.")

    # Verify that the slug is not empty
    if not slug:
        raise ValueError("Full slug cannot be empty.")

    # Verify that the slug is not too long
    if len(slug) > 64:
        raise ValueError("Full slug cannot be longer than 64 characters.")

    # Verify that the slug contains only a single slash
    if slug.count("/") != 1:
        raise ValueError("Full slug can only contain one slash.")

    # Split on the slash
    packaging_slug, wild_slug = slug.split("/")

    # Validate the packaging slug
    validate_packaging_slug(packaging_slug + "/")

    # Validate the wild slug, if there is one
    if wild_slug:
        validate_wild_slug(wild_slug)

    # If we got this far, the slug is valid
    return True


def validate_packaging_slug(slug: str) -> bool:
    """Check whether a packaging slug is valid.

    Style guide entry:

        A slug is a simple human readable method of grouping content for packaging,
        either internally or externally. By using the same slug for the same real world
        event Reuters can ensure that it is easy to find pictures, text, graphics,
        video, audio that all belong together.

        A slug has two parts:

        • a packaging slug (FERRARI-IPO/)
        • a wild slug (PROSPECTUS)

        They come together as the full slug in FERRARI-IPO/PROSPECTUS.

        The packaging slug is the part that is used to pull a package of stories together
        with visuals and so MUST STAY THE SAME for as long as the story runs through updates,
        wrap-ups and for days, weeks or even months sometimes. Once a packaging slug
        (the first two words before the "/" mark) has been established, it should be adopted
        by all services and regions. For example: MALAYSIA-POLITICS/ or BRITAIN-POLITICS/.

    Args:
        slug: The packaging slug to validate. (str)

    Returns:
        Whether the packaging slug is valid. (bool)

    Raises:
        ValueError: If the packaging slug is invalid.

    Examples:
        >>> import reuters_style
        >>> reuters_style.validate_packaging_slug('FERRARI-IPO/')
        True
        >>> reuters_style.validate_packaging_slug('FERRaRI IPO')
        Traceback (most recent call last):
            ...
        ValueError: Packaging slug can only contain uppercase letters, hyphens and slashes.
    """
    # Verify that the slug is a string
    if not isinstance(slug, str):
        raise ValueError("Packaging slug must be a string.")

    # Verify that the slug is not empty
    if not slug:
        raise ValueError("Packaging slug cannot be empty.")

    # Verify that the slug is not too long
    if len(slug) > 64:
        raise ValueError("Packaging slug cannot be longer than 64 characters.")

    # Verify that the slug only contains uppercase letter, hyphens and slashes
    if not slug.isupper():
        raise ValueError(
            "Packaging slug can only contain uppercase letters, hyphens and slashes."
        )

    # Verify that the slug ends with a slash
    if not slug.endswith("/"):
        raise ValueError("Packaging slug must end with a slash.")

    # Verify that the slug contains only one slash
    if slug.count("/") != 1:
        raise ValueError("Packaging slug can only contain one slash.")

    # Verify that the slug only contains two to five terms separated by hyphens
    terms = slug.split("/")[0].split("-")
    if len(terms) < 2 or len(terms) > 5:
        raise ValueError(
            "Packaging slug must contain two to five terms separated by hyphens."
        )

    # Verify that all of the terms are at least two characters long
    for term in terms:
        if len(term) < 2:
            raise ValueError(
                "Packaging slug terms must be at least two characters long."
            )

    # Verify that the terms are only alphanumeric
    for term in terms:
        if not term.isalnum():
            raise ValueError("Packaging slug terms can only be alphanumeric.")

    # Verify that there are no duplicate terms
    if len(terms) != len(set(terms)):
        raise ValueError("Packaging slug terms cannot be duplicated.")

    # If we got this far, the slug is valid
    return True


def validate_wild_slug(slug: str) -> bool:
    """Check whether a wild slug is valid.

    Style guide entry:

        A slug is a simple human readable method of grouping content for packaging,
        either internally or externally. By using the same slug for the same real world
        event Reuters can ensure that it is easy to find pictures, text, graphics,
        video, audio that all belong together.

        A slug has two parts:

        • a packaging slug (FERRARI-IPO/)
        • a wild slug (PROSPECTUS)

        They come together as the full slug in FERRARI-IPO/PROSPECTUS.

        If this story develops other angles that warrant separate content, you can add
        words after the “/” mark, like this: MALAYSIA-POLITICS/STATEMENT, MALAYSIA-POLITICS/PROTEST,
        or BRITAIN-POLITICS/PM. The part after the “/” mark is called the wild slug.

    Args:
        slug: The wild slug to validate. (str)

    Returns:
        Whether the wild slug is valid. (bool)

    Raises:
        ValueError: If the wild slug is invalid.

    Examples:
        >>> import reuters_style
        >>> reuters_style.validate_wild_slug('PROSPECTUS')
        True
        >>> reuters_style.validate_wild_slug('PROSPECTUS REPORT')
        Traceback (most recent call last):
            ...
        ValueError: Wild slug can only contain uppercase letters, hyphens and slashes.
    """
    # Verify that the slug is a string
    if not isinstance(slug, str):
        raise ValueError("Wild slug must be a string.")

    # Verify that the slug is not empty
    if not slug:
        raise ValueError("Wild slug cannot be empty.")

    # Verify that the slug is not too long
    if len(slug) > 64:
        raise ValueError("Wild slug cannot be longer than 64 characters.")

    # Verify that the slug only contains uppercase letter, hyphens and slashes
    if not slug.isupper():
        raise ValueError(
            "Wild slug can only contain uppercase letters, hyphens and slashes."
        )

    # Verify that the slug does not include a slash
    if "/" in slug:
        raise ValueError("Wild slug cannot contain a slash.")

    # Verify that the slug only contains one to five terms separated by hyphens
    terms = slug.split("-")
    if len(terms) > 5:
        raise ValueError(
            "Wild slug must contain one to five terms separated by hyphens."
        )

    # Verify that all of the terms are at least two characters long
    for term in terms:
        if len(term) < 2:
            raise ValueError("Wild slug terms must be at least two characters long.")

    # Verify that the terms are only alphanumeric
    for term in terms:
        if not term.isalnum():
            raise ValueError("Wild slug terms can only be alphanumeric.")

    # Verify that there are no duplicate terms
    if len(terms) != len(set(terms)):
        raise ValueError("Wild slug terms cannot be duplicated.")

    # If we got this far, the slug is valid
    return True


@dataclass
class RIC:
    """Metadata about a Refinitiv Instrument Code.

    Refinitiv Instrument Codes (RICs), or ticker symbols, are crucial in helping customers
    find news and market data. All financial instruments — stocks, bonds, currencies and commodities —
    as well as many types of economic data have RICs.

    Examples include IBM.N, EUR=, and XAU=.
    """

    code: str  #: The Refinitiv Instrument Code
    title: str  #: The more verbose definition of the code

    def __str__(self) -> str:
        """Generate the string representation of the RIC.

        Returns:
            The RIC code. (str)
        """
        return self.code


@dataclass
class Slug:
    """A full Reuters slug.

    Style guide entry:

        A slug is a simple human readable method of grouping content for packaging,
        either internally or externally. By using the same slug for the same real world
        event Reuters can ensure that it is easy to find pictures, text, graphics,
        video, audio that all belong together.

        A slug has two parts:

        • a packaging slug (FERRARI-IPO/)
        • a wild slug (PROSPECTUS)

        They come together as the full slug in FERRARI-IPO/PROSPECTUS.
    """

    packaging_slug: str  #: The packaging slug
    wild_slug: str  #: The wild slug

    def __str__(self) -> str:
        """Generate the string representation of the slug.

        Returns:
            The full slug. (str)
        """
        return f"{self.packaging_slug}{self.wild_slug}"

    def __eq__(self, other: object) -> bool:
        """Compare two slugs.

        Args:
            other: The other slug to compare. (Slug)

        Returns:
            Whether the slugs are equal. (bool)
        """
        if not isinstance(other, Slug):
            return NotImplemented
        return str(self) == str(other)

    @property
    def full_slug(self) -> str:
        """The full slug.

        Returns:
            The full slug. (str)
        """
        return str(self)

    def validate(self) -> bool:
        """Validate the slug.

        Returns:
            Whether the slug is valid. (bool)

        Raises:
            ValueError: If the slug is invalid.
        """
        return validate_slug(str(self))
