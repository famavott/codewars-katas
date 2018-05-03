"""."""


def remove(text, targets):
    """."""
    for key, val in targets.items():
        if key in text:
            text = text.replace(key, '', val)
    return text


remove('this is a string', {'t': 1, 'i': 2})
