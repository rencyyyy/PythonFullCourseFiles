# Dictionary Comprehension - create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key, value) in iterables}
# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: (if/else) for (key, value) in iterable}
# dictionary = {key: function(value) for (key, value) in iterable}

#-----------------------------------------------------------------------------------------------------------------------
print("\nDictionary Comprehension Normal")
# dictionary = {key: expression for (key, value) in iterables}

cities_in_F = {'Mariveles': 69, "Balanga": 72, "San Fernando": 60, "Samal":81}

cities_in_C = {key:round((value-32)*(5/9))for(key,value) in cities_in_F.items()}
print(cities_in_C)


#-----------------------------------------------------------------------------------------------------------------------
print("\nDictionary Comprehension with condition")
# dictionary = {key: expression for (key, value) in iterable}

weather = {"Mariveles":"sunny", "Baguio":"snowing", "Davao":"sunny", "New York":"cloudy"}

sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
print(sunny_weather)

#-----------------------------------------------------------------------------------------------------------------------
print("\nDictionary Comprehension with condition")
# dictionary = {key: (if/else) for (key, value) in iterable}

city_temp = {'Mariveles': 69, "Balanga": 72, "San Fernando": 60, "Samal":39}

desc_city = {key: ("Warm" if value >= 40 else "Cold") for (key,value) in city_temp.items()}
print(desc_city)

#-----------------------------------------------------------------------------------------------------------------------
print("\nDictionary Comprehension with function")
# dictionary = {key: function(value) for (key, value) in iterable}
def check_desc(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

temp_city = {'Mariveles': 39, "Balanga": 40, "San Fernando": 69, "Samal":70}
description_city = {key: check_desc(value) for (key,value) in temp_city.items()}
print(description_city)