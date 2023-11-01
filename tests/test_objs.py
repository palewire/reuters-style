"""Test our dataclass objects."""
import reuters_style


def test_ric():
    """Test the RIC object."""
    ric = reuters_style.RIC(code="AAPL.O", title="Apple Inc")
    assert ric.code == "AAPL.O"
    assert ric.title == "Apple Inc"
    assert str(ric) == "AAPL.O"
