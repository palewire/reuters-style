```{include} _templates/nav.html
```

# reuters-style

A Python library that format dates, numbers and text to conform with the Reuters Style Guide, the standards that guide the world's largest independent newsroom

```{contents} Sections
  :depth: 1
  :local:
```

## Installation

Install the package from the Python Package Index (PyPI) with pipenv:

```bash
pipenv install reuters-style
```

## Functions

A collection of functions for formatting date, text and numbers:

* [date](#reuters_style.date)
* [dayofweek](#reuters_style.dayofweek)
* [time](#reuters_style.time)
* [validate_slug](#reuters_style.validate_slug)
* [validate_packaging_slug](#reuters_style.validate_packaging_slug)
* [validate_wild_slug](#reuters_style.validate_wild_slug)

```{eval-rst}
.. autofunction:: reuters_style.date
.. autofunction:: reuters_style.dayofweek
.. autofunction:: reuters_style.time
.. autofunction:: reuters_style.validate_slug
.. autofunction:: reuters_style.validate_packaging_slug
.. autofunction:: reuters_style.validate_wild_slug
```

## Objects

A set of [dataclasses](https://docs.python.org/3/library/dataclasses.html) for formatting Reuters-specific objects:

* [RIC](#reuters_style.RIC)
* [Slug](#reuters_style.Slug)

```{eval-rst}
.. autoclass:: reuters_style.RIC
.. autoclass:: reuters_style.Slug
```

## Links

- Code: [github.com/palewire/reuters-style](https://github.com/palewire/reuters-style)
- Issues: [github.com/palewire/reuters-style/issues](https://github.com/palewire/reuters-style/issues)
- Packaging: [pypi.org/project/reuters-style](https://pypi.org/project/reuters-style)
