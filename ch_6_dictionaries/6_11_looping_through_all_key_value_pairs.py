# Before we explore the different approaches to looping, let’s consider a
# new dictionary designed to store information about a user on a website.
# The following dictionary would store one person’s username, first name,
# and last name:


user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print('\nKey: ' + key)
    print("Value: " + value)