# Ba' Battle V21 — Release & Verification Report
Date: 2026-11-23 (UTC)
Status: **PARTIAL — development tester, not production-ready**

## Repository
- Repo: `Simey407/hay-digital-solutions`
- Branch: `ba-battle-web-tester-20261123`
- Previous version: `demos/ba-battle/v20/index.html` (preserved)
- Candidate: `demos/ba-battle/v21/index.html`
- V21 source commit: `ce99f0565fe429e04e5b2955626b36e0598ab3c0`
- V21 source blob: `24682abf6508d2b533657d479e70ae6e4d9cb10b`
- Play: https://raw.githack.com/Simey407/hay-digital-solutions/ba-battle-web-tester-20261123/demos/ba-battle/v21/index.html

## Changes implemented
1. Retained V20 mobile menus, Push/Hold controls, boosting, smuggling, AI and local progress.
2. On successful OpenStreetMap loading, renders actual OSM building outlines rather than procedurally generated houses. Retains visibly labeled approximate fallback when real data is unavailable.
3. Extends the OSM import/cache paths to include building footprints and mapped water polygons when those data exist.
4. Enlarged and tightened the moving spectator crowd around the scrum.
5. Reduced the Ba' size during normal play.
6. Corrected the next-junction selection ordering.
7. Bumped the OSM cache key and displayed debug version to V21.

## Evidence and test outcomes
- **PASS — GitHub publication:** create-file operation returned commit `ce99f...`; fetching V21 afterward returned byte-for-byte identical source to the submitted HTML.
- **PASS — JavaScript syntax:** compiled the extracted inline script via V8 `new Function` with no syntax errors.
- **PASS — browser smoke:** independent hosted browser successfully opened the RawGitHack preview and saw V21, team selection, start flow, throw-up power/accuracy, active clock/location, and Push response.
- **PASS — online OSM route loading in the hosted browser:** status showed `OSM STREET LINES · CONNECTED` and `OSM: 91 connected route segments · online`. This establishes loading as observed by the app, but is not an independent geospatial coordinate-by-coordinate validation.
- **PARTIAL — Hold:** button rendered and accepted a click; sustained pointer hold and bracing benefit were not measured.
- **NOT TESTED — Doonies complete match, Uppies complete match, both goal triggers, post-goal replay, real lane-change movement, smuggle interception and chaos results, iPhone responsiveness/FPS.**
- **NOT TESTED — real OSM building footprints as seen in the actual frame:** geometry parsing and drawing were syntax-checked but not independently inspected on a screenshot.
- **NOT TESTED — offline cache/fallback reconnect after a live successful load.**

Hosted browser evidence: https://agent.tinyfish.ai/runs/a97cb122-2140-4fa2-8bf2-fad791437bfd (completed; 17 steps)

## Geographic references
- Orkney Museums: https://orkneymuseums.co.uk/75th-anniversary-womens-ba/
- Historic game details: https://www.footballheritage.co.uk/an-orkney-football-saga
- Mercat Cross field photography/coordinates: https://www.geograph.org.uk/photo/7620608
- OSM data and attribution: https://www.openstreetmap.org/copyright

Important limits: The game uses OSM geometry where available, but the stored `HOME`, `S_GOAL` and `N_GOAL` coordinate hints have not been independently verified to precision sufficient for exact wall/water trigger placement. Its single harbour goal is an arcade simplification; traditionally the Doonies can win by reaching salt water anywhere in the accepted harbour area. Public OSM API/Overpass endpoints and public OSM tile servers are not suitable as an unreviewed production dependency at scale. Build a properly licensed, prepackaged/stored geospatial snapshot and confirm the coordinates on site before declaring full map accuracy.

## Commercial and operational status
- No purchases or paid subscriptions implemented. Existing coin economy is local device-only and there is no public competitive leaderboard.
- No production branch or public website was changed.
- No payment authorization or external spending was requested.

## Next acceptance gate
1. Validate the street scene against the user's Kirkwall reference maps, including the smaller closes/lanes.
2. Verify exact Mackinson's Corner wall and reachable inner-harbour water goal geometry against geographic evidence and correct the endpoint conditions.
3. Run independent browser tests for both complete goal outcomes, Hold long press, routing, smuggling, mobile layout, replay and saved progress.
4. Obtain actual iPhone review.
5. Only then label V21 release candidate rather than PARTIAL.

Executive verdict: **PARTIAL.** The actual V21 exists and runs in a hosted browser with live OSM street loading, but the geographically exact endpoints and complete mobile gameplay have not been verified.