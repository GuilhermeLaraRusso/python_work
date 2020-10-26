# Often, you’ll need to test more than two possible situations, and to evaluate
# these you can use Python’s if-elif-else syntax. Python executes only one
# block in an if-elif-else chain. It runs each conditional test in order until
# one passes. When a test passes, the code following that test is executed and
# Python skips the rest of the tests.

# For example, consider an amusement park that charges different rates for
# different age groups:
# • Admission for anyone under age 4 is free.
# • Admission for anyone between the ages of 4 and 18 is $5.
# • Admission for anyone age 18 or older is $10.

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")
