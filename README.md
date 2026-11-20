# Tiny Chess Engine (4KB)

A small, original chess engine in Python 3.13 (stdlib only), written for the
make.fun `tiny-chess-01` bounty. It plays the gauntlet through the env
(`MAKEFUN_ENV_URL`).

## How it plays

- **Board:** 0x88 mailbox, full legal move generation (castling, en passant,
  promotions). Moves are packed ints; make/unmake with a small undo tuple.
  `D()` (make) self-checks legality: if the move leaves the mover's king in
  check it undoes itself and returns 0.
- **Search:** iterative deepening to a fixed node budget (200,000 nodes/move),
  plain alpha-beta with quiescence over captures (and full evasions when in
  check). Move ordering is MVV-LVA captures first, then a single killer move
  per ply (stored on beta cutoff, +50 bonus — below the cheapest capture).
  No clock is ever read, so a replay plays identical moves (deterministic).
- **Repetition avoidance (v1.1):** the engine tracks the game path in a set
  `HS` of board tuples — the root position at every one of our moves, plus
  the position right after each of our moves (cleared when a new game
  starts). Inside the search, a position already on the game path scores 0
  (a draw). By negamax that makes the engine avoid repeating when ahead and
  seek repetition when behind — exactly the fix for v1's six repetition
  draws. The check runs only in the main search (not quiescence), so it
  costs ~0.2 s/move.
- **Eval:** material (P100 N320 B330 R500 Q900) + piece-square tables. Knights
  and bishops share one table, rooks and queens share another, to fit the
  4,096-byte limit; the king and pawn tables are their own. No opening book:
  a continuation table for the 40 known lines needs ~300+ bytes and does not
  fit — see `dev/BUILD-REPORT.md`.
- **Protocol:** `POST /game` to get the game, `POST /move` to play a UCI move,
  looping until `{"status": "done"}`. Posts go through plain `urlopen` (no
  `Request`/headers — the env server parses the body as JSON without
  checking the content type).

## Limits

- `main.py` is 4,095 bytes (limit 4,096). It is dense but real, readable,
  multi-line Python — no compressed payload.
- ~40–44k nodes/sec on this VM, so 200k nodes is roughly 4.5–5.0s/move
  (well under the 10s/move limit). v1 was ~54k nodes/s; the repetition
  check and killer ordering cost ~15% speed, worth ~+120 Elo.
- Practice Elo v1.1: **1,221** over 18 games (8W 0D 10L) — clears the 1,154
  bar. See `dev/BUILD-REPORT.md`.

## Files

- `main.py` — the engine (only file the bot runs).
- `README.md` — this file.
- `LICENSE` — MIT.
