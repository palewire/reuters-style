"""Reuters Graphics colors for charts and maps.

Each named palette is an immutable tuple, so its colors can be addressed by
role or passed directly to a chart as an ordered sequence. Scales are stored
as the nine exact stops in the Graphics guide, from low to high; diverging
scales run from the negative side through the midpoint to the positive side.

Examples:
    >>> from reuters_style import colors
    >>> colors.GRAPHICS_PRIMARY.rust
    '#cb643c'
    >>> list(colors.GRAPHICS_PRIMARY[:2])
    ['#cb643c', '#4e75ad']
    >>> colors.SEQUENTIAL.blue[0]
    '#f9fafd'
"""

from __future__ import annotations

from typing import NamedTuple, TypeAlias

__all__ = [
    "DIVERGING",
    "GRAPHICS_MAPS",
    "GRAPHICS_MONO",
    "GRAPHICS_PRIMARY",
    "ROLES",
    "SEQUENTIAL",
    "US_POLITICS",
    "DivergingScales",
    "GraphicsMaps",
    "GraphicsMono",
    "GraphicsPrimary",
    "NineStepScale",
    "SemanticRoles",
    "SequentialScales",
    "USPolitics",
]

NineStepScale: TypeAlias = tuple[str, str, str, str, str, str, str, str, str]


class GraphicsPrimary(NamedTuple):
    """Six unordered categories in their recommended series order."""

    rust: str
    blue: str
    teal: str
    plum: str
    green: str
    yellow: str


class GraphicsMono(NamedTuple):
    """Seven neutral steps, from white to near-black."""

    white: str
    grey_100: str
    grey_200: str
    grey_300: str
    grey_400: str
    grey_500: str
    black: str


class SemanticRoles(NamedTuple):
    """Colors for emphasis, context, change, gaps and annotations."""

    focus: str
    muted: str
    positive: str
    negative: str
    no_data: str
    annotation: str


class GraphicsMaps(NamedTuple):
    """Map labels, area fills and emphasis marks, in guide order."""

    label_primary: str
    label_secondary: str
    label_water: str
    fill_neutral: str
    fill_primary: str
    emphasis_primary: str
    emphasis_secondary: str
    highlight: str


class USPolitics(NamedTuple):
    """Election result colors: wins, flips and a shared tie."""

    rep_win: str
    rep_flip: str
    dem_win: str
    dem_flip: str
    ind_win: str
    ind_flip: str
    tie: str


class SequentialScales(NamedTuple):
    """Nine-step quantity scales, from low values to high values."""

    rust: NineStepScale
    blue: NineStepScale
    teal: NineStepScale
    plum: NineStepScale
    green: NineStepScale
    yellow: NineStepScale
    yellow_blue: NineStepScale
    yellow_green: NineStepScale
    yellow_plum: NineStepScale


class DivergingScales(NamedTuple):
    """Nine-step change scales, from negative through zero to positive."""

    blue_rust: NineStepScale
    blue_yellow: NineStepScale
    teal_yellow: NineStepScale


GRAPHICS_PRIMARY = GraphicsPrimary(
    rust="#cb643c",
    blue="#4e75ad",
    teal="#499e9a",
    plum="#7b3f71",
    green="#2a6e4d",
    yellow="#daad3d",
)

GRAPHICS_MONO = GraphicsMono(
    white="#ffffff",
    grey_100="#d5d5d5",
    grey_200="#adadad",
    grey_300="#878787",
    grey_400="#666666",
    grey_500="#404040",
    black="#212223",
)

ROLES = SemanticRoles(
    focus=GRAPHICS_PRIMARY.rust,
    muted=GRAPHICS_MONO.grey_200,
    positive=GRAPHICS_PRIMARY.green,
    negative=GRAPHICS_PRIMARY.rust,
    no_data="#f4f4f4",
    annotation=GRAPHICS_MONO.grey_400,
)

GRAPHICS_MAPS = GraphicsMaps(
    label_primary=GRAPHICS_MONO.black,
    label_secondary=GRAPHICS_MONO.grey_300,
    label_water=GRAPHICS_PRIMARY.blue,
    fill_neutral=GRAPHICS_MONO.grey_100,
    fill_primary="#eeb49d",
    emphasis_primary="#d0381e",
    emphasis_secondary="#8914a2",
    highlight="#ffca05",
)

US_POLITICS = USPolitics(
    rep_win="#d02a41",
    rep_flip="#7c000f",
    dem_win="#1c7cb3",
    dem_flip="#004c7f",
    ind_win="#60c160",
    ind_flip="#008000",
    tie="#f7d131",
)

SEQUENTIAL = SequentialScales(
    rust=(
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
    blue=(
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
    teal=(
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
    plum=(
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
    green=(
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
    yellow=(
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
    yellow_blue=(
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
    yellow_green=(
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
    yellow_plum=(
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
)

DIVERGING = DivergingScales(
    blue_rust=(
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
    blue_yellow=(
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
    teal_yellow=(
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
)
