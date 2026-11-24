# Ba’ Battle V33 · visual assessment and style

- [Play V33](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Simey407/hay-digital-solutions/278dc716f8814466efc67836c34a224e823b2bfd/demos/ba-battle/v33/index.html)
- Playable commit `278dc716f8814466efc67836c34a224e823b2bfd` on `ba-battle-v33-testing`. V32 remains available for rollback.

## Assessment

| Area | V32 observation | V33 decision |
| --- | --- | --- |
| Identity | The real streets and goal calls are distinctive. The blue interface could belong to many sports apps. | Use a winter match programme palette across the header, score strip, setup, dock and results. Give Kirkwall, Orkney the masthead byline. |
| Map | Dark street labels competed with players. Several roofs looked alike at close zoom. | Use quieter street labels, warm paving, varied stone roof fills, cool harbour water and a red sandstone tint for the mapped cathedral footprint. Use a distinct landmark marker. |
| Action | The stable Push and Hold dock and direct side actions worked. Toasts, chants and surge warnings occupied overlapping space. | Preserve the direct controls. Put cues in one position and give urgent events priority. Increase common UI text and make the zoom and header touch targets at least 44 CSS pixels. |
| Remaining | The scrum is easy to miss when zoomed out. | Check actual iPhone readability outdoors and observe whether first-time players can explain why a surge began. |

References were the local event description and archive photos for setting, Dinosaur Polo Club’s design material for separating map information from gameplay objects, and Apple’s guidance for readable game controls and context-sensitive touch actions. The palette is original and the map remains the same OpenStreetMap extract. [Orkney’s Ba’ event](https://www.orkney.com/events/new-years-day-ba) · [Orkney winter photos](https://www.orkney.com/news/an-orkney-christmas) · [Mini Motorways design material](https://dinopoloclub.com/press/mini-motorways/) · [Apple game controls](https://developer.apple.com/design/human-interface-guidelines/game-controls)

## Verification

- Compared V32 and V33 screenshots with the same zoom and phone viewport. Checked V33 at 360, 390 and 430 px. Confirmed the major match controls were at least 44 × 44 CSS pixels, reachable and free of overlap. A forced surge confirmed the warning occupied the shared cue area.
- The published build passed at all three widths in Chromium and WebKit without page errors or unexpected scrolling.
- Completed an Uppies match with 46 clean drives. Verified the wall replay, return to results, preserved rewards and match history after reload.
- The bundled Kirkwall map remained byte-identical. £0 spent.

Physical iPhone and outdoor readability checks remain open.
