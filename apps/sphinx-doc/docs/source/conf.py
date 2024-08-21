# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Docker Sphinx Doc'
copyright = '2024, Marcin Prączko'
author = 'Marcin Prączko'

# The full version, including alpha/beta/rc tags
release = '0.1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "ablog",
    "myst_parser",
    "sphinx_panels",
    "sphinx_tabs.tabs",
    "sphinx.ext.githubpages", 
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- PyData theme and ABLOG --
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

post_auto_image = 1

html_theme_options = {
    "navigation_with_keys": False,
    "navbar_align": "right",
    "logo": {
        "text": "Docker Sphinx Doc",
    },
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/marcinpraczko/mposl_collector/tree/master/apps/sphinx-doc",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },
    ],
    "icon_links_label": "Quick Links",
    "use_edit_page_button": True,
    "back_to_top_button": True,
}

html_context = {
    "github_url": "https://github.com", # or your GitHub Enterprise site
    "github_user": "marcinpraczko",
    "github_repo": "mposl_collector",
    "github_version": "master",
    "doc_path": "apps/sphinx-doc/docs/source",
}
