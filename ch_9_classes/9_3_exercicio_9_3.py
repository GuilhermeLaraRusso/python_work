# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.



class User():
    """A simple User interface"""

    def __init__(self, first_name, last_name, age, height, ):
        """Initialize first and last name of the user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height

    def greet_user(self):
        print("Hello " + self.first_name())

user1 = User('guilherme', 'russo', 32, 179)
print("First Name: " + user1.first_name.title())
print("Last Name: " + user1.last_name.title())
print("Age: " + str(user1.age))
print("Height: " + str(user1.height) + " cm")

print("\nHello, " + user1.first_name.title() + " " + user1.last_name.title())


