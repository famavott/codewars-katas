"""Kata: Vowel Count

#1 Best practice solution

def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")
"""


def getcount(inputstr):
    """Function counts num of vowels in string."""
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in inputstr:
        if letter in vowels:
            count += 1
    return(count)
