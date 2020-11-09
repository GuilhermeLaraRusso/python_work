# Sometimes you won’t know ahead of time how many arguments a function
# needs to accept. Fortunately, Python allows a function to collect an arbitrary
# number of arguments from the calling statement.
# For example, consider a function that builds a pizza. It needs to accept a
# number of toppings, but you can’t know ahead of time how many toppings
# a person will want. The function in the following example has one parameter,
# *toppings, but this parameter collects as many arguments as the calling
# line provides:

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')