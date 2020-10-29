# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

prompt = "Chose a number and I will tell you if it is multiple of 10."
prompt += "\nNumber: "

number = input(prompt)
number = int(number)

if number % 10 == 0:
    print("The number " + str(number) + " is multiple of 10.")
else:
    print("The number " + str(number) + " isn't multiple of 10.")
