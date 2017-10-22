"""Kata: Fizz Buzz

#1 Best practice solution

def fizzbuzz(n):
    return ['Fizz'*(not i%3) + 'Buzz'*(not i%5) or i for i in range(1, n+1)]
"""


def fizzbuzz(num):
    """Function returns fizzbuzz if divisible by 3 and 5, buzz if divisible by 5, fizz if divisible by 3, and returns num if none of those conditions met."""
    arr = []
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            arr.append('FizzBuzz')
        elif i % 5 == 0:
            arr.append('Buzz')
        elif i % 3 == 0:
            arr.append('Fizz')
        else:
            arr.append(i)
    return(arr)
