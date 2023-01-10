#!/usr/bin/python3
"""Defines a class Animal."""


class Animal:
    """Creates a class Animal."""

    def __init__(self, birth_type="Unknown", appearance="Unknown",
            blooded="Unknown"):
        """Initializes an animal.


        Args:
            @birth_type: How animal was born.
            @appearance: How animan looks like.
            @blooded: Whether animal's blood is warm or cold.
        """
        self.birth_type = birth_type
        self.appearance = appearance
        self.blooded = blooded

    @property
    def birth_type(self):
        """Returns a private instance of birth_type."""
        return (self.__birth_type)

    @birth_type.setter
    def birth_type(self, birth_type):
        """Sets birth_type to a new value."""
        self.__birth_type = birth_type

    @property
    def appearance(self):
        """Returns a private instance of appearance."""
        return (self.__appearance)

    @appearance.setter
    def appearance(self, appearance):
        """Sets appearance to a new value."""
        self.__appearance = appearance

    @property
    def blooded(self):
        """Returns a private isntance of blooded."""
        return (self.__blooded)

    @blooded.setter
    def blooded(self, blooded):
        """Sets blooded to a new value."""
        self.__blooded = blooded

    def __str__(self):
        """Return a string representation."""
        return ("A {} is {} it is {} it is {}".format(type(self).__name__, self.birth_type,
            self.appearance, self.blooded))


"""Creates a new subclass Mammal."""

class Mammal(Animal):
    """Defines a mammal."""

    def __init__(self, birth_type="born alive", appearance="hair or fur",
            blooded="warm blooded", nurse_young=True):
        Animal.__init__(self, birth_type, appearance,
                blooded)  # No need to bring default values

        self.__nurse_young = nurse_young  # why return private here???

    @property
    def nurse_young(self):
        """Returns a private instance of nurse_young."""
        return (self.__nurse_young)

    @nurse_young.setter
    def nurse_young(self, nurse_young):
        """Sets nurse_young to a new value."""
        self.__nurse_young = nurse_young

    
    # Define a magic method to overwrite a method in base/parent class
    # super() - superclass Animal
    # super().__str__()

    def __str__(self):
        return (super().__str__() + "and it is {} they nurse "\
                "their young" .format(self.nurse_young))  # No use of private __nurse_young


"""Defines a new subclass Reptile."""

class Reptile(Animal):
    """Creates a class Reptile."""

    def __init__(self, birth_type="born in an egg or born alive",
            appearance="dry scales", blooded="cold blooded"):
        
        Animal.__init__(self, birth_type, appearance, blooded)

    
    # function overloading in Python - simpler than in other languages

    def sum_all(self, *args):
        """Returns sum of unknown number of arguments."""
        
        sum = 0

        for i in args:
            sum += i

        return (sum)

# POLYMORPHISM

def get_birth_type(the_object):
    print("the {} is {}".format(type(the_object).__name__,
        the_object.birth_type))


def main():
    animal1 = Animal("born alive")

    print(animal1.birth_type)

    print(animal1)
    print()

    mammal1 = Mammal()

    print(mammal1.birth_type)
    print(mammal1.appearance)
    print(mammal1.nurse_young)
    print()
    print(mammal1)
    print()

    reptile1 = Reptile()

    print(reptile1.birth_type)
    print(reptile1.appearance)
    print(reptile1.blooded)
    print()
    print(reptile1)
    print()

    print("Sum : {}".format(reptile1.sum_all(1, 2, 3, 4, 5)))
    print()

    get_birth_type(reptile1)
    get_birth_type(mammal1)
    print()



main()
