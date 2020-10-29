# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.

cities = {
    'belo horizonte': {
        'country': 'brazil',
        'population': '1440000',
        'fact': 'good horizon',
    },

    'paris': {
        'country': 'france',
        'population': '2161000',
        'fact': 'omelete au fromage',
    },

    'new york':{
        'country': 'usa',
        'population': '8400000',
        'fact': 'central park'
    },
}

for city, data in cities.items():
    print(city.title() + ':')
    for info, dado in data.items():
        print("\t" + info.title() + ": " + dado.title())


