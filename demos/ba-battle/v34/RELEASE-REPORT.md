# Ba’ Battle V34 · Push timing spectrum

- [Play V34](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Simey407/hay-digital-solutions/046644e5083a2c991203a5d4afe880785f9ef433/demos/ba-battle/v34/index.html)
- Playable commit `046644e5083a2c991203a5d4afe880785f9ef433` on `ba-battle-v34-testing`. V33 remains available for rollback.

## Changes

- Hold Push to move the marker across a timing spectrum. Release in the narrow gold band for Perfect, or around it for Good, OK or Poor. The grade appears beside stamina, with distinct sound accents.
- Perfect releases give the biggest drive, a stamina refund and more rally charge. Consecutive Perfect releases increase forward force and speed, capped after the fifth for movement. A missed release, quick tap or gap over 3.1 seconds resets the streak. Results show the best Perfect streak.
- Quick taps still push. The map data, team goals, follow camera, direct side actions and replay carry forward.

## Verified

- Controlled browser tests exercised all four grades and verified that a non-Perfect release resets the current streak while preserving the best streak. Five Perfect releases advanced approximately 108 m versus 62 m for five Good releases over the same scripted interval.
- The published build accepted Perfect releases and displayed the spectrum in Chromium and WebKit at 360, 390 and 430 px. Chromium used emulated touch. WebKit used held pointer input. No page scrolling or errors were reported.
- An Uppies QA match reached the wall in about 51 seconds of simulated match time. Goal replay and history persistence passed again.

Physical iPhone timing feel remains open. £0 spent.
