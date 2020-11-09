# Now we’ll make a separate file called making_pizzas.py in the same
# directory as pizza.py. This file imports the module we just created and then
# makes two calls to make_pizza():

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'wxtra cheese')


# When Python reads this file, the line import pizza tells Python to
# open the file pizza.py and copy all the functions from it into this program.
# You don’t actually see code being copied between files because Python
# copies the code behind the scenes as the program runs. All you need
# to know is that any function defined in pizza.py will now be available in
# making_pizzas.py.
# To call a function from an imported module, enter the name of
# the module you imported, pizza, followed by the name of the function,
# make_pizza(), separated by a dot u. This code produces the same output
# as the original program that didn’t import a module:|