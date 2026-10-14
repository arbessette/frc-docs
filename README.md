# FRC Documentation

Draft documentation for FIRST Robotics Competition robot hardware, assembly,
wiring, troubleshooting, and competition preparation. Uses the Furo theme
and styles adapted from WPILib Documentation.

## Setup and preview

Requires Python 3.12 or newer.

```sh
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
make check
make preview
```

Open http://127.0.0.1:8000. Stop the server with Ctrl+C.
If you use uv, `uv sync` creates the environment instead.

`make check` rebuilds with warnings treated as errors and strict references.
`make linkcheck` checks external links separately. Builds download the WPILib
Intersphinx inventory and need network access on the first run.

## Content

Sections include the 2027 Robot Overview, Zero to Robot, Hardware, Vendors,
Assembly, Competition, and Resources. Hardware references and supporting
images were adapted from WPILib Documentation, with original paths and
attribution preserved. Older roboRIO wiring examples are labeled so they
are not mistaken for Systemcore wiring instructions.

Software and programming guides remain linked to WPILib. Some sections
are still starter content; this is not an official competition rule source.

Edit `source/index.rst` for navigation and `source/conf.py` for site settings.
The GitHub Actions workflow checks the documentation build and uploads an
HTML preview artifact. Website hosting is not configured.

See ATTRIBUTION.md and LICENSE.txt for attribution and licensing.
