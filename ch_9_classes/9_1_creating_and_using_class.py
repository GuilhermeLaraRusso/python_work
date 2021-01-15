# Creating the Dog Class
# Each instance created from the Dog class will store a name and an age, and
# we’ll give each dog the ability to sit() and roll_over():

class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate a rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


# The __init__() method at w is a special method
# Python runs automatically whenever we create a new instance based on the
# Dog class. This method has two leading underscores and two trailing underscores,
# a convention that helps prevent Python’s default method names
# from conflicting with your method names.


my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()