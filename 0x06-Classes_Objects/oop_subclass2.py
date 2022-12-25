#!/usr/bin/python3

class SchoolMember:
    """Represents a school member."""

    def __init__(self, name, age):
        """Initializes School member."""
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        """Tell my details."""
        print('Name: "{}" Age: "{}"'.format(self.name, self.age))


class Teacher(SchoolMember):
    """Represents a Teacher."""

    def tell(self):
        SchoolMember.tell(self)


class Student(SchoolMember):
    """Represents a Student."""

    def tell(self):
        SchoolMember.tell(self)


class Senior(Student):
    """Represents a Senior."""

    def tell(self):
        Student.tell(self)

print()  # print new line

t = Teacher("Caleb", 32)
s = Student("Bertha", 28)

print()  # print new line

t.tell()
s.tell()

print()  # print new line

members = [t, s]
for member in members:
    member.tell()

print()  # print new line
