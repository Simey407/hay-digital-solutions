# Ba’ Battle V26 · pitch-side controls

- [Play V26](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Simey407/hay-digital-solutions/4198e90400ab7d4d808616aa6ce7bede322dbce6/demos/ba-battle/v26/index.html)
- Playable commit `4198e90400ab7d4d808616aa6ce7bede322dbce6` on `ba-battle-v26-testing`. V25 remains available for rollback.

## Changes

- Tactics opens against the left edge and Boosts against the right. Availability dots identify usable tools. One panel opens at a time, leaving the central pitch clear. Both tabs move above the directional choices when a junction approaches.
- Boost use and in-game inventory stay on the right edge. Opening the other edge, closing the panel or leaving the match dismisses the in-game inventory. The local leaderboard retains its full results view between matches.
- Simplified the header, dock and inventory copy. Refined spacing, button shapes, focus indicators and safe-area padding. Edge panel animation follows the reduced-motion preference.
- Preserved the V25 map extract byte for byte and retained the north-up follow camera and overhead actor rendering. The camera eases 14 CSS pixels away from an open panel to keep the Ba’ visible. Drive timing, results and the connected routes carry forward.

## Verified

- Tested the published preview in Chromium and WebKit at 360, 390 and 430 px. Verified left and right placement, one panel at a time, in-panel inventory, boost consumption, keyboard dismissal and leaderboard navigation. Push and Hold stayed visible and hit-testable. No unexpected page scrolling or page errors appeared.
- Completed a Standard Uppies match with the Boosts panel open. The browser used timed Push holds and defensive Holds with accelerated game time. The result showed 47 clean drives, and Rematch reopened the pitch.
- Matched the embedded OpenStreetMap snapshot against V25 and inspected the panel placement on the map at phone widths.

Physical iPhone testing remains open. £0 spent. The preview uses the existing isolated GitHub and HTML Preview path.
