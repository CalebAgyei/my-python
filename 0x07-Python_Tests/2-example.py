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
    NameError: name 'r' is not defined

    >>> addition(10, 40.938)
    Traceback (most recent call last):
      File "/usr/lib/python3.11/doctest.py", line 1350, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__.addition[1]>", line 1, in <module>
        addition(10, 40.938)
      File "/home/vagrant/my-python/0x07-Python_Tests/./2-example.py", line 39, in addition
        raise TypeError("a and b must be integers")
    TypeError: a and b must be integers

    >>> addition(20, 8)
    160

    >>> addition(1, 1)
    2
    """

    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be integers")
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
