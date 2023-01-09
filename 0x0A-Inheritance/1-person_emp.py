#!/usr/bin/python3

"""Defines a class Person."""

# class Person(Object) - used in lower versions below python v3
class Person:
    """Class that defines a person."""
    # Constructor
    def __init__(self, name, id_number):
        """Initializes a person.

        Args:
            @name: Name of the person
            @id: Identity of the person.
        """
        self.name = name
        self.id_number = id_number

    # To check if this is an employee
    def Display(self):
        print(self.name, self.id_number)

# Driver code
emp_1 = Person("Caleb", 583)
emp_1.Display()

# Creating subclasses

"""Defines a subclass Employee."""


class Employee(Person):
    """Defines an employee."""

    def __init__(self, name, id_number, salary, position):
        """Initializes an employee."""

        # Invoke parent's init()
        Person.__init__(self, name, id_number)
        
        self.salary = salary
        self.position = position

emp_2 = Employee("Bertha", 34556, "5000 GHS", "Staff Nurse")
emp_2.Display()
