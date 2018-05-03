"""."""


def reverse_fizzbuzz(string):
    """Return list of numbers that generate the string passed as arg."""
    final_array = []
    words = string.split()
    for word in words:
        if word == 'Fizz':
            final_array.append(3)
        elif word == 'Buzz':
            final_array.append(5)
        elif word == 'FizzBuzz':
            final_array.append(15)
        else:
            final_array.append(int(word))
    return final_array
