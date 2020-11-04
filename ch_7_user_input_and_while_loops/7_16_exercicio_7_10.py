# 7-10. Dream Vacation: Write a program that polls users about their dream
# vacation. Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.

dream_vacation = {}

poll = True

while poll:
    name = input("\nWhat's your name? ")
    place = input("Where would you like to visit? ")

    dream_vacation[name] = place

    repeat = input("would you like to continue the poll? (yes/no) ")
    if repeat.lower() == "no":
        poll = False


print("\n--- Poll Result ---")
for name, place in dream_vacation.items():
    print(name + " would like to visit " + place)