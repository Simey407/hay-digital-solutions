# Ba’ Battle V29 · final stretch and moving crowd

- [Play V29](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Simey407/hay-digital-solutions/99b117d3c3b244852b6cb65ba104ef760223de81/demos/ba-battle/v29/index.html)
- Playable commit `99b117d3c3b244852b6cb65ba104ef760223de81` on `ba-battle-v29-testing`. V28 remains available for rollback.

## Changes

- On entering the final 20% of either goal route, the game moves into a tighter overhead view and names the wall or Basin. The zoom buttons remain live. A manual zoom-out stays in place for the rest of the approach. Retreating outside the final 28% re-arms the automatic zoom for the next approach.
- 64 spectators follow the moving scrum along its street route. Most trail at different distances and speeds. Others gather ahead or at the sides. Their positions are clipped against mapped buildings and water. During a smuggle, the main crowd follows the pack on its approach route.
- Ready side actions pulse in place. Urgent counters pulse faster. Quick Push taps build a combo, spend stamina and trigger a stronger ring, sparks and short sound accents. Gold-release drives still work. Reduce Motion removes the side pulses, spectator cheering animation and tap sparks, and changes zoom without the easing transition.
- The V28 embedded Kirkwall map stayed byte-identical. Throw Up, the direct boost and tactic buttons and the moving north-up view carry forward.

## Verification

- Chromium and WebKit at 360, 390 and 430 px exercised the final-stretch threshold on both routes, the manual zoom-out override and re-arming after retreat. These threshold tests positioned the Ba’ with the QA harness.
- The published preview in both engines accepted eight quick taps, played a boost, displayed or suppressed the pulse according to motion preference, and stayed within the viewport without page errors. Paired local checks measured spectator movement and sampled all 64 positions outside mapped obstacles.
- Standard timed-drive matches reached both mapped goals under accelerated browser input, with 47 clean drives for Uppies and 48 for Doonies. Results and Rematch worked.

Real iPhone testing of crowd legibility and performance at close zoom remains open. £0 spent.
