# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

prompt = "\nChoose a topping for your pizza: "
prompt += "\nType 'quit' to leave. "

topping = ""

while topping.lower() != 'quit':
    topping = input(prompt)
    if topping.lower() != 'quit':
        print("Adding " + topping.title() + " to your pizza!")
