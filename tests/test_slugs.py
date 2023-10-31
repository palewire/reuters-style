"""Test slug methods."""
import pytest

import reuters_style


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
