# Graphics colors

Use the palette that matches the job the color is doing. These are the exact
values in the [Reuters Graphics color guide](https://graphics.thomsonreuters.com/testfiles/2026/o96NvTQkPV/).

```python
from reuters_style import colors

colors.GRAPHICS_PRIMARY.rust  # '#cb643c' — first category
colors.GRAPHICS_PRIMARY[:2]  # ('#cb643c', '#4e75ad')
colors.ROLES.muted  # '#adadad' — context series
colors.SEQUENTIAL.blue  # nine stops, low to high
colors.DIVERGING.blue_rust  # negative → midpoint → positive
colors.GRAPHICS_MAPS.label_water  # '#4e75ad'
colors.US_POLITICS.dem_win  # '#1c7cb3'
```

The named groups are immutable tuples: use a field for one color, or pass the
whole group to a chart that needs an ordered sequence.

| Group | Use |
| --- | --- |
| `GRAPHICS_PRIMARY` | Six unordered series: rust, blue, teal, plum, green, yellow. Use them in order. |
| `GRAPHICS_MONO` | Seven neutrals from white to near-black; use grey for context. |
| `ROLES` | `focus`, `muted`, `positive`, `negative`, `no_data`, `annotation`. |
| `SEQUENTIAL` | Six single-hue and three yellow-to-color quantity scales, each with nine low-to-high stops. |
| `DIVERGING` | Three nine-stop scales for change around a meaningful midpoint: `blue_rust`, `blue_yellow`, `teal_yellow`. |
| `GRAPHICS_MAPS` | Eight named map-label, area-fill and emphasis roles. |
| `US_POLITICS` | Wins and flips for three parties, plus a shared tie color. |

Do not extend the six-category palette by cycling it. For more series, consider
small multiples or highlight one series against grey. Yellow needs an outline
or direct label when its boundary matters on white; pale map and election fills
also need legible labels. Check marks against their actual background, not just
large swatches.
