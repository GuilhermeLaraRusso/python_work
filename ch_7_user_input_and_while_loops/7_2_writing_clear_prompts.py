# Each time you use the input() function, you should include a clear, easy-tofollow
# prompt that tells the user exactly what kind of information you’re
# looking for. Any statement that tells the user what to enter should work. For

# example:

# name = input("Please enter you name: ")
# print("Hello, " + name + "!")


# Sometimes you’ll want to write a prompt that’s longer than one line. For
# example, you might want to tell the user why you’re asking for certain input.
# User Input and while Loops 119
# You can store your prompt in a variable and pass that variable to the input()
# function. This allows you to build your prompt over several lines, then write
# a clean input() statement.

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhait is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")
