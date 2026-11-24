# Ba’ Battle V38 · safe pushes and risky gold

- [Play V38](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Simey407/hay-digital-solutions/4cc4bcdbf70ab543162def8fd83b1fe16dfeca45/demos/ba-battle/v38/index.html)
- Playable commit `4cc4bcdbf70ab543162def8fd83b1fe16dfeca45` on `ba-battle-v38-testing`. V37 is available for rollback.

## Changes

- Standard, Hard and Veteran add red risk bands beside the moving gold target. A near miss in red grades as Poor and costs four extra stamina. It also cuts existing forward momentum. Green releases still grade as Good, giving a safe way to push. Practice keeps its forgiving timing.
- Raised opposition pressure above Practice and reduced sustained hold force. The embedded Kirkwall map is unchanged.
- Crowd chants, Rally charge and the Ba’ Shouts button sit together beside the timing bar. The Shouts action still follows the chant.
- A Perfect release brings one ready bonus or tactic into a gold, tappable spot next to the bar. The original side action remains available. Both use the same game handler and a used or expired offer clears. When no eligible action is ready, the dock highlights Shouts if usable and shows the rally gain.

## Verification

- Chromium graded a deliberate near miss as Poor and five safe green inputs as Good. The same opening sequence advanced about 55 m in V38 compared with about 73 m in V37.
- A Perfect surfaced Rally beside the meter. One tap activated Rally and cleared both the offer and the ready side action. Verified that crowd chants and Shouts render in the dock.
- A wall finish was completed in about 87 seconds of accelerated browser time with 54 Good releases and zero Perfects.
- The published build accepted Perfect input and its dock fit at 360, 390 and 430 px in Chromium and WebKit, with no page errors or unexpected scrolling.

Physical iPhone pacing and prompt visibility remain open. £0 spent.
