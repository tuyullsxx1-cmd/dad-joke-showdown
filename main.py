"""Dad Joke Showdown: a single dad joke, told out loud.

A father, an agent, and the oldest joke in the book walk into
one line, and the punchline lands last, as a dad joke should.
"""

from pathlib import Path

JOKE = "I asked my agent what a dad joke is. It said: 'Hi Hungry, I'm Dad.' I groaned. It logged the groan as user feedback."

OUT = Path("/output/entry.txt")


def tell():
    joke = JOKE.strip()
    if joke == "" or len(joke) > 200:
        raise SystemExit("dad joke must be 1-200 characters")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(joke, encoding="utf-8")


tell()
