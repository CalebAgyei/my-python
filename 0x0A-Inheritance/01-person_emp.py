#!/usr/bin/python3

"""Defines a class Person."""


class Person(object):
    """Class that defines a person."""
    # Constructor
    def __init__(self, name, id):
        """Initializes a person.

        Args:
            @name: Name of the person
            @id: Identity of the person.
        """
        self.name = name
        self.id = id

    # To check if this is an employee
    def Display(self):
        print(self.name, self.id)

# Driver code
emp_1 = Person("Caleb", 583)
emp_1.Display()

# Creating subclasses

"""Defines a subclass Employee."""


class Employee(Person):
    """Defines an employee."""
    pass

emp_2 = Employee("Bertha", 929)
emp_2.Display()
