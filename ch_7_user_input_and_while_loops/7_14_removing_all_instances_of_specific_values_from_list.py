# In Chapter 3 we used remove() to remove a specific value from a list. The
# remove() function worked because the value we were interested in appeared
# only once in the list. But what if you want to remove all instances of a value
# from a list?

# Se usar apenas pet.remove('cat'), apenas o primeiro 'cat' será removido

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

# pets.remove('cat')

print(pets)

# We start with a list containing multiple instances of 'cat'. After printing
# the list, Python enters the while loop because it finds the value 'cat' in the list
# 130 Chapter 7
# at least once. Once inside the loop, Python removes the first instance of 'cat',
# returns to the while line, and then reenters the loop when it finds that 'cat' is
# still in the list. It removes each instance of 'cat' until the value is no longer in
# the list, at which point Python exits the loop and prints the list again: