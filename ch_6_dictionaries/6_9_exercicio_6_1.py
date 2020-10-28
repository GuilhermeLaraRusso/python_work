# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.

person = {'first_name': 'Lorenzo', 'last_name': 'Russo', 'age': 6, 'city': 'Belo Horizonte'}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

print(person['first_name'] + " " + person['last_name'] + " tem " +
      str(person['age']) + " anos e mora em " + person['city'])