# Removing an Item by Value

# Sometimes you won’t know the position of the value you want to remove
# from a list. If you only know the value of the item you want to remove, you
# can use the remove() method.

# For example, let’s say we want to remove the value 'ducati' from the list of
# motorcycles.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# motorcycles.remove('ducati')
# print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA ' + too_expensive.title() + ' is too expensive for me.')

