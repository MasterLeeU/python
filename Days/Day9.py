# Day 9 Dicitionaries and Nesting

# Dictionaries
# A dictionary is a collection of key-value pairs
# A dictionary is created using curly braces {} or the dict() function
# A dictionary is unordered, mutable, and indexed
# A dictionary can contain any data type as a key or value.
# A dictionary can be nested, meaning a dictionary can contain other dictionaries as values

# Example of a dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

# Adding new items to a dictionary
programming_dictionary["New Key"] = "New Value"
print(programming_dictionary)

# Creating an empty dictionary
# empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Looping through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


# Nesting
# A dictionary can contain other dictionaries as values
# Example of a nested dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
}

# print Lille
print(travel_log["France"]["cities_visited"][1])

# Nesting a dictionary in a dictionary
travel_log["Italy"] = {
    "cities_visited": ["Rome", "Venice", "Florence"],
    "total_visits": 3,
}

# Looping through a nested dictionary
for country, info in travel_log.items():
    print(f"{country}: {info['total_visits']} visits")
    print("Cities visited:")
    for city in info["cities_visited"]:
        print(city)

# Example of a nested dictionary
def add_new_country(country, cities_visited, total_visits):
    travel_log[country] = {
        "cities_visited": cities_visited,
        "total_visits": total_visits,
    }
# Example of a nested dictionary
add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)
print(travel_log)

print(travel_log["Germany"]["cities_visited"][2])
