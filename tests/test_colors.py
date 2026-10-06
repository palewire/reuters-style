"""Exact values and ordering from the Reuters Graphics colour guide."""

import pytest

from reuters_style import colors


def test_named_palettes() -> None:
    """Check every named colour and the recommended order.

    Returns:
        None. Assertions fail if a guide value or name changes.

    Examples:
        >>> test_named_palettes()
    """
    assert colors.GRAPHICS_PRIMARY._asdict() == {
        "rust": "#cb643c",
        "blue": "#4e75ad",
        "teal": "#499e9a",
        "plum": "#7b3f71",
        "green": "#2a6e4d",
        "yellow": "#daad3d",
    }
    assert colors.GRAPHICS_MONO._asdict() == {
        "white": "#ffffff",
        "grey_100": "#d5d5d5",
        "grey_200": "#adadad",
        "grey_300": "#878787",
        "grey_400": "#666666",
        "grey_500": "#404040",
        "black": "#212223",
    }
    assert colors.ROLES._asdict() == {
        "focus": "#cb643c",
        "muted": "#adadad",
        "positive": "#2a6e4d",
        "negative": "#cb643c",
        "no_data": "#f4f4f4",
        "annotation": "#666666",
    }
    assert colors.GRAPHICS_MAPS._asdict() == {
        "label_primary": "#212223",
        "label_secondary": "#878787",
        "label_water": "#4e75ad",
        "fill_neutral": "#d5d5d5",
        "fill_primary": "#eeb49d",
        "emphasis_primary": "#d0381e",
        "emphasis_secondary": "#8914a2",
        "highlight": "#ffca05",
    }
    assert colors.US_POLITICS._asdict() == {
        "rep_win": "#d02a41",
        "rep_flip": "#7c000f",
        "dem_win": "#1c7cb3",
        "dem_flip": "#004c7f",
        "ind_win": "#60c160",
        "ind_flip": "#008000",
        "tie": "#f7d131",
    }
    assert colors.GRAPHICS_PRIMARY[:2] == ("#cb643c", "#4e75ad")
    assert isinstance(colors.GRAPHICS_MAPS, tuple)
    with pytest.raises(AttributeError):
        colors.GRAPHICS_PRIMARY.rust = "#000000"  # type: ignore[misc]


