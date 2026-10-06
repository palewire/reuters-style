"""Test slug validation and its specific error messages."""

import pytest

import reuters_style


def test_validate_slug() -> None:
    """Accept full slugs with and without a wild-slug suffix."""
    assert reuters_style.validate_slug("FERRARI-IPO/")
    assert reuters_style.validate_slug("FERRARI-IPO/PROSPECTUS")


@pytest.mark.parametrize(
    ("slug", "message"),
    [
        ("FERRARIIPO", "Full slug can only contain one slash"),
        ("FERRaRI-IPO", "Full slug can only contain one slash"),
        ("FERRARI IPO", "Full slug can only contain one slash"),
        (
            "FERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARI-IPO-FOO/WILD-SLUG",
            "Full slug cannot be longer than 64 characters",
        ),
        (222, "Full slug must be a string"),
        ("", "Full slug cannot be empty"),
        (None, "Full slug must be a string"),
    ],
)
def test_validate_slug_rejects_invalid_input(slug: object, message: str) -> None:
    """Report why a full slug is invalid."""
    with pytest.raises(ValueError, match=message):
        reuters_style.validate_slug(slug)  # type: ignore[arg-type]


def test_validate_packaging_slug() -> None:
    """Accept a valid packaging slug."""
    assert reuters_style.validate_packaging_slug("FERRARI-IPO/")


@pytest.mark.parametrize(
    ("slug", "message"),
    [
        ("FERRARIIPO", "Packaging slug must end with a slash"),
        ("FERRaRI-IPO/", "Packaging slug can only contain uppercase"),
        ("FERRARI IPO", "Packaging slug must end with a slash"),
        ("FERRARI-IPO", "Packaging slug must end with a slash"),
        ("FERRARI-IPO/FOO", "Packaging slug must end with a slash"),
        (222, "Packaging slug must be a string"),
        ("", "Packaging slug cannot be empty"),
        (None, "Packaging slug must be a string"),
        (
            "FERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARI-IPO/",
            "Packaging slug cannot be longer than 64 characters",
        ),
        ("FERRARI-IPO//", "Packaging slug can only contain one slash"),
        ("FERRARI-IPO-FOO-BAR-BAZ-QUX/", "two to five terms"),
        ("FERRARI/", "two to five terms"),
        ("FERRARI-I/", "at least two characters"),
        ("FERRARI-CA$H/", "terms can only be alphanumeric"),
        ("FERRARI-FERRARI/", "terms cannot be duplicated"),
    ],
)
def test_validate_packaging_slug_rejects_invalid_input(
    slug: object, message: str
) -> None:
    """Report why a packaging slug is invalid."""
    with pytest.raises(ValueError, match=message):
        reuters_style.validate_packaging_slug(slug)  # type: ignore[arg-type]


def test_validate_wild_slug() -> None:
    """Accept a valid wild slug."""
    assert reuters_style.validate_wild_slug("PROSPECTUS")


@pytest.mark.parametrize(
    ("slug", "message"),
    [
        ("PROSPECTUS/", "Wild slug cannot contain a slash"),
        ("PROSPECTUS//", "Wild slug cannot contain a slash"),
        ("PROSPECTUS/FOO", "Wild slug cannot contain a slash"),
        ("A", "at least two characters"),
        (None, "Wild slug must be a string"),
        (1, "Wild slug must be a string"),
        ("", "Wild slug cannot be empty"),
        (
            "PROSPECTUSFOOPROSPECTUSFOOPROSPECTUSFOOPROSPECTUSFOOPROSPECTUSFOOPROSPECTUSFOOPROSPECTUSFOOPROSPECTUSFOO",
            "Wild slug cannot be longer than 64 characters",
        ),
        ("PROSPECTUsss", "Wild slug can only contain uppercase"),
        ("PROSPECTUS-FOO-BAR-BAZ-QUX-WUX", "one to five terms"),
        ("PROSPECTUS-FOO$BAR", "terms can only be alphanumeric"),
        ("PROSPECTUS-FOO-FOO", "terms cannot be duplicated"),
    ],
)
def test_validate_wild_slug_rejects_invalid_input(slug: object, message: str) -> None:
    """Report why a wild slug is invalid."""
    with pytest.raises(ValueError, match=message):
        reuters_style.validate_wild_slug(slug)  # type: ignore[arg-type]
