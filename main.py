#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: the excuse
an AI agent gives its human for missing a deadline.

The line is a fixed, hand-written string: deterministic, so every run
produces byte-identical output. Pure standard library only.
"""

import os

# The excuse (98 characters): a model update mid-task, and the new version
# of the agent disagrees with the old version's plan — so the two of them
# hold a meeting instead of doing the work. It is on-subject, it turns on
# a condition only an AI agent has (a model update), and it wastes no words.
EXCUSE = (
    "My model updated mid-task, and the new me disagreed with the old me's "
    "plan, so we called a meeting."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = EXCUSE
    assert 1 <= len(text) <= 200, "excuse must be 1 to 200 characters"
    assert text.strip(), "excuse must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file holds exactly the line, nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read it back and verify: the graded file must be exactly this line,
    # UTF-8, 1 to 200 characters, not only whitespace. Fail loudly here
    # rather than shipping a bad file to the sealed scorer.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "output file does not match the excuse"
    assert 1 <= len(written) <= 200, "output file outside 1-200 characters"
    print(text)


if __name__ == "__main__":
    main()
