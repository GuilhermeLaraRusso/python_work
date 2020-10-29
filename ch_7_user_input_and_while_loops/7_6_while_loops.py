# The for loop takes a collection of items and executes a block of code once
# for each item in the collection. In contrast, the while loop runs as long as,
# or while, a certain condition is true.

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


# In the first line, we start counting from 1 by setting the value of
# current_number to 1. The while loop is then set to keep running as long
# as the value of current_number is less than or equal to 5. The code inside
# the loop prints the value of current_number and then adds 1 to that value
# with current_number += 1. (The += operator is shorthand for current_number =
# current_number + 1.)

# Python repeats the loop as long as the condition current_number <= 5
# is true. Because 1 is less than 5, Python prints 1 and then adds 1, making
# the current number 2. Because 2 is less than 5, Python prints 2
# and adds 1 again, making the current number 3, and so on. Once the
# value of current_number is greater than 5, the loop stops running and the
# program ends