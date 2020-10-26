# Although you can’t modify a tuple, you can assign a new value to a variable
# that holds a tuple.


dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# When compared with lists, tuples are simple data structures. Use them
# when you want to store a set of values that should not be changed throughout
# the life of a program.