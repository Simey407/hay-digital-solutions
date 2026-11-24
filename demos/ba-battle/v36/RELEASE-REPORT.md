# Ba’ Battle V36 · match-poster overhaul

- [Play V36](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Simey407/hay-digital-solutions/c7d9390f55992c13b3a0fbf196f3fc7880806a21/demos/ba-battle/v36/index.html)
- Playable commit `c7d9390f55992c13b3a0fbf196f3fc7880806a21` on `ba-battle-v36-testing`. V35 remains available for rollback.

## Design and research

- Reworked the home screen, scoreboard, action dock, pitch controls and results into a matching sports-poster style. The home-screen Ba’s sit in a lit title panel. Uppies and Doonies have warm clay and harbour-blue accents, with distinct goal posters at the wall and Basin.
- Refined the overhead palette for separation between paving, roofs and water. The OpenStreetMap snapshot is byte-identical to V35. The connected streets, mapped goals, follow camera and timing rules carry forward.
- Added an opening throw trail, graded push bursts with a stronger Perfect effect, a wall impact and water ripples. The effects are brief and tied to a specific event. Reduce Motion removes the animated trail, rays and goal poster entrance while retaining the grade and scoring information.
- Kao et al. linked readable graded outcomes to competence and curiosity, and found that adding more visual amplification by itself could hurt engagement in their test. The game-feel survey and Apple’s motion guidance informed the short, localized effects. [Kao et al.](https://people.csail.mit.edu/dkao/pdf/3613904.3642656.pdf) · [Designing Game Feel](https://researcher.itu.dk/p/en/research-outputs/designing-game-feel-a-survey) · [Apple Motion](https://developer.apple.com/design/human-interface-guidelines/motion)

## Verification

- The published build loaded the new home styling and art, completed the throw-up and displayed Perfect feedback in Chromium and WebKit at 360, 390 and 430 px without page scrolling or errors.
- Uppies and Doonies reached their mapped finishes with accelerated browser input. Both team result posters and Rematch were exercised.
- In a desktop Chromium sample of 180 close-view frames, V35 and V36 both measured 16.7 ms median and 16.8 ms at the 95th percentile. This is a desktop comparison, with physical iPhone frame rate and visual appeal still open.

£0 spent. No production deployment.
