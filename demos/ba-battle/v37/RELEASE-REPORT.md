# Ba’ Battle V37 · round actions and a smaller Perfect bonus

- [Play V37](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Simey407/hay-digital-solutions/8b0eb5d036bd7f238f0364f3f96fcaf79b5a38af/demos/ba-battle/v37/index.html)
- Playable commit `8b0eb5d036bd7f238f0364f3f96fcaf79b5a38af` on `ba-battle-v37-testing`. V36 is available for rollback.

## Changes

- Available side actions now pop up as 48 × 48 px circles. Symbols remain in the centre, with captions underneath and stock counts on the relevant boosts. A ready button still pulses unless Reduce Motion is enabled.
- Kept the existing timing requirements. Reduced the force, duration and stamina reward for Perfect and substantially lowered the Perfect-streak acceleration and speed ceilings. The maximum forward speed on Standard with a streak is 11.7 m/s instead of 16.5 m/s. V37 starts a separate personal-best time for the new balance.
- The Kirkwall map data is byte-identical to V36. Push and Hold, direct pitch actions and the match-poster styling carry over.

## Verification

- In matched Chromium simulations, five Good pushes advanced about 68 m in both builds. Five Perfect pushes advanced about 91 m in V36 and 75 m in V37 over the same scripted interval.
- The published build passed in Chromium and WebKit at 360, 390 and 430 px. Verified the circular hit targets and captions, direct activation of a boost and counter, and no unexpected scrolling or page errors.
- A Standard Uppies match reached the wall with 48 clean drives in about 100 seconds of accelerated match time. The result and Rematch worked.

Physical iPhone balance and thumb-reach checks remain open. £0 spent.