@pytest.mark.parametrize(
    ("scale", "expected"),
    [
        pytest.param(
            colors.SEQUENTIAL.rust,
            (
                "#fefaf8",
                "#f8d6ca",
                "#eeb49d",
                "#e19273",
                "#cb643c",
                "#b05735",
                "#88452b",
                "#623321",
                "#3e2318",
            ),
            id="sequential-rust",
        ),
        pytest.param(
            colors.SEQUENTIAL.blue,
            (
                "#f9fafd",
                "#d7dded",
                "#b5c1dc",
                "#93a6cb",
                "#6f8bbb",
                "#4e75ad",
                "#3b5983",
                "#2c405f",
                "#1d2a3e",
            ),
            id="sequential-blue",
        ),
        pytest.param(
            colors.SEQUENTIAL.teal,
            (
                "#f7fbfb",
                "#cbe2e0",
                "#9ec9c6",
                "#70b0ad",
                "#499e9a",
                "#367b78",
                "#29605d",
                "#1b4644",
                "#0f2e2d",
            ),
            id="sequential-teal",
        ),
        pytest.param(
            colors.SEQUENTIAL.plum,
            (
                "#fdfafc",
                "#e8d9e4",
                "#d3bacd",
                "#be9bb6",
                "#a97da0",
                "#945f8a",
                "#7b3f71",
                "#5a3253",
                "#382334",
            ),
            id="sequential-plum",
        ),
        pytest.param(
            colors.SEQUENTIAL.green,
            (
                "#f7fcf9",
                "#d2e1d8",
                "#aec7b8",
                "#8aad99",
                "#67947b",
                "#437c5e",
                "#2a6e4d",
                "#1b4832",
                "#152e21",
            ),
            id="sequential-green",
        ),
        pytest.param(
            colors.SEQUENTIAL.yellow,
            (
                "#fcfaf7",
                "#f4daad",
                "#e4bc64",
                "#daad3d",
                "#a88631",
                "#896d28",
                "#6b5520",
                "#4e3e18",
                "#332811",
            ),
            id="sequential-yellow",
        ),
        pytest.param(
            colors.SEQUENTIAL.yellow_blue,
            (
                "#fcfaf7",
                "#f2dbaa",
                "#dabe7d",
                "#b6a474",
                "#8b8c7d",
                "#617384",
                "#3e597d",
                "#284064",
                "#1d2a3e",
            ),
            id="sequential-yellow-blue",
        ),
        pytest.param(
            colors.SEQUENTIAL.yellow_green,
            (
                "#fcfaf7",
                "#e5ddbf",
                "#c8c489",
                "#a4ac5c",
                "#7c953e",
                "#567d31",
                "#35632e",
                "#1f492a",
                "#152e21",
            ),
            id="sequential-yellow-green",
        ),
        pytest.param(
            colors.SEQUENTIAL.yellow_plum,
            (
                "#fcfaf7",
                "#f0dac0",
                "#e8b590",
                "#de906f",
                "#c96d5f",
                "#ab525a",
                "#853f55",
                "#5d3048",
                "#382334",
            ),
            id="sequential-yellow-plum",
        ),
        pytest.param(
            colors.DIVERGING.blue_rust,
            (
                "#2c405f",
                "#4b6896",
                "#6493d8",
                "#aebfe4",
                "#f5edde",
                "#e7b3a0",
                "#e0734a",
                "#9f5235",
                "#623321",
            ),
            id="diverging-blue-rust",
        ),
        pytest.param(
            colors.DIVERGING.blue_yellow,
            (
                "#2c405f",
                "#4b6896",
                "#6493d8",
                "#aebfe4",
                "#f5edde",
                "#dcbb75",
                "#ae8e45",
                "#7b6533",
                "#4e3e18",
            ),
            id="diverging-blue-yellow",
        ),
        pytest.param(
            colors.DIVERGING.teal_yellow,
            (
                "#1b4644",
                "#3c706d",
                "#549e9a",
                "#83cbc7",
                "#f5edde",
                "#dcbb75",
                "#ae8e45",
                "#7b6533",
                "#4e3e18",
            ),
            id="diverging-teal-yellow",
        ),
    ],
)
def test_exact_scale_stops(
    scale: colors.NineStepScale, expected: colors.NineStepScale
) -> None:
    """Check all nine stops in a sequential or diverging scale.

    Args:
        scale: The exported scale to inspect.
        expected: The exact nine colours in the Graphics guide.

    Returns:
        None. Assertions fail if any stop or its position changes.

    Examples:
        >>> test_exact_scale_stops(colors.SEQUENTIAL.rust, colors.SEQUENTIAL.rust)
    """
    assert scale == expected
    assert len(scale) == 9


def test_scale_relationships() -> None:
    """Check shared endpoints and the common diverging midpoint.

    Returns:
        None. Assertions fail when a shared guide colour differs.

    Examples:
        >>> test_scale_relationships()
    """
    assert len(colors.SEQUENTIAL) == 9
    assert len(colors.DIVERGING) == 3
    assert colors.SEQUENTIAL.yellow_blue[0] == colors.SEQUENTIAL.yellow[0]
    assert colors.SEQUENTIAL.yellow_green[-1] == colors.SEQUENTIAL.green[-1]
    assert colors.SEQUENTIAL.yellow_plum[-1] == colors.SEQUENTIAL.plum[-1]
    assert all(scale[4] == "#f5edde" for scale in colors.DIVERGING)
    assert colors.DIVERGING.blue_rust[0] == colors.SEQUENTIAL.blue[-2]
    assert colors.DIVERGING.blue_rust[-1] == colors.SEQUENTIAL.rust[-2]
