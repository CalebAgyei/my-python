#!/usr/bin/python3

class Base:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return (self.name)


# Inherited or subclass

class Child(Base):
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    def get_age(self):
        return (self.age)


# Inherited or subclass

class GrandChild(Child):
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    def get_address(self):
        return (self.address)

# Driver code
g = GrandChild("Geek1", 23, "Nodia")
print(g.get_name())
print(g.get_age())
print(g.get_address())
