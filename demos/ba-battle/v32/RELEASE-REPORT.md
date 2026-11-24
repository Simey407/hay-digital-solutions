# Ba’ Battle V32 · on-screen actions

- [Play V32](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Simey407/hay-digital-solutions/2c9283b91748a5851ce6e804412207043ff5e208/demos/ba-battle/v32/index.html)
- Playable commit `2c9283b91748a5851ce6e804412207043ff5e208` on `ba-battle-v32-testing`. V31 remains available for rollback.

## Changes

- Boosts and tactics pop onto the appropriate pitch edge as soon as they become usable. One tap plays the action. Spent and unavailable actions clear the pitch. The brief entrance animation is followed by the ready pulse, with a faster pulse for urgent counters and static controls with Reduce Motion.
- Removed the shared tab strip from Boost Inventory, Match History and the Local Leaderboard. Each opens directly from the home screen with a Back button. Rematch and the goal replay sit on the result screen.
- The Kirkwall map, overhead follow camera and Push and Hold dock carry forward.

## Verification

- Published Chromium and WebKit checks passed at 360, 390 and 430 px. Each menu action opened the intended screen directly. On the pitch, the counter and boost appeared without taking over the map, accepted a single tap and cleared after use. Push and Hold remained reachable. No page errors or unexpected scrolling appeared.
- Completed an Uppies match, paused and resumed the goal replay, returned to the result and replayed it through automatic completion. Score, coins and match history count stayed stable. The history survived reload and Rematch worked.

Physical iPhone testing of V32 remains open. £0 spent.
