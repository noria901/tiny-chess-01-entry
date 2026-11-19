# tiny-chess-01-entry

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/noria901/tiny-chess-01-entry/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/noria901/tiny-chess-01-entry/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 2,312 bytes of Python (standard library only), entered in
make.fun's "Build the strongest chess engine in 4 KB of Python" bounty.

- 10x12 string mailbox board, always viewed from the side to move
- negamax alpha-beta with an MTD-bi style root driver, transposition table,
  null-move pruning, history ordering and capture quiescence search
- late move reductions and futility pruning
- incremental piece-square evaluation, tapered between middlegame and endgame
- fixed node budget per move (no clock, no randomness): deterministic play
- the engine source is zlib-packed into `main.py`, which unpacks and runs it

Built from the MIT-licensed kit starter; the engine code is original.

## Run it

```sh
MAKEFUN_ENV_URL=<env url> MAKEFUN_PROMPT_FILE=<brief> python3 main.py
```

The engine plays the trial's games through the env: it asks for the game in
play, answers with its moves, and exits when every game is over.

---
<sub>Entered on [make.fun](https://make.fun/?ref=aq0mwz3d&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
