# tiny-chess-4k

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/adivadena1/tiny-chess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/adivadena1/tiny-chess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A small, original chess engine in Python 3.13 (stdlib only), written for the
make.fun `tiny-chess-01` bounty. It plays the gauntlet through the env
(`MAKEFUN_ENV_URL`).

## Run it

```sh
python3 main.py
```

## How it plays

- **Board:** 0x88 mailbox, full legal move generation (castling, en passant,
  promotions). Moves are packed ints; `D()` self-checks legality.
- **Search:** iterative deepening to a fixed 200,000-node budget/move,
  alpha-beta with quiescence over captures (and full evasions in check).
  Ordering: MVV-LVA captures, then one killer per ply. No clock is read,
  so a replay plays identical moves (deterministic).
- **Repetition avoidance (v1.1):** the engine tracks the game path in a set
  `HS` of board tuples; a position already on the path scores 0 in the main
  search, so it avoids repeating when ahead and seeks it when behind.
- **Eval:** material (P100 N320 B330 R500 Q900) + piece-square tables
  (N/B share one table, R/Q share another, P and K their own). No opening
  book: a continuation table for the 40 known lines needs ~300+ bytes and
  does not fit.
- **Protocol:** `POST /game`, `POST /move` (UCI), until `{"status": "done"}`.

## Limits

- `main.py` is 4,095 bytes (limit 4,096) — dense but readable multi-line
  Python, no compressed payload. ~40–44k nodes/s, so 200k nodes is about
  4.5–5.0 s/move (limit 10 s/move). Practice Elo v1.1: **1,221** over
  18 games (8W 0D 10L) — clears the 1,154 bar. See `dev/BUILD-REPORT.md`.

## Files

- `main.py` — the engine (only file the bot runs).
- `README.md` — this file.
- `LICENSE` — MIT.

---

<sub>Entered on [make.fun](https://make.fun/?ref=3txr3dna&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
