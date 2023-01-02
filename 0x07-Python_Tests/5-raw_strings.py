#!/usr/bin/python3
def f(x):
    r"""Backslashes in a raw doctring: m\n"""  # add r to make it a raw string
    pass

print(f.__doc__)
