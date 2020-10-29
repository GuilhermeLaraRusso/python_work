# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

prompt = "\nFrom 0 to 2 = Free"
prompt += "\nFrom 3 to 12 = $10"
prompt += "\nAbove 12 = $15"
prompt += "\nWhat's your age? "

age = ""

while age != "quit":
    age = input(prompt)
    age = int(age)
    if age < 3:
        price = "Free"
    elif age >= 3 and age < 12:
        price = "$10"
    else:
        price = "$15"
    print("\nThe price is " + price)