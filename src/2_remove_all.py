"""Second attempt at remove all kata."""


def remove(text, what):
    """."""
    for key in what:
        text = text.replace(key, '', what[key])
    return text
