#!/usr/bin/python3

def add(a, b):
    """Add two numbers.
    >>> 1 + None
    Traceback (most recent call last):
      File "/usr/lib/python3.11/doctest.py", line 1350, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__.add[0]>", line 1, in <module>
        1 + None
        ^~~~~~~~
    TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
    """
    # markers ^ and tildes ~ will not affect the outcome
    
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
