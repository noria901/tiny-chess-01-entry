# tiny-chess-01 entry

`main.py`: a chess engine in under 4 KB of Python (standard library only).

- 10x12 string mailbox board, always viewed from the side to move
- negamax alpha-beta with an MTD-bi style root driver, transposition table,
  null move, history ordering, capture quiescence search
- incremental piece-square evaluation, tapered between middlegame and endgame
- fixed node budget per move (no clock, no randomness): deterministic

Built from the MIT-licensed kit starter; the engine code is original.
