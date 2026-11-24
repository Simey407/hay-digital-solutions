# Ba’ Battle V24 test release

- [Play V24](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Simey407/hay-digital-solutions/de6d835cdfa01006cbd01d9c97665e25b6512b0b/demos/ba-battle/v24/index.html)
- [Playable build `de6d835cdfa01006cbd01d9c97665e25b6512b0b`](https://github.com/Simey407/hay-digital-solutions/commit/de6d835cdfa01006cbd01d9c97665e25b6512b0b) on `ba-battle-v24-testing`. V23 remains the rollback branch.

## Research and implementation

- Local match reporting describes the pack grinding to a standstill, slipping into lanes, then breaking back onto different streets. That sequence informed the locked, moving and surging states, and the decision to keep real street turns and open-lane smuggling. [The Orcadian’s 2019 match report](https://orcadian.co.uk/uppie-break-proves-critical-in-mens-new-years-day-ba-game/) and [Orkney’s description of the Ba’](https://www.orkney.com/events/new-years-day-ba).
- Instrumented rugby scrum research distinguishes the initial impact from sustained compression. V24 borrows that distinction for arcade play: a held Push builds pack force over a short interval, a locked pack has a higher threshold to start moving, and a force imbalance accelerates the pack against damping. Under pressure the actors close ranks, with tighter streets increasing resistance. The numerical values are game tuning. [Preatoni et al., 2015](https://pubmed.ncbi.nlm.nih.gov/24511085/)
- The standard input is a short Push hold followed by release to recover. Taps are still accepted. Long pushes cost stamina faster. Hold brakes an opposing drive, and bracing a surge long enough creates a 2.8-second counter-push window on release.
- The Action camera starts at 1.55 CSS pixels per metre, about three times V23’s Town scale. It follows the Ba’ continuously and looks ahead along the connected route in its current direction of travel, including carrier routes. Town and District views remain available. All views stay overhead and north-up.
- The OSM map, throw-up and mapped goal positions carry over from V23. Street turns, smuggling, both teams, local results and the optional boost inventory remain available. [V23 geographic evidence](https://github.com/Simey407/hay-digital-solutions/blob/ba-battle-v23-testing/demos/ba-battle/v23/RELEASE-REPORT.md)

## Verification

- A Chromium touch test held Push, observed continuous advance and camera travel, measured stamina drain and recovery, and opened the counter window by holding through a surge. The zoom control cycled through all three scales.
- Both teams reached their goals using accelerated browser input. A connected turn produced an audited route, and the tested smuggle interception returned the carrier to the scrum. An idle Uppies match allowed the opposition to reach the Basin after three rival turns.
- A Standard Uppies run driven by short Push holds, recovery and defensive Holds reached the wall in 4:46 of accelerated match time with 49 Push presses and 12 blocked rival runs. This recorded a completed match with intermittent input. Faster tapping can still win more quickly.
- The pinned preview ran in Chromium and WebKit at 360, 390 and 430 px. Push and Hold stayed interactive with the inventory open, gameplay fit the viewport, and the bundled map kept working after the network was disabled. These were desktop browser tests at simulated phone dimensions.

## Open checks

- A physical iPhone playtest is still needed for comfort, pacing and real-device performance. The arcade model uses rugby research as an analogy and has no measured Kirkwall Ba’ force data.
- The V23 geographic limits still apply. V24 models one Basin finish, and the final wall and slipway contact points have been cross-checked remotely.
- £0 spent. The isolated preview uses the same free GitHub and HTML Preview path as V23.
