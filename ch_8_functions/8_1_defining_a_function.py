# In this chapter you’ll learn to write
# functions, which are named blocks of code
# that are designed to do one specific job.
# When you want to perform a particular task
# that you’ve defined in a function, you call the name
# of the function responsible for it. If you need to
# perform that task multiple times throughout your program, you don’t
# need to type all the code for the same task again and again; you just call
# the function dedicated to handling that task, and the call tells Python to
# run the code inside the function. You’ll find that using functions makes
# your programs easier to write, read, test, and fix.

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()



#
# This example shows the simplest structure of a function. The line at u
# uses the keyword def to inform Python that you’re defining a function. This
# is the function definition, which tells Python the name of the function and, if
# applicable, what kind of information the function needs to do its job. The
# parentheses hold that information. In this case, the name of the function
# is greet_user(), and it needs no information to do its job, so its parentheses
# are empty. (Even so, the parentheses are required.) Finally, the definition
# ends in a colon.
# Any indented lines that follow def greet_user(): make up the body of
# the function. The text at v is a comment called a docstring, which describes
# what the function does. Docstrings are enclosed in triple quotes, which
# Python looks for when it generates documentation for the functions in your
# programs.
# The line print("Hello!")  is the only line of actual code in the body
# of this function, so greet_user() has just one job: print("Hello!").
# When you want to use this function, you call it. A function call tells
# Python to execute the code in the function. To call a function, you write
# the name of the function, followed by any necessary information in parentheses,
# as shown at x. Because no information is needed here, calling our
# function is as simple as entering greet_user(). As expected, it prints Hello!: