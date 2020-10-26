# The simplest kind of if statement has one test and one action:

# if condicional_test:
#     do something

# You can put any conditional test in the first line and just about any
# action in the indented block following the test. If the conditional test
# evaluates to True, Python executes the code following the if statement.
# If the test evaluates to False, Python ignores the code following the if
# statement.
# Let’s say we have a variable representing a person’s age, and we want to
# know if that person is old enough to vote. The following code tests whether
# the person can vote:

age = 19
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
