# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value
# that’s returned.

def city_country(city, country):
    """Return a city and it's country name"""
    full_city = city + ", " + country
    return full_city.title()

print(city_country('santiago', 'chile'))
print(city_country('belo horizonte', 'brasil'))
print(city_country('new york', 'usa'))