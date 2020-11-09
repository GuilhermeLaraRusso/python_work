# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sandwich
# that is being ordered. Call the function three times, using a different number
# of arguments each time.

def make_sandwich(*items):
    print('\nO recheio do seu sanduiche é:')
    for item in items:
        print("-" + item)

make_sandwich('presunto')
make_sandwich('presunto', 'queijo', 'alface', 'tomate')
make_sandwich('bacon', 'ovos', 'hamburger', 'tomate', 'alface', 'queijo')