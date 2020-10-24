# If you want to make a list of numbers, you can convert the results of range()
# directly into a list using the list() function.
# When you wrap list() around a
# call to the range() function, the output will be a list of numbers.

numbers = list(range(1,6))
print(numbers)


# We can also use the range() function to tell Python to skip numbers
# in a given range. For example, here’s how we would list the even numbers
# between 1 and 10:

even_numbers = list(range(2,11,2))
print(even_numbers)


# You can create almost any set of numbers you want to using the range()
# function. For example, consider how you might make a list of the first 10
# square numbers (that is, the square of each integer from 1 through 10). In
# Python, two asterisks (**) represent exponents. Here’s how you might put
# the first 10 square numbers into a list:

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)