"""Test our dataclass objects."""
import pytest

import reuters_style


def test_ric():
    """Test the RIC object."""
    ric = reuters_style.RIC(code="AAPL.O", title="Apple Inc")
    assert ric.code == "AAPL.O"
    assert ric.title == "Apple Inc"
    assert str(ric) == "AAPL.O"


def test_slug():
    """Test the Slug object."""
    slug = reuters_style.Slug(packaging_slug="FERRARI-RESULTS/", wild_slug="PROSPECTUS")
    assert slug.packaging_slug == "FERRARI-RESULTS/"
    assert slug.wild_slug == "PROSPECTUS"
    assert str(slug) == "FERRARI-RESULTS/PROSPECTUS"
    assert slug.full_slug == "FERRARI-RESULTS/PROSPECTUS"
    assert slug.validate() is True

    # Test a slug with invalid inputs
    slug = reuters_style.Slug(
        packaging_slug="FERRARI-RESULssss ", wild_slug="PROSPECTUS"
    )
    with pytest.raises(ValueError):
        slug.validate()
