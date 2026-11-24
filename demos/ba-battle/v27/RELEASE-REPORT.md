# Ba’ Battle V27 · direct pitch-side actions

- [Play V27](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Simey407/hay-digital-solutions/40c1400bf3c4490edcbf6b226c8aa0cb124110f6/demos/ba-battle/v27/index.html)
- Playable commit `40c1400bf3c4490edcbf6b226c8aa0cb124110f6` on `ba-battle-v27-testing`. V26 remains available for rollback.

## Changes

- Ready tactics appear on the left and usable boosts and recovery actions appear on the right. Buttons are directly playable, with 44 px or taller touch targets. Spent and unavailable actions clear from the edges.
- Time-sensitive counters get a larger gold button. At a connected lane, Flank Left or Flank Right sends a squad with one tap. Smuggle appears when the squad is in position.
- The side actions sit above direction choices. Push and Hold remain docked. Inventory is accessible from the menu and leaderboard between matches.
- The embedded Kirkwall map is byte-identical to V26. The moving north-up camera, mapped geometry, overhead figures and drive timing carry over.

## Verification

- The published build passed in Chromium and WebKit at 360 × 640, 390 × 710 and 430 × 932. Direct taps sealed a rival lane and used Ba’ Shouts. Used actions cleared. Push and Hold remained visible and interactive alongside the side actions, with no unexpected scrolling or page errors.
- A local browser test sent a flank directly from the pitch and started a smuggle when the button appeared.
- A Standard Uppies match reached Mackinson’s Corner with 48 clean drives and no short taps under accelerated browser input. The result and Rematch worked.

Physical iPhone testing of V27 remains open. £0 spent.
