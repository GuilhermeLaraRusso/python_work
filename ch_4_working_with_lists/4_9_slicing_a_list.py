# To make a slice, you specify the index of the first and last elements you
# want to work with. As with the range() function, Python stops one item
# before the second index you specify. To output the first three elements
# in a list, you would request indices 0 through 3, which would return elements
# 0, 1, and 2.

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])

# If you omit the first index in a slice, Python automatically starts your
# slice at the beginning of the list:

print(players[:4])

# A similar syntax works if you want a slice that includes the end of a list.
# For example, if you want all items from the third item through the last item,
# you can start with index 2 and omit the second index:

print(players[2:])

# Recall that a negative
# index returns an element a certain distance from the end of a list;
# therefore, you can output any slice from the end of a list. For example, if
# we want to output the last three players on the roster, we can use the slice
# players[-3:]:

print(players[-3:])