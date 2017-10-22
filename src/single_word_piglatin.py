"""Kata: Single Word Piglatin

#1 Best practice solution

VOWELS = set('aeiou')

def pig_latin(st):
    s = st.lower()
    if s.isalpha():
        if set(s) & VOWELS:
            if s[0] in VOWELS:
                s += 'w'
            while s[0] not in VOWELS:
                s = s[1:] + s[:1]
        return s + 'ay
"""


def pig_latin(s):
    """Function creates words with arbitrary rules."""
    vowels = ['a', 'e', 'i', 'o', 'u']
    lowstring = s.lower()
    if lowstring.isalpha():
        if lowstring[0] in vowels:
            return(lowstring + 'way')
        elif lowstring[0] not in vowels:
            vowel_index = 0
            for idx, letter in enumerate(lowstring):
                if letter in vowels:
                    vowel_index = idx
                    break
            return(lowstring[vowel_index] + lowstring[vowel_index + 1:] + lowstring[:vowel_index] + 'ay')
        else:
            return(lowstring + 'ay')
    else:
        return None
