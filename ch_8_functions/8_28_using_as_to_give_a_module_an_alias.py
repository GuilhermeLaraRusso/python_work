# You can also provide an alias for a module name. Giving a module a short
# alias, like p for pizza, allows you to call the module’s functions more quickly.
# Calling p.make_pizza() is more concise than calling pizza.make_pizza():

import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# The general syntax for this approach is:

# import module_name as mn