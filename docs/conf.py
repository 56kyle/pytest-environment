"""Sphinx configuration."""

project = "Pytest Environment"
author = "Kyle Oliver"
copyright = "2024, Kyle Oliver"  # noqa: A001
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
