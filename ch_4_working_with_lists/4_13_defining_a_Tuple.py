# Lists work well for storing sets of items that can change throughout the
# life of a program. The ability to modify lists is particularly important when
# you’re working with a list of users on a website or a list of characters in a
# game. However, sometimes you’ll want to create a list of items that cannot
# change. Tuples allow you to do just that.
#
# Python refers to values that cannot
# change as immutable, and an immutable list is called a TUPLE.


# A tuple looks just like a list except you use parentheses instead of square
# brackets. Once you define a tuple, you can access individual elements by
# using each item’s index, just as you would for a list.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])


# Let’s see what happens if we try to change one of the items in the tuple
# dimensions:

dimensions[0] = 250

# The code at u tries to change the value of the first dimension, but
# Python returns a type error. Basically, because we’re trying to alter a tuple,
# which can’t be done to that type of object, Python tells us we can’t assign a
# new value to an item in a tuple: