#!/usr/bin/python3
"""This is my 2nd example.

>>> addition(4, 5)
9

>>> addition(5, 6)
10
"""

def addition(a, b):
    """Returns the sum of two numbers.

    Args:
        @a: First number
        @b: Second number

    Return:
        Sum of a and b

    >>> addition(r, 4)
    Traceback (most recent call last):
        ...
    TypeError: a and b must be integers

    >>> addition(10, "Hello")
    Traceback (most recent call last):
        ...
    TypeError: a and b cannot be strings

    >>> addition(20, 8)
    160

    >>> addition(1, 1)
    2
    """

    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be integers")
    if isinstance(a, str) or isinstance(b, str):
        raise TypeError("a and b cannot be strings")
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
