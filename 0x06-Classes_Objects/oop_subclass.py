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
        print('Name: "{}", Age: "{}",'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    """Represents a Teacher."""

    def __init__(self, name, age, salary):
        """Initializes Teacher."""
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('My salary: "{}"'.format(self.salary))


class Student(SchoolMember):
    """Represents a Student."""

    def __init__(self, name, age, score):
        """Initializes a Student."""
        SchoolMember.__init__(self, name, age)
        self.score = score
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Class score: "{}"'.format(self.score))


class Senior(Student):
    """Represents a Senior."""

    def __init__(self, name, age, score, team):
        """Initializes a Senior student."""
        Student.__init__(self, name, age, score)
        self.team = team
        print('(Initialized Senior: {})'.format(self.name))

    def tell(self):
        Student.tell(self)
        print('Team: "{}"'.format(self.team))


print("=============")
t = Teacher("Caleb", 32, 10000)
print("=============")
s = Student("Bertha", 28, 3500)


print("=============")
t.tell()
print("=============")
s.tell()

print("=============")
members = [t, s]
for member in members:
    member.tell()
