# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying
# they’ll have to wait for a table. Otherwise, report that their table is ready.


name = input("What is your name? ")
group = input("How many people are in your group? ")

group = int(group)

if group > 8:
    print("I'm sorry Mr. " + name + ", but your group will have to wait for a table.")
else:
    print("Mr. " + name, ", your table is ready!")