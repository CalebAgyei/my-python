#!/usr/bin/python3

class A:
    def __init__(self):
        self.__hello = "Hello"


class B(A):
    def __init__(self):
        A.__init__(self)
        self.__how = "Great"

object1 = B()
print(object1.hello)  # Error - B cannot access a private member hello
