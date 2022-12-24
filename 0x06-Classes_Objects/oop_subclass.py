class SchoolMember:
    """Represents a school member."""

    def __init__(self, name, age):
        """Initializes School member."""
        self.name = name
        self.age = age


class Teacher(SchoolMember):
    """Represents a Teacher."""

    def __init__(self, name, age, salary):
        """Initializes Teacher."""
        SchoolMember.__init__(self, name, age)
        self.salary = salary



class Student(SchoolMember):
    """Represents a Student."""

    def __init__(self, name, age, marks):
        """Initializes a Student."""
        SchoolMember.__init__(self, name, age)
        self.marks = marks


class Senior(Student):
    """Represents a Senior."""

    def __init__(self, name, age, marks, team):
        """Initializes a Senior student."""
        Student.__init__(self, name, age, marks)
        self.team = team
