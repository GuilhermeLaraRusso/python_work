# Removendo um Item utilizando o comando 'del'

# If you know the position of the item you want to remove from a list, you can
# use the del statement.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)


# Removendo um item utilizando o comando 'pop()'

# Sometimes you’ll want to use the value of an item after you remove it from a
# list. For example, you might want to get the x and y position of an alien that
# was just shot down, so you can draw an explosion at that position. In a web
# application, you might want to remove a user from a list of active members
# and then add that user to a list of inactive members.
#
# The pop() method removes the last item in a list, but it lets you work
# with that item after removing it. The term pop comes from thinking of a
# list as a stack of items and popping one item off the top of the stack. In
# this analogy, the top of a stack corresponds to the end of a list.

motorcycles_2 = ['honda', 'yamaha', 'suzuki']
print(motorcycles_2)

popped_motorcycle = motorcycles_2.pop()
print(motorcycles_2)
print(popped_motorcycle)
print('The last motorcycle I owned was a ' + popped_motorcycle.title() + '.')


# Popping Items from any Position in a List

motorcycles_3 = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles_3.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')