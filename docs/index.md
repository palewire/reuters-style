# reuters-style

A Python library for Reuters editorial formatting and Graphics chart colours.

## Install

```sh
pip install reuters-style
```

## Use

```python
from datetime import datetime

import reuters_style

reuters_style.date(datetime(2021, 9, 1))  # "Sept. 1, 2021"
reuters_style.validate_slug("FERRARI-IPO/PROSPECTUS")  # True
```

The [API reference](api) documents each formatter, validator and data object.
The [Graphics colours](colors) page is a quick reference for charts and maps.

```{toctree}
:maxdepth: 2
:hidden:

api
colors
```

## Project links

- [Source code](https://github.com/palewire/reuters-style)
- [Issues](https://github.com/palewire/reuters-style/issues)
- [Package on PyPI](https://pypi.org/project/reuters-style/)
