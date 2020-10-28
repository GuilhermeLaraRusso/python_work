# The keys() method is useful when you don’t need to work with all of the
# values in a dictionary. Let’s loop through the favorite_languages dictionary
# and print the names of everyone who took the poll:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())


# Looping through the keys is actually the default behavior when looping
# through a dictionary, so this code would have exactly the same output if you
# wrote . . .
# You can choose to use the keys() method explicitly if it makes your code
# easier to read, or you can omit it if you wish.

# You can access the value associated with any key you care about inside
# the loop by using the current key. Let’s print a message to a couple of friends
# about the languages they chose. We’ll loop through the names in the dictionary
# as we did previously, but when the name matches one of our friends, we’ll
# display a message about their favorite language:

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

# You can also use the keys() method to find out if a particular person
# was polled. This time, let’s find out if Erin took the poll:

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")