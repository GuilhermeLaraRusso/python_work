# You can call a function as many times as needed. Describing a second, different
# pet requires just one more call to describe_pet():

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('dog', 'luna')
describe_pet('hamster', 'willie')


# Calling a function multiple times is a very efficient way to work. The
# code describing a pet is written once in the function. Then, anytime you
# want to describe a new pet, you call the function with the new pet’s information.
# Even if the code for describing a pet were to expand to ten lines,
# you could still describe a new pet in just one line by calling the function
# again.
# You can use as many positional arguments as you need in your functions.
# Python works through the arguments you provide when calling the
# function and matches each one with the corresponding parameter in
# the function’s definition.