# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1. Write
# another method called reset_login_attempts() that resets the value of login_
# attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

class User():
    """A simple User interface"""

    def __init__(self, first_name, last_name, age, height, ):
        """Initialize first and last name of the user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.login_attempts = 0

    def greet_user(self):
        print("Hello " + self.first_name())

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts


user1 = User('guilherme', 'russo', 32, 179)
print("First Name: " + user1.first_name.title())
print("Last Name: " + user1.last_name.title())
print("Age: " + str(user1.age))
print("Height: " + str(user1.height) + " cm")

print("\nHello, " + user1.first_name.title() + " " + user1.last_name.title())

while user1.login_attempts < 5:
    print("Number of login attempts: " + str(user1.increment_login_attempts()))

print("\nResetting login attempts")
print("Number of login attempts: " + str(user1.reset_login_attempts()))


