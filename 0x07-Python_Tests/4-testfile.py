#!/usr/bin/python3
import doctest
doctest.testfile("example.txt")

def addition(a, b):
    """Returns the sum of two numbers.

    Args:
        @a: First number
        @b: Second number

    Return:
        Sum of a and b

    >>> addition(20, 8)
    28

    >>> addition(1, 1)
    2
    """

    return a + b

doctest.testfile("example.txt")
