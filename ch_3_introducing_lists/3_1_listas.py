# A list is a collection of items in a particular order. You can make a list that
# includes the letters of the alphabet, the digits from 0–9, or the names of
# all the people in your family. You can put anything you want into a list, and
# 38 Chapter 3
# the items in your list don’t have to be related in any particular way. Because
# a list usually contains more than one element, it’s a good idea to make the
# name of your list plural, such as letters, digits, or names.


# In Python, square brackets ([]) indicate a list, and individual elements
# in the list are separated by commas. Here’s a simple example of a list that
# contains a few kinds of bicycles:

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)


# Para acessar apenas um elemento da lista, basta colocar a posição do elemento dentro do colchetes
print(bicycles[0])

print(bicycles[0].title())


# Para acessar o último elemento da lista, é utilizado [-1]
print(bicycles[-1])

# Para acessar o antepenúltimo item da lista, utiliza [-2], depois [-3] e assim sucessivamente


message = 'My first bicycle was a ' + bicycles[0].title() +'.'
print(message)



