# Ba’ Battle V39 · mobile release foundation

- [Play the V39 browser preview](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Simey407/hay-digital-solutions/af8f9da7b1f29af5d6846fb9eb1ca3cc6ca2608a/demos/ba-battle/v39/index.html)
- Playable commit `af8f9da7b1f29af5d6846fb9eb1ca3cc6ca2608a` on `ba-battle-v39-testing`. V38 is available for rollback.

## First release milestone

- Added a Pause button during play. The match, stamina, crowd, camera and replay capture stop until Resume. A background or page-hide event pauses the match, clears held input and asks the player to resume on return. The pause screen also gives a deliberate way to end the current match. An in-flight replay pauses on background.
- Packaged a standalone web app with a portrait manifest, two Ba’ icons and a scoped service worker. All map and game data are bundled. After the first load at a direct origin, the cache can supply a fresh launch without reaching the server. The worker only handles the V39 launch page and known app files.
- The map, timing rules, shout mechanics, side actions and result flow carry forward from V38.

## Verified

- Published preview passed Pause, Resume, and End Match at 360, 390 and 430 px in Chromium and WebKit. Tests observed frozen match time, position, stamina and replay frame count. A simulated visibility change invoked the background pause path.
- Chromium’s regular-profile installability check returned no errors on localhost. Chromium and WebKit each reloaded from the service worker and started a match after the local origin was physically stopped.
- A complete Uppies browser match survived a manual pause and resume. The wall replay, result rewards, rematch and history after reload were checked.

## Delivery boundary and next gate

The public link uses HTML Preview, whose wrapper origin is not the app origin. That link supports browser play and pause. Home Screen installation and offline startup require the direct package served on a secure, app-controlled address. A second raw GitHub preview host stopped at its warning interstitial during testing, so it is not a verified installation link. The app bundle is the V39 folder with its manifest, worker and icons. No production hosting was changed and £0 was spent.

The next release gate is one stable HTTPS test address and a physical iPhone round trip through Home Screen launch, airplane-mode restart, app switching and a full match. Current pause state lives in the running session. Closing or reloading starts a new session while completed results persist. [Apple’s Home Screen web app instructions](https://support.apple.com/en-az/guide/iphone/iphea86e5236/26/ios/26) · [Service worker secure contexts](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)
