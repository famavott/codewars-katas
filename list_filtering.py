"""Kata: List Filering

#1 Best practice solution

def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]

"""


def filter_list(given_list):
    """Function filers list and removes anything that is not an int."""
    return [i for i in given_list if type(i) is int]
