# Modifying an Attribute’s Value Through a Method
# It can be helpful to have methods that update certain attributes for you.
# Instead of accessing the attribute directly, you pass the new value to a
# method that handles the updating internally.
# Here’s an example showing a method called update_odometer():


class Car():

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

# The only modification to Car is the addition of update_odometer() at u.
# This method takes in a mileage value and stores it in self.odometer_reading.
# At v we call update_odometer() and give it 23 as an argument (corresponding
# 170 Chapter 9
# to the mileage parameter in the method definition). It sets the odometer
# reading to 23, and read_odometer() prints the reading: