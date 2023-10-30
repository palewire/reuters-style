"""Configuration file for the Sphinx documentation builder."""
import os
import sys
from datetime import datetime

# Insert the parent directory into the path
sys.path.insert(0, os.path.abspath("../"))

project = "reuters-style"
year = datetime.now().year
copyright = f"{year}"
author = "Ben Welsh"

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "alabaster"
html_baseurl = "/docs/"
pygments_style = "sphinx"
html_sidebars = {
    "**": [
        # "about.html",
        # "navigation.html",
        "relations.html",
        "searchbox.html",
    ]
}

html_static_path = ["_static"]
html_css_files = [
    "css/custom.css",
]

autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "show-inheritance": True,
}
autodoc_mock_imports = ["pytz"]

extensions = [
    "myst_parser",
    "sphinx_click",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinxcontrib.mermaid",
]
