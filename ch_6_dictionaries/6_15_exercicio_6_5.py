# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.

# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.

# • Use a loop to print the name of each river included in the dictionary.

# • Use a loop to print the name of each country included in the dictionary.

rivers = {'nilo': 'egito',
          'amazonas': 'brasil',
          'sao francisco': 'minas gerais',
          }

for rio in rivers.keys():
    print("O " + rio.title() + " passa por " + rivers[rio].title())

for rio in rivers.keys():
    print(rio.title())

for local in rivers.values():
    print(local.title())