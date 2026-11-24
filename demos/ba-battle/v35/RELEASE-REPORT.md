# Ba’ Battle V35 · tighter timing and home-screen Ba’s

- [Play V35](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Simey407/hay-digital-solutions/cce7715a8123d2c86081f41c640fdd596b2566db/demos/ba-battle/v35/index.html)
- Playable commit `cce7715a8123d2c86081f41c640fdd596b2566db` on `ba-battle-v35-testing`. V34 remains available for rollback.

## Changes

- Standard’s Perfect window is now 100 ms wide, down from 220 ms. The gold band can shift between graded pushes. It stays fixed while the player holds Push. Hard and Veteran have narrower windows. Practice keeps a fixed, more forgiving band. The Good, OK and Poor grades remain.
- Perfect streaks still build speed. V35 starts a fresh personal-best time for its revised timing rules. Existing match history stays available.
- The game’s home screen displays two black-and-brown leather Ba’s beside the title, including at short iPhone viewport heights. The asset is embedded as a transparent WebP in `demos/ba-battle/v35/index.html`. It was generated with the built-in ImageGen tool, then resized and encoded for the browser. The leather and stitching reference was the [NorthLink description of making the Ba’](https://www.northlinkferries.co.uk/orkney-blog/beginners-guide-to-the-ba/).

ImageGen prompt:

> Create one wide transparent-background game home-screen asset showing two hand-stitched Kirkwall Ba’ leather balls, a slightly smaller ball beside the larger one. Historic eight-piece sewn construction, alternating dark tawny brown leather and near-black leather, curved broad panels with subtle visible stitching, subtly worn matte leather; no modern football pentagons. Side by side with a little breathing room, fully in frame, viewed slightly from above, restrained studio light. No text, labels, badges, watermark, background or other objects. The shapes and seams should read at mobile thumbnail scale.

## Verification

- Five repeated holds of exactly 1.05 seconds gave five Perfects in V34 and two Perfects in the sampled V35 run. Five holds aimed at each current gold band gave five Perfects in V35.
- The published build loaded the home artwork, launched the throw-up and accepted a Perfect release in Chromium and WebKit at 360, 390 and 430 px. The gold band shifted after release and no page errors appeared.
- Completed an Uppies match and checked the result, replay, rematch and match history after reload. The bundled Kirkwall map remained byte-identical.

Physical iPhone timing remains open. £0 spent.
