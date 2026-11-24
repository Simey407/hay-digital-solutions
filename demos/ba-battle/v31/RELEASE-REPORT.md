# Ba’ Battle V31 · App Store feature assessment

- [Play V31](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Simey407/hay-digital-solutions/15c6950bdf32bcc84eefd07fbc829732f0dbb53c/demos/ba-battle/v31/index.html)
- Playable commit `15c6950bdf32bcc84eefd07fbc829732f0dbb53c` on `ba-battle-v31-testing`. V30 remains available for rollback.

## Comparison and decisions

- **FC Mobile and eFootball.** FC Mobile documents post-match replay highlights. eFootball documents replay and skip controls. The scoring touch or splash in Ba’ Battle also moves quickly, so V31 adds an optional last-six-seconds replay from the results screen, with Pause, Play and Results controls. [FC Mobile App Store listing](https://apps.apple.com/gb/app/ea-sports-fc-mobile-football/id1094930513) · [eFootball controls](https://www.konami.com/efootball/en/page/mobile_controller)
- **Brawl Stars.** Supercell documents a battle log with recent results and replays. V31 adds a local log of the last eight completed matches with team, difficulty, win or loss, time and clean drives. [Brawl Stars App Store listing](https://apps.apple.com/gb/app/brawl-stars/id1229016807) · [Supercell gameplay reference](https://support.supercell.com/brawl-stars/en/game/index.html)
- **Rocket League Sideswipe.** Psyonix highlights short matches and three core touch buttons. This supported preserving Ba’ Battle’s existing direct play controls and keeping the replay optional with Rematch still prominent. [Rocket League Sideswipe App Store listing](https://apps.apple.com/us/app/rocket-league-sideswipe/id1549027048?platform=ipad)

The comparison used official listings and manuals. V31 uses Ba’ Battle’s own art, map and interface. The V30 map extract stayed byte-identical. Replay snapshots stay in memory for the latest completed match. Match summaries survive reload in the same browser.

## Verified

- Browser QA completed both goal routes under timed-drive input. The wall replay passed pause, resume, return to results and automatic completion. The Basin replay reached the exact recorded finish point.
- Points, coins, duration and history count stayed the same after repeated playback. The match log survived reload. Rematch and the leaderboard remained accessible.
- The published build passed menu, match-history navigation, gameplay controls and viewport checks in Chromium and WebKit at 360, 390 and 430 px, with no page errors.

Physical iPhone playback and performance remain open. £0 spent.
