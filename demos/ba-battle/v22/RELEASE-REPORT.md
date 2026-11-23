# Ba' Battle V22 — Map-First Arcade Tester
Date: 23 November 2026 · Verdict: **PARTIAL — playable browser tester, not production ready**

## Source & rollback
- Repository: `Simey407/hay-digital-solutions`
- Branch: `ba-battle-web-tester-20261123`
- File: `demos/ba-battle/v22/index.html`
- Commit: [5b7f29ab6e660b028aa522636cc9e12825ff068a](https://github.com/Simey407/hay-digital-solutions/commit/5b7f29ab6e660b028aa522636cc9e12825ff068a)
- [Play V22](https://raw.githack.com/Simey407/hay-digital-solutions/ba-battle-web-tester-20261123/demos/ba-battle/v22/index.html)
- V21 and the standalone Map Lab remain intact for comparison and rollback.

## Implemented
1. Integrated the user-approved smooth-road rendering approach from `demos/ba-battle/map-lab/index.html`: original OpenStreetMap road polylines painted in two global passes (continuous kerbs, then surfaces), with flat OSM building footprints and mapped water.
2. Removed bright route-tracing overlays, speculative junction route highlights, and invented end-goal scenery from the authentic-map view.
3. Reduced overhead character size and increased the map's visible world area; existing dynamic spectators remain attached to the scrum.
4. Made Push and Hold permanently visible and moved optional boost inventory, shop access and advanced tactics into an on-demand drawer. The opposition counter button appears conditionally.
5. Kept the existing team selection, throw-up, AI opposition, scoring, local coin boosts, Chaos Challenge and smuggling code, except for layout/map integration.
6. Added a map-readiness gate: game cannot start with the fictional fallback street illustration; it requires genuine OpenStreetMap geometry to load first.
7. Preserved V21 as-is; only created V22 on the isolated test branch. No billing or production changes.

## Verification
- **PASS** — GitHub created the source commit; reading back the new file returned exactly the submitted content.
- **PASS** — JavaScript source compiled with V8 `new Function`; no syntax errors detected.
- **PASS** — Independent hosted browser opened the V22 preview, read `OSM STREET LINES · CONNECTED` and `OSM: 91 connected route segments · online` (1824 mapped graph nodes).
- **PASS** — Uppies default team selection and start -> power -> accuracy -> Ba' throw-up -> running clock.
- **PASS** — Push responded, Hold button accepted interaction, compact controls were visible without scrolling in the automated browser inspection.
- **PASS** — Tactics & Boosts panel opened and closed, revealing the existing shop/boost/tactics controls while Push and Hold stayed accessible.
- **OBSERVED** — Browser reported smooth flat OSM roads/buildings and no on-screen JavaScript errors. This was not a pixel-by-pixel geographic audit or iPhone native performance test.
- Browser trace: https://agent.tinyfish.ai/runs/0c87ca0c-90d9-4606-a03f-a52dc83ef25f

## Unverified and risks
- Both complete goals, exact Mackinson's Corner wall placement and permissible Doonies salt-water boundary have **not** been field-validated or end-to-end retested for V22.
- The standard browser smoke test selected Uppies only. Doonies full gameplay, smuggling, Chaos Challenge, leaderboard persistence, boost consumption and replay are inherited code but were **not** retested here.
- A click on Hold was observed; a sustained press and its effect on surge resistance were not objectively measured.
- The map uses real coordinates for streets and buildings but lacks a surveyed validation of street widths, tiny closes, goal coordinates and all route endpoints. Avoid describing the complete game's geography as exactly verified.
- The current frontend requests live OSM/Overpass data on cache miss. A production release needs a licensed, pre-packaged map snapshot with appropriate attribution and reliable hosting; do not assume public APIs are suitable for many users.
- Real iPhone layout, frame rate, touch feel and prolonged play remain user/device acceptance checks.
- No real-money purchasing and no public global leaderboard are present.

## Next review gate
Owner to open V22 on iPhone and assess the **overhead viewpoint, actual Kirkwall street appearance, moving scrum, smaller Ba', controls**. Then prioritize exact goal coordinates, full-match gameplay tests on both teams, and mobile performance before new features.

**No spending authorized or incurred by this GitHub work; no production branch was changed.**
