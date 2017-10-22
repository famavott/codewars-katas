"""Kata: Simple Pig Latin

#1 Best practice solution

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
"""


def pig_it(string):
    """Function creates string with simple pig latin words."""
    pyg = "ay"
    final_output = ""
    for word in string.split():
        if not word.isalpha():
            final_output += word + " "
            break
        else:
            first = word[0]
            new_word = word + first + pyg
            new_word = new_word[1:len(new_word)]
            final_output += new_word + " "
    return(final_output[:-1])
