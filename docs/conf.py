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

project = 'Programming for Cognitive and Brain Sciences'
copyright = 'CC-BY-SA 2019, Christophe Pallier'
author = 'Christophe Pallier'


# -- General configuration ---------------------------------------------------

source_suffix = ['.rst', '.md']
source_encoding = 'utf-8-sig'


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "recommonmark",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    # "nbsphinx"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

master_doc = 'index'
root_doc = 'index'

language = 'en'

latex_engine = 'xelatex'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'master'
#html_theme = 'pyramid'
#html_theme = 'classic'
html_theme = "sphinx_rtd_theme"
#html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# html_theme_options = {
#     # Disable showing the sidebar. Defaults to 'false'
#     'nosidebar': True,
# }

#def setup(app):
#    app.add_css_file('my_theme.css')

highlight_language = 'python3'
html_context = {'display_github': True, 'github_user': 'chrplr', 'github_repo': 'PCBS', 'github_version': 'master/sample-docs/', 'github_root_dir': 'master/src', 'current_version': 'latest', 'latest_version': 'latest', 'available_versions': ('latest', ), 'css_files': (), }
#html_theme_options = {'collapse_navigation': False, 'analytics_id': '', 'style_nav_header_background': '#5bbdbf', 'style_external_links': True, 'canonical_url': 'https://pradyunsg.me/sphinx-themes/', 'vcs_pageview_mode': 'edit', 'navigation_depth': 3, }
pygments_style = 'sphinx'
     

#latex_toplevel_sectioning = 'part'
latex_show_urls = 'footnote'
