"""Find all anagrams of a word in a list."""


def anagrams(word, words):
    """Return list of words that are anagrams."""
    final_list = []
    to_match = ''.join(sorted(word))
    for i in words:
        if ''.join(sorted(i)) == to_match:
            final_list.append(i)
    return final_list
