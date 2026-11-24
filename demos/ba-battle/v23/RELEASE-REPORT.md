# Ba’ Battle V23 release report

24 November 2026 · Isolated tester for CEO review

- Playable build commit [`f46b47333fe32005fdccf71c6335979ff01c9021`](https://github.com/Simey407/hay-digital-solutions/commit/f46b47333fe32005fdccf71c6335979ff01c9021)
- [Play V23](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Simey407/hay-digital-solutions/f46b47333fe32005fdccf71c6335979ff01c9021/demos/ba-battle/v23/index.html)
- Branch `ba-battle-v23-testing`, based on testing commit `8009489eabd3f9d8492da986f9f61a7a5b782364`. V22 remains available on its existing branch for rollback.

## Bird’s-eye camera update

- Town View now starts at the approved Map Lab’s 0.52 CSS pixels per metre. District and Street scales are available from the map-scale button. Every view uses the same north-up overhead projection.
- A resize observer keeps the canvas drawing buffer aligned to the map’s CSS dimensions when the dock appears. This removes vertical stretching during the change from menu to match.
- Flat building fills and small top-down figures replace directionally shaded artwork. The ball stays on the ground projection during the throw and is highlighted with a ring. The compass and 50 m scale give a visual reference.
- The larger overview uses the same OSM extract at its full bounds, so more of the town and harbour stay visible as the camera moves. The updated extract includes 1,014 highway ways, 3,124 building-tagged ways, five inland-water ways and the extended coastline. The graph has 4,195 nodes and 4,482 edges with 25 crossing segments flagged. The original 80-segment baseline, mapped starts and finishes are preserved.
- Checked screenshots and all three scale presets at 360, 390 and 430 px. The connected turn and intercepted smuggle passed again. Both teams completed matches again under accelerated browser input. The published link passed the layout and input checks in Chromium and WebKit at all three widths, with no page errors.

The implementation notes below describe the original V23 build before this camera update.

## Implemented and fixed

- Adapted the Map Lab’s north-up, two-pass street rendering. The shared road surface removes colour seams at OSM way boundaries, and mapped building footprints sit above roads. The cathedral and the three Ba’ landmarks are labelled. Streets, closes and harbour water use the packaged map.
- Built routing from shared OpenStreetMap node IDs. The snapshot flags 13 segments that intersect mapped building interiors or salt water. The default route has 80 connected segments. Player and spectator offsets are constrained by the road corridor, mapped buildings and harbour water.
- Put the throw-up at the Mercat Cross and its landing on the Broad Street approach. Added separate ball finishes from the road to the mapped wall point and from the dry slipway into the Basin. Only those finishes trigger results.
- Tightened the 16-a-side scrum, added small winter-clothed overhead figures and animated a compact spectator crowd. Camera smoothing is time-based. Opponent breakaways now apply pressure over time. Turns change routes at the shared junction and preserve the Ba’s position even when the distance from the Cross changes. A smuggle uses connected waypoints and moves the trailing scrum toward the eventual rejoin.
- Put Push and Hold in a fixed dock, with stamina and momentum feedback. Steady taps build rhythm and rapid tapping uses more stamina. Hold brakes the scrum and can stop a rival breakaway. Direction buttons appear for available alternatives at an upcoming junction. Tactics, boost inventory and manual counters open above the dock.
- Retained both teams, difficulty settings, throw timing, opposition orders, local inventory, scoring, smuggling and the local leaderboard. Replay restores the baseline route. Fixed an HTML Preview error by storing the packaged data in an inert HTML template.

## Geographic evidence

| Feature | Evidence and implementation |
| --- | --- |
| Mercat Cross and St Magnus Cathedral | The local event listing and match coverage put the throw at the Cross in front of the cathedral on Broad Street. The throw starts at OSM node [5634885266](https://www.openstreetmap.org/node/5634885266) (58.9816029, −2.9603507). The Broad Street landing reference is a projection approximately 11 m west-northwest of the Cross. The cathedral uses OSM footprint [75038322](https://www.openstreetmap.org/way/75038322). |
| Uppies | Match coverage records the winning touch at Mackinson’s Corner. OSM names node [11494911078](https://www.openstreetmap.org/node/11494911078) (58.9779919, −2.9632897) on the wall of building [860470617](https://www.openstreetmap.org/way/860470617). The approach runs via Victoria Street, Union Street, Main Street and the short New Scapa Road segment to node [5827979905](https://www.openstreetmap.org/node/5827979905). The final 7.4 m to the wall was checked against mapped building interiors. |
| Doonies | Match coverage records a goal in the water of Kirkwall Basin. The dry approach follows mapped service way [205116431](https://www.openstreetmap.org/way/205116431). The selected water point is slipway node [2150870661](https://www.openstreetmap.org/node/2150870661) (58.9849879, −2.9597523), checked inside the polygon derived from mapped coastline [1150759973](https://www.openstreetmap.org/way/1150759973). This is one playable finish in the Basin. |
| Roads and closes | Baseline routes include Broad, Albert, Bridge, Harbour, Victoria and Main Streets. The extract retains separately mapped closes and lanes such as St Magnus Lane, Gas Wynd, Mounthoolie Lane and Bridge Street Wynd, with their shared-node connectivity where mapped. |

Sources include the [Orkney event listing](https://www.orkney.com/events/new-years-day-ba), [Orkney Museums’ cathedral entry](https://orkneymuseums.co.uk/our-museums/st-magnus-cathedral/), [The Orcadian’s wall finish and Mercat Cross throw-up coverage](https://orcadian.co.uk/uppie-break-proves-critical-in-mens-new-years-day-ba-game/) and [The Orcadian’s report of a Basin finish](https://orcadian.co.uk/christmas-day-win-for-doonie-boys-2/).

The 24 November 2026 [OpenStreetMap API extract](https://api.openstreetmap.org/api/0.6/map?bbox=-2.973,58.973,-2.950,58.991) was reduced to a central Kirkwall snapshot of 527 highway ways, 1,617 building-tagged ways and five inland-water ways, plus clipped coastline polygons. The playable graph has 1,964 nodes and 2,089 edges. The derived data is bundled under [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/) with [OpenStreetMap attribution](https://www.openstreetmap.org/copyright) and an in-game **Map data** download of the unpacked snapshot.

## Browser quality assurance

- **Pass — both teams and both finishes.** Playwright used real button taps for team selection, the two-stage throw-up and initial Push input. The running browser then used accelerated simulation with repeated Push inputs through the complete routes. Uppies and Doonies each won on Standard in about 65 seconds of match time. Results, leaderboard access and replay worked. The idle Uppies test ended with a Doonie win after three rival turns.
- **Pass — directional choice and scrum.** Tapped Straight and then Left at a connected junction. The turn produced a valid 93-segment route. The largest sampled movement was 1.56 m in a 0.2 s step across that test. The browser recorded 32 active bodies in regular play, collision contacts during the turn test and zero blocked actor centres in the sampled positions.
- **Pass — Push, Hold and stamina.** Six touches produced six Push actions. A sustained Hold consumed about nine stamina in 0.9 seconds. A separate touch test measured 11.10 m of retreat over two seconds unbraced versus 0.39 m braced. Releasing the touch ended Hold.
- **Pass — smuggling and boosts.** The squad, flank and Smuggle buttons started the carrier run. Controlled random draws selected the interception and clean-rejoin cases. The carrier returned continuously on interception and earned 200 points on a successful rejoin. A saved shout boost was consumed.
- **Pass — offline map and mobile layout.** Loaded the single HTML file with networking disabled at 360 × 640, 390 × 844 and 430 × 932. Started a match and exercised the action dock and optional panels. Gameplay had no page scrolling at these sizes. One desktop Chromium capture measured 16.7 ms median and 95th-percentile frame intervals over 180 frames.
- **Pass — published preview.** The pinned HTML Preview link opened directly in Chromium and WebKit at all three sizes. The start and gameplay docks fit the viewport, and hit tests confirmed Push and Hold remained interactive with the tactics drawer and inventory open. Both engines continued to accept Push after the network was disabled. No mapping API requests or page errors were reported.
- **Pass — local persistence.** Completed a match under a named profile, reloaded the page and verified the profile’s win remained on the local leaderboard.

## Open checks and limitations

- Wall placement and the dry-to-wet transition were checked against mapped geometry and local records. On-site confirmation of the wall contact point, tide conditions and alternate legal salt-water approaches remains open. V23 models one Basin finish.
- Road widths are illustrative. The audit covered baseline routes and sampled detours and actor positions. A street-by-street visual survey and continuous collision checks for every spectator, flank participant and AI guard remain open. Some tactical squad handoffs can visibly reposition individual figures.
- Physical iPhone touch response, readability outdoors, performance and repeat-play balance need device testing. The hosted URL needs a first network load. The downloaded standalone file works offline, but the hosted preview is not an installed offline app.
- No expenditure, paid service, payment integration or production deployment. The browser preview uses the public GitHub source and the free HTML Preview service.

**Next improvement** — Run one complete match per side on a physical iPhone in Kirkwall to assess touch rhythm and confirm the visual approaches to the two goals.
