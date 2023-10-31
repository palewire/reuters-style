"""Test slug methods."""
import pytest

import reuters_style


def test_validate_slug():
    """Test validate_slug()."""
    assert reuters_style.validate_slug("FERRARI-IPO/")
    assert reuters_style.validate_slug("FERRARI-IPO/PROSPECTUS")
    with pytest.raises(ValueError):
        reuters_style.validate_slug("FERRARIIPO")
    with pytest.raises(ValueError):
        reuters_style.validate_slug("FERRaRI-IPO")
    with pytest.raises(ValueError):
        reuters_style.validate_slug("FERRARI IPO")
    with pytest.raises(ValueError):
        reuters_style.validate_slug(
            "FERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARI-IPO-FOO/WILD-SLUG"
        )
    with pytest.raises(ValueError):
        reuters_style.validate_slug(222)
    with pytest.raises(ValueError):
        reuters_style.validate_slug("")
    with pytest.raises(ValueError):
        reuters_style.validate_slug(None)


def test_validate_packaging_slug():
    """Test validate_packaging_slug()."""
    assert reuters_style.validate_packaging_slug("FERRARI-IPO/")
    with pytest.raises(ValueError):
        reuters_style.validate_packaging_slug("FERRARIIPO")
    with pytest.raises(ValueError):
        reuters_style.validate_packaging_slug("FERRaRI-IPO/")
    with pytest.raises(ValueError):
        reuters_style.validate_packaging_slug("FERRARI IPO")
    with pytest.raises(ValueError):
        reuters_style.validate_packaging_slug("FERRARI-IPO")
    with pytest.raises(ValueError):
        reuters_style.validate_packaging_slug("FERRARI-IPO/FOO")
    with pytest.raises(ValueError):
        reuters_style.validate_packaging_slug(222)
    with pytest.raises(ValueError):
        reuters_style.validate_packaging_slug("")
    with pytest.raises(ValueError):
        reuters_style.validate_packaging_slug(None)
    with pytest.raises(ValueError):
        reuters_style.validate_packaging_slug(
            "FERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARIFERRARI-IPO/"
        )
    with pytest.raises(ValueError):
        reuters_style.validate_packaging_slug("FERRARI-IPO//")
    with pytest.raises(ValueError):
        reuters_style.validate_packaging_slug("FERRARI-IPO-FOO-BAR-BAZ-QUX/")
    with pytest.raises(ValueError):
        reuters_style.validate_packaging_slug("FERRARI/")
    with pytest.raises(ValueError):
        reuters_style.validate_packaging_slug("FERRARI-I/")
    with pytest.raises(ValueError):
        reuters_style.validate_packaging_slug("FERRARI-CA$H/")
    with pytest.raises(ValueError):
        reuters_style.validate_packaging_slug("FERRARI-FERRARI/")


def test_validate_wild_slug():
    """Test validate_wild_slug()."""
    assert reuters_style.validate_wild_slug("PROSPECTUS")
    with pytest.raises(ValueError):
        reuters_style.validate_wild_slug("PROSPECTUS/")
    with pytest.raises(ValueError):
        reuters_style.validate_wild_slug("PROSPECTUS//")
    with pytest.raises(ValueError):
        reuters_style.validate_wild_slug("PROSPECTUS/FOO")
    with pytest.raises(ValueError):
        reuters_style.validate_wild_slug("A")
    with pytest.raises(ValueError):
        reuters_style.validate_wild_slug(None)
    with pytest.raises(ValueError):
        reuters_style.validate_wild_slug(1)
    with pytest.raises(ValueError):
        reuters_style.validate_wild_slug("")
    with pytest.raises(ValueError):
        reuters_style.validate_wild_slug(
            "PROSPECTUSFOOPROSPECTUSFOOPROSPECTUSFOOPROSPECTUSFOOPROSPECTUSFOOPROSPECTUSFOOPROSPECTUSFOOPROSPECTUSFOO"
        )
    with pytest.raises(ValueError):
        reuters_style.validate_wild_slug("PROSPECTUsss")
    with pytest.raises(ValueError):
        reuters_style.validate_wild_slug("PROSPECTUS-FOO-BAR-BAZ-QUX-WUX")
    with pytest.raises(ValueError):
        reuters_style.validate_wild_slug("PROSPECTUS-FOO$BAR")
    with pytest.raises(ValueError):
        reuters_style.validate_wild_slug("PROSPECTUS-FOO-FOO")
