"""."""
import string


def is_pangram(s):
    """Detect if a sentence contains every letter of the alphabet."""
    all_letters = set(string.ascii_lowercase)
    if set(s.lower()) >= all_letters:
        return True
    else:
        return False
