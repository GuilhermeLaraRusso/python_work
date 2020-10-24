# The approach described earlier for generating the list squares consisted of
# using three or four lines of code. A list comprehension allows you to generate
# this same list in just one line of code.


squares = [value**2 for value in range(1,11)]
print(squares)