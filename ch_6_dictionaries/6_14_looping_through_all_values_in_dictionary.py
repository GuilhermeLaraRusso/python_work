# If you are primarily interested in the values that a dictionary contains,
# you can use the values() method to return a list of values without any keys.
# For example, say we simply want a list of all languages chosen in our programming
# language poll without the name of the person who chose each
# language:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
print("\n")

# This approach pulls all the values from the dictionary without checking
# for repeats. That might work fine with a small number of values, but in a
# poll with a large number of respondents, this would result in a very repetitive
# list. To see each language chosen without repetition, we can use a set.
# A set is similar to a list except that each item in the set must be unique:

for language in set(favorite_languages.values()):
    print(language.title())

# When you wrap set() around a list that contains duplicate items, Python
# identifies the unique items in the list and builds a set from those items.