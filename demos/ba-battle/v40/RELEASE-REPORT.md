# Ba’ Battle V40 · Accounts and public boards

- Branch `ba-battle-v40-testing`
- Playable build `b53f57a3cf8d3188a03d19661e200f0820dd8e7c`
- [iPhone guest preview](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Simey407/hay-digital-solutions/b53f57a3cf8d3188a03d19661e200f0820dd8e7c/demos/ba-battle/v40/index.html)

## Delivered

Players use a private username and password, choose Uppies or Doonies when creating the account, and appear publicly under a separate nickname. The server and database enforce the permanent choice. Password-confirmed deletion removes the account, sessions and board results. A subsequent registration can choose either side.

Team & Profile edits the public nickname, personal team crest and profile trim. Four public boards rank total wins, best Perfect streak in a single match, highest single-match score and fastest win. Rankings combine difficulty levels in this beta. Guests can view the public boards on a connected tester and can still play, select either side and use the local history and leaderboard in the static preview.

The same-origin tester uses Python's standard library and persistent SQLite. It stores salted PBKDF2-HMAC-SHA256 password hashes, hashes session tokens at rest, and checks the origin for account and score changes. Public requests receive nicknames, side, cosmetics and ranking values. Match tickets are single-use and checked against the signed-in account, locked side and elapsed time.

## Verification

- Chromium and WebKit at 360, 390 and 430 CSS pixels. Tested signup, profile styling save, sign-out, case-insensitive sign-in, reload persistence, team lock in UI and API, password-confirmed deletion and re-registration for the opposite side.
- Independent guest browsers saw all four rankings without the private username and saw the results removed after deletion. The API rejected duplicate result submissions.
- Chromium completed a full Uppies guest match with the existing accelerated QA clock, checked the goal result, replay controls, rematch and persistent local match history. No browser JavaScript errors were recorded in that run or in the account matrix.
- Chromium also completed a signed-in Uppies match with accelerated game time and a fixture-adjusted ticket timestamp. The browser submitted the goal result, and an independent guest context saw the win on the public board.
- The pinned public preview opened in mobile-emulated Chromium, reported that accounts need the connected tester and allowed a Doonies throw-up.
- Fixed duplicate leaderboard rows when two requests for the same board completed out of order. Retested in both engines.

## Run the connected tester

From the repository root, use Python 3.9+ with SQLite 3.35+ and a database path outside the checkout.

```sh
python3 demos/ba-battle/v40/server.py --database /tmp/ba-battle-v40.sqlite3
```

Open [the local tester](http://127.0.0.1:8040/). The process binds to loopback. The database persists between runs when the same path is used. Use a persistent private directory if retaining test accounts.

## Outstanding

The static preview supports guest play. Account features and shared boards were tested on the local direct server and need an isolated HTTPS host for cross-device review. No physical iPhone testing was performed for V40. Browser-reported results are provisional. A single-use match ticket prevents duplicate submission but cannot independently verify the play that produced a score. Password recovery and nickname moderation are outside this tester. The Kirkwall geography was carried forward from V39 and was not revalidated in this account release.

No spend, hosted backend, or production deployment.
