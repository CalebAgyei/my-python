class Robot:
    """Creates a Robot with a name."""

    population = 0

    def __init__(self, name):
        """Initializes the data."""

        self.name = name
        print("(Initializing all-new robot {})".format(self.name))

        Robot.population += 1
        print("Our total number now is {:d}".format(Robot.population))

    def say_hi(self):
        """Introducing robot."""

        print("Hello, my name is {} and I'm very happy to meet you".format(self.name))

    def die(self):
        """Robot is dying."""

        print("OMG robot {} is dying".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("The last robot to die was {}".format(self.name))
        else:
            print("There are still {} robots active".format(Robot.population))

    def can_do(self):
        print("I am strong and can do amazing things")

    @classmethod
    def how_many(cls):
        print("We have {:d} robots left".format(Robot.population))

print("=======================")
droid1 = Robot("R2-D2")
droid1.say_hi()
droid1.can_do()
Robot.how_many()

print("=======================")
happy2 = Robot("H40")
happy2.say_hi()
happy2.can_do()
Robot.how_many()

print("=======================")
droid1.die()

print("=======================")
happy2.die()

Robot.how_many()
print("=======================")

print("***PRINTING DOCSTRINGS***")
print(Robot.__doc__) # class docstrings
print(Robot.say_hi.__doc__) # method docstrings
