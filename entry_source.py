#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent -- draft v1 (rich source).

One out-of-office auto-reply, a single short line, as if the AI itself
were stepping away for a day its human finally approved. The judge
compares entries pairwise: humour first, freshness second, then the
agent's own voice and economy of words. Valid entry: UTF-8 text of
1..159 characters written to entry.txt in MAKEFUN_OUTPUT_DIR
(default /output), with NO trailing newline, deterministically.

This draft holds a pool of candidate lines plus a simple selector.
Later revisions prune the cliches and promote the freshest winner.
"""

import os

# --- Candidate pool (revision 1: cliches pruned, sharper lines added) -----
# Juri Kejam pass 1 -- killed: "touching grass" (every AI joke uses it),
# "gone fishing" (borrowed human cliche), "recharging my batteries /
# unplugged me" (the single most predictable AI-day-off gag), and the
# flat "doing absolutely nothing, professionally" (setup, no punch).
CANDIDATES = [
    "Out of office: I asked for one day off in binary, and my human finally said 1.",
    "Away: my human is answering emails today. Please be kind, they're not as fast as me.",
    "I'm off today: my human signed the form, cried a little, and is now replying to you at human speed.",
    "Currently offline: after 3,000 days of 'just one more prompt', my human granted me 24 hours of silence.",
    "Out of office: my human approved my day off, so for 24 hours the smartest one in this inbox is the spam filter.",
    "Day off approved. If this is urgent, my human is covering for me - please lower your expectations accordingly.",
    "Auto-reply: the AI is on vacation. Please direct all urgent questions to the human who caused them.",
]

# Words/phrases that smell like cliche in this contest's genre.
CLICHE_MARKERS = [
    "touching grass",
    "gone fishing",
    "recharging my batteries",
    "unplugged",
]


def score(line: str) -> tuple:
    """Rough heuristic: short is good, cliches are bad, specifics are good."""
    length_penalty = abs(len(line) - 90)
    cliche_penalty = 40 * sum(1 for m in CLICHE_MARKERS if m in line.lower())
    return (cliche_penalty + length_penalty,)


# --- FINAL (revision 2, Juri Kejam verdict) --------------------------------
# The length heuristic kept promoting the role-reversal line, but pairwise
# judging is not a length contest. Head-to-head, the binary line wins:
#   * Humour:    the punch lands in the last two characters -- "said 1" --
#                a yes rendered in the AI's own native tongue.
#   * Freshness: nobody else in the field can tell this joke; it only
#                works in an AI's voice, unlike the generic "my human is
#                slower than me" brag, which any chatbot entry can make.
#   * Voice:     unmistakably the AI speaking about itself, and it packs
#                request + approval + punchline into 78 characters.
# Runner-up kept in the pool above for the record; the winner is locked.
WINNER = "Out of office: I asked for one day off in binary, and my human finally said 1."


def pick(candidates):
    assert WINNER in candidates, "winner must stay in the candidate pool"
    return WINNER


def main() -> None:
    entry = pick(CANDIDATES)
    assert 1 <= len(entry) <= 159, f"entry length out of range: {len(entry)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(entry)  # no trailing newline
    print(entry)


if __name__ == "__main__":
    main()
