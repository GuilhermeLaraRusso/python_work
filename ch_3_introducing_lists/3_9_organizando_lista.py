# Sorting a List Permanently with the sort() Method

# Python’s sort() method makes it relatively easy to sort a list. Imagine we
# have a list of cars and want to change the order of the list to store them
# alphabetically. To keep the task simple, let’s assume that all the values in
# the list are lowercase.


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# The sort() method, shown at u, changes the order of the list permanently.
# The cars are now in alphabetical order, and we can never revert to
# the original order:



# You can also sort this list in reverse alphabetical order by passing the
# argument reverse=True to the sort() method. The following example sorts
# the list of cars in reverse alphabetical order:

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
