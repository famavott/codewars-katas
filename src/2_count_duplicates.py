"""Second attempt at count duplicates kata."""


def duplicate_count(text):
    """."""
    text = text.lower()
    counter = {}
    for let in text:
