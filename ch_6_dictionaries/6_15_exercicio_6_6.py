# 6-6. Polling: Use the code in favorite_languages.py (page 104).
# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

names = ['jen', 'sarah', 'guilherme', 'lorenzo', 'thais']

for name in names:
    if name not in favorite_languages:
        print(name.title() + ", you need to take the poll!")
    else:
        print(name.title() + ", thank you for taking the poll!")
