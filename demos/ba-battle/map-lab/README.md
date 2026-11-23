# Ba' Battle — Kirkwall Map Lab (23 November 2026)

## Purpose
Map-only north-up orthographic visual test, developed after user feedback that V21's map looked geographically wrong, visually angled and cluttered. **This is not V22 gameplay**, and does not replace V21. Its principal purpose is to approve the visual and geographic foundation before updating the scrum game.

### Source
- `index.html` under this folder
- Exact road centerlines, mapped lanes and building footprints are loaded from the public OpenStreetMap read-only API, with Overpass fallbacks. No synthetic streets or buildings are shown if they fail.
- Coordinates are mapped using latitude/longitude, fixed north-up. The Mercat Cross marker uses approximately 58.98159, -2.96045; St Magnus Cathedral around 58.98144, -2.95961.
- Copyright and attribution displayed in application: © OpenStreetMap contributors, ODbL.
- Layout is visually simplified; colours and road widths are illustrative, **not surveyed widths**.
- Reference maps supplied by the owner were consulted for context, not embedded or redistributed because reuse licensing is unknown.

### Verification
- GitHub preview browser successfully loaded **520 mapped street ways and 1,574 OSM building outlines**; an OSM-derived water shape was visible.
- Remote read-only browser report: https://agent.tinyfish.ai/runs/8ac48ba4-170b-4016-a9db-47c5f703753d
- Flat 2D, north-up map and anchored bottom control dock visible in that browser session.
- JavaScript syntax checked with Node; local Chromium fixture tests passed at 360px, 390px and 430px widths with no page errors or vertical scrolling.
- In local fixture tests, Street View changes zoom to 1.46 and Town View back to 0.52; zoom state was subsequently made explicitly visible in the interface.
- **Fixture data was synthetic only for UI testing, not geographic accuracy.**
- This is a visual-data and interaction smoke test, **not a field survey or full Kirkwall road-by-road audit**.

### Outstanding for acceptance
1. Owner to compare the actual mapped closes, junctions, street names and buildings with their supplied Kirkwall reference maps.
2. Locate Mackinson's Corner wall and permitted Doonie salt-water boundary precisely, then build route/win conditions on verified geometry rather than sample point coordinates.
3. Choose acceptable visual scale and road/body relative sizes before game integration.
4. Once approved, port map layer into V22, retain existing mechanics, and keep essential PUSH and HOLD buttons visible without scroll. Hide advanced controls until contextually needed.
5. Test both complete matches, lane turns, smuggling, mobile performance and iPhone display. Production map delivery should not depend on frequent live requests to public OSM/Overpass endpoints; create a properly licensed self-hosted/prepared snapshot.

**Status: PARTIAL — map geometry is genuinely sourced from OSM; exact goal positions and the full game integration remain open.**