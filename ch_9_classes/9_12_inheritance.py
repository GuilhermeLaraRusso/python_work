# Inheritance
# You don’t always have to start from scratch when writing a class. If the class
# you’re writing is a specialized version of another class you wrote, you can
# use inheritance. When one class inherits from another, it automatically takes
# on all the attributes and methods of the first class. The original class is
# called the parent class, and the new class is the child class. The child class
# inherits every attribute and method from its parent class but is also free to
# define new attributes and methods of its own.

# The first task Python has when creating an instance from a child class is to
# assign values to all attributes in the parent class. To do this, the __init__()
# method for a child class needs help from its parent class.
# As an example, let’s model an electric car. An electric car is just a specific
# kind of car, so we can base our new ElectricCar class on the Car class
# we wrote earlier. Then we’ll only have to write code for the attributes and
# behavior specific to electric cars.
# Let’s start by making a simple version of the ElectricCar class, which
# does everything the Car class does:


class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())


# At u we start with Car. When you create a child class, the parent class
# must be part of the current file and must appear before the child class in
# the file. At v we define the child class, ElectricCar. The name of the parent
# class must be included in parentheses in the definition of the child class.
# The __init__() method at w takes in the information required to make a Car
# instance.

# The super() function at x is a special function that helps Python make
# connections between the parent and child class. This line tells Python to
# call the __init__() method from ElectricCar’s parent class, which gives an

# ElectricCar instance all the attributes of its parent class. The name super
# comes from a convention of calling the parent class a superclass and the
# child class a subclass.