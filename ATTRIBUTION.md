The Furo configuration and source/_static/css/wpilib-rtd.css and
source/_static/css/sw-components.css come from the sibling wpilib-docs checkout
(FIRST and WPILib contributors). Upstream: https://github.com/wpilibsuite/wpilib-docs
License: Creative Commons Attribution 4.0, https://creativecommons.org/licenses/by/4.0/

Local overrides in frc-docs.css adapt branding, content width, and navigation.
The sidebar uses source/_static/images/wpilibDocsLogo.png from the same
WPILib checkout, showing the FIRST and WPILib logos and partnership text.
The sidebar brand template adapts WPILib's source/_templates/sidebar/brand.html.
FIRST and WPILib branding belongs to its respective owners.
No official-site metadata is included.

The eleven Hardware and Zero to Robot articles and their supporting images
were imported from the sibling wpilib-docs checkout under the same CC BY 4.0
license. Their original document paths are preserved. Markdown-style headings
and links were converted to reStructuredText using upstream's redown converter;
references to pages and glossary terms remaining in WPILib use Intersphinx.
Expandable instructions use Sphinx Design dropdowns. Stale section references
were corrected, and links to unpublished draft pages use the corresponding
published WPILib guides or changelog.

Four additional reference articles (hardware component overview, wiring best
practices, CAN wiring basics, and status lights) and 54 supporting images
were imported from wpilibsuite/wpilib-docs at ab6a3e4c5fa84eeeee2f89ee028c3f6de8da4067.
Original document paths and image credits are preserved. References to
software documentation and glossary terms remain linked to WPILib. A scope
note identifies the roboRIO/PCM/PDP examples in the CAN guide.
