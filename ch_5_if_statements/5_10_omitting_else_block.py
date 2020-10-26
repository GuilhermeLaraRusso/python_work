# Python does not require an else block at the end of an if-elif chain. Sometimes
# an else block is useful; sometimes it is clearer to use an additional
# elif statement that catches the specific condition of interest:

age = 70

if age < 4:
    price = 0
elif age <18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")