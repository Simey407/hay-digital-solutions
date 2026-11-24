# Ba’ Battle V41 · Scrum and match cutaways

- Isolated branch `ba-battle-v41-testing`
- Playable build `8fc3f0a2988f100590e939045c02eddaa3b320f0`
- [iPhone guest preview](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Simey407/hay-digital-solutions/8fc3f0a2988f100590e939045c02eddaa3b320f0/demos/ba-battle/v41/index.html)
- [Overhaul brief](OVERHAUL-BRIEF.md)

## Changes

- Replaced fixed scrum positions with counter-rotating shoulder loops. Players travel toward the Ba’ and peel back along the outside. The formation compresses with pressure and still uses spacing, road-width limits and the existing building-footprint checks.
- Moved the default north-up camera one zoom step closer. Tuned the relative size of players and the Ba’ selection ring after inspecting browser screenshots. Manual zoom and the final-stretch camera remain available.
- Added three short illustrated cutaways. The stitched Ba’ is tossed at Mercat Cross, touches stone at Mackinson’s Corner or lands in the harbour with spray and ripples. The throw-up runs on rematch. The goal cutaways use the existing goal transition and lead to the existing result and replay. Reduced-motion mode uses static contact poses.
- Carried the V40 account tester forward. Only the guest game is available through the static preview.

## Verification

- Actual Chromium and WebKit at 360, 390 and 430 CSS px. Checked throw-up into live play, player circulation between samples, wall and harbour cutaways from staged route endpoints, result headings and rematch. Included a reduced-motion run in each engine. Inspected screenshots of live play and cutaways.
- Chromium completed a full Uppies match using accelerated QA time and touch input. Verified replay pause, resume and return to results, rematch, and persisted match history. The pinned guest preview also passed the Doonies throw-up and live play transition in mobile-emulated Chromium.
- The gameplay map, goal coordinates and OSM attribution were carried forward from V40. Cutaway illustrations are stylised, and the coordinates were not independently rechecked for this pass.

## Remaining

Physical iPhone Safari checks and an uninterrupted Doonies run remain outstanding. The connected account tester still needs a direct HTTPS address for remote use. No spend or production change.
