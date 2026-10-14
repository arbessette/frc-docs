"""FRC Docs: local prototype using the WPILib Furo design."""
project = "FRC Documentation"
author = "FRC Docs contributors"
copyright = "2026, FRC Docs contributors; CC BY 4.0"
release = "0.1"
extensions = ["sphinx_design", "sphinx.ext.intersphinx", "sphinx.ext.autosectionlabel", "sphinx.ext.mathjax", "sphinxcontrib.youtube"]
autosectionlabel_prefix_document = True
nitpicky = True
root_doc = "index"
exclude_patterns = []
html_theme = "furo"
html_title = "FRC Documentation"
html_logo = "_static/images/wpilibDocsLogo.png"
templates_path = ["_templates"]
html_static_path = ["_static"]
html_css_files = ["css/wpilib-rtd.css", "css/sw-components.css", "css/frc-docs.css"]
html_theme_options = {
    "announcement": "<strong>DRAFT</strong> &mdash; FRC Docs local prototype. Starter content is under review.",
    "light_css_variables": {
        "color-sidebar-background": "#003974",
        "color-sidebar-brand-text": "#ffffff",
        "color-sidebar-link-text": "#d9e5f2",
        "color-sidebar-link-text--top-level": "#ffffff",
        "color-sidebar-caption-text": "#bdcfe3",
        "color-background-hover": "#023160",
    },
}
intersphinx_mapping = {
    "wpilib": ("https://docs.wpilib.org/en/stable/", None),
}
intersphinx_disabled_reftypes = ["*"]
intersphinx_timeout = 15
linkcheck_timeout = 15
linkcheck_retries = 2
linkcheck_anchors = False
