# The previous example involved storing different kinds of information about
# one object, an alien in a game. You can also use a dictionary to store one
# kind of information about many objects.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".\n")

# Utilizando o loop para percorrer todos os valores - parte 6_11

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title())