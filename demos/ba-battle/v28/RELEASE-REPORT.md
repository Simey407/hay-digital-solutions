# Ba’ Battle V28 · throw-up and close zoom

- [Play V28](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Simey407/hay-digital-solutions/c717d7dba80e00fe1e7dc32e5d0ab22399fa0f7d/demos/ba-battle/v28/index.html)
- Playable commit `c717d7dba80e00fe1e7dc32e5d0ab22399fa0f7d` on `ba-battle-v28-testing`. V27 remains available for rollback.

## Changes

- **Throw Up** starts the match from Mercat Cross. A quick tap tosses the Ba’ into the central scrum. Holding the button fills a power indicator and releasing sets a longer landing along the connected street toward the chosen side. Rematch still starts in one tap.
- Dedicated **+** and **−** buttons adjust the moving overhead camera during the throw or live play. The new close scale is 2.60 CSS pixels per metre, compared with the 1.55 default. District and Town views remain available through **−**.
- Preserved the V27 map data, north-up view, Push and Hold dock, and contextual pitch-side actions.

## Verified

- Chromium and WebKit opened the published build at 360 × 640, 390 × 710 and 430 × 932. Quick taps launched once, sustained presses waited for release, and long throws landed about nine metres toward the selected team. Zoom worked during the throw and in play, and the phone-width dock stayed interactive without page scrolling or page errors.
- Chromium also passed the hold-and-release test with emulated touch events.
- A Standard Uppies match completed at close zoom with 47 clean drives under accelerated browser input. Results and Rematch worked.

Physical iPhone testing of V28 remains open. £0 spent.
