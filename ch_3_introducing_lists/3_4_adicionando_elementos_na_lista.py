# The simplest way to add a new element to a list is to append the item to the
# list. When you append an item to a list, the new element is added to the end
# of the list. Using the same list we had in the previous example, we’ll add the
# new element 'ducati' to the end of the list:


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)




# The append() method makes it easy to build lists dynamically. For
# example, you can start with an empty list and then add items to the list
# using a series of append() statements. Using an empty list, let’s add the elements
# 'honda', 'yamaha', and 'suzuki' to the list:


motorcycles_vazia = []
print(motorcycles_vazia)

motorcycles_vazia.append('honda')
motorcycles_vazia.append('yamaha')
motorcycles_vazia.append('suzuki')

print(motorcycles_vazia)