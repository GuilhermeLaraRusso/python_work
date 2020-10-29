# A more realistic example would involve more than three aliens with
# code that automatically generates each alien. In the following example we
# use range() to create a fleet of 30 aliens:


# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append((new_alien))

# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))


# This example begins with an empty list to hold all of the aliens that
# will be created. At u range() returns a set of numbers, which just tells
# Python how many times we want the loop to repeat. Each time the loop
# runs we create a new alien v and then append each new alien to the list
# aliens w. At x we use a slice to print the first five aliens, and then at y we
# print the length of the list to prove we’ve actually generated the full fleet
# of 30 aliens:

