# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.

prompt = "\nFrom 0 to 2 = Free"
prompt += "\nFrom 3 to 12 = $10"
prompt += "\nAbove 12 = $15"
prompt += "\nWhat's your age? "

age = ""

while True:
    age = input(prompt)
    if str(age).lower() == 'quit':
        break
    else:
        age = int(age)

    if age < 3:
        price = "Free"
    elif age >= 3 and age < 12:
        price = "$10"
    else:
        price = "$15"
    print("\nThe price is " + price)


