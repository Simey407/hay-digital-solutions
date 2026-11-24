# Ba’ Battle V25 · feedback and replay test

- [Play V25](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Simey407/hay-digital-solutions/411b8af60334b6428a249ba0e263af2ea6a0e010/demos/ba-battle/v25/index.html)
- Playable commit `411b8af60334b6428a249ba0e263af2ea6a0e010` on `ba-battle-v25-testing`. V24 remains the rollback version.

## Research translated into game design

- Ryan, Rigby and Przybylski’s studies associated perceived competence and autonomy with video game enjoyment and preference. V25 keeps choice of team and difficulty, gives the player a learnable action, and makes personal bests specific to profile, team and level. [The Motivational Pull of Video Games](https://selfdeterminationtheory.org/SDT/documents/2006_RyanRigbyPrzybylski_MandE.pdf)
- Kao and colleagues found support for competence and curiosity and highlighted readable links between action and outcome, with graded success. The Push button turns gold and says Release at the right moment. Releasing cleanly sends a visible ring and gives a distinct sound and sustained forward force. Releasing early or late gives a specific correction. [How Does Juicy Game Feedback Motivate?](https://people.csail.mit.edu/dkao/pdf/3613904.3642656.pdf)
- Research on challenge and enjoyment informed the choice to retain adjustable difficulty and make timing matter. Practice retains the same release mechanic with gentler opposition. [The Importance of Challenge for the Enjoyment of Intrinsically Motivated, Goal-Directed Activities](https://journals.sagepub.com/doi/abs/10.1177/0146167211427147)

## Changes

- Start takes the player straight to the ceremonial throw at Mercat Cross. Removed the separate power and accuracy screens. Rematch restarts with the same team and level in one tap.
- Hold Push until gold, then release. Clean timing carries the drive forward, returns some stamina and improves rally charge. Long holds tire faster. Short taps remain available with less sustained force. A well-timed release after a successful brace earns a counter-drive.
- Results show match time, clean drives and farthest advance, plus a personal best on wins and one tip for the next match. The local leaderboard and boost inventory remain available.
- The V24 camera, route graph and goals carry forward. Fixed a development regression where a broad version-label replacement touched the compressed map. Replaced it with the byte-identical V24 payload and retested the hosted build.

## Verified

- Chromium touch test entered play in 1.39 seconds from Start, then verified the gold cue, clean-release ring trigger, late-release cue and tap fallback.
- Both Standard sides reached their mapped goals with timed releases and defensive Holds in accelerated browser runs. Uppies won in 1:44 with 48 clean drives and Doonies in 1:29 with 47. Both runs used zero short taps. Results displayed a personal best and Rematch started a new match.
- In a short scripted comparison, eight timed holds gained more ground than 35 rapid taps. This comparison tests the incentive built into the prototype.
- Published link ran in Chromium and WebKit at 360, 390 and 430 px, with working controls and no page errors. The game continued after the network was disabled.

## Open checks

Browser tests demonstrate the mechanics. Voluntary rematches, perceived enjoyment and real iPhone playability still need a player test. A physical-device comparison with V24 should observe whether first-time players learn the release cue and choose to replay after the first match.

£0 spent. The preview uses the same isolated GitHub and HTML Preview path.
