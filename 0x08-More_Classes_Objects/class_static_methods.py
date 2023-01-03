#!/usr/bin/python3
class Employee:
    """Represents an employee of MoringaConnect."""
    
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first_name, last_name, pay):
        """Initializes and employee of MoringaConnect."""
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        """Defines fullname of employee."""
        return ("{} {}".format(self.first_name, self.last_name))

    def apply_raise(self):
        """Calculates employee's pay."""
        self.pay = int(self.pay * self.raise_amt)

    def email_add(self):
        return ("{}.{}@gmail.com".format(self.first_name, self.last_name))

    @classmethod
    def set_raise_amt(cls, amount):
        """Change instance method to class method."""
        cls.raise_amt = amount

emp_1 = Employee("Caleb", "Agyei", 10560)
emp_2 = Employee("Rashida", "Eliasu", 5600)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

print(emp_1.fullname())
print(emp_1.email_add())

