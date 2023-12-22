"""Sphinx configuration."""
project = "GridWorks Weather Service"
author = "Jessica Millar"
copyright = "2023, Jessica Millar"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
