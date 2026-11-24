# Ba’ Battle V30 · team calls and the scrum

- [Play V30](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Simey407/hay-digital-solutions/e9be4c56c0070a2b827847ece0829740b4fd36cd/demos/ba-battle/v30/index.html)
- Playable commit `e9be4c56c0070a2b827847ece0829740b4fd36cd` on `ba-battle-v30-testing`. V29 remains available for rollback.

## Changes

- Results name the scoring side as **Uppies Ba’ !!** or **Doonies Ba’ !!**, with the wall or harbour finish below.
- All nine pitch-side actions have distinct symbols with an animated pulse while available. Buttons retain text and large touch targets. Reduce Motion disables the animation.
- The crowd alternates visible Uppie and Doonie chants and sends matching voice lines to the browser when sound is enabled. Tap Ba’ Shouts during your side’s chant to back the pack. Tap during the rival chant and your shout echoes them, giving their pack a short lift. A caption identifies what happened.
- Staggered, inward-facing players form a tighter cluster. Shoulder and arm shapes, contact separation, foreground layering and smaller spectator silhouettes make the scrum easier to pick out.
- The bundled Kirkwall map stayed byte-identical. The camera remains directly overhead.

## Verification

- Chromium and WebKit checked the published build at 360 × 640, 390 × 710 and 430 × 932. Verified symbol display and reduced-motion behavior, visible chants, both shout outcomes and viewport fit.
- A Chromium test recorded the speech requests for both sides and exercised an Uppie boost with the correct call and a Doonie miscall. Physical device voice playback and volume remain open.
- Browser QA completed both goals and verified the exact result headings, results and Rematch. In a fixed Broad Street sample, 32 actors averaged 2.9 m from the Ba’ in V30 versus 3.5 m in V29. Contact resolution was active and no sampled actor centre lay inside a mapped obstacle.
- £0 spent. The isolated testing branch uses the existing GitHub preview workflow.
