# Functions
#def greet():
#    print("Hello ")
#    print("How do you do?")
#    print("Isn't the weather nice today?")
#greet()

#Function that allows an input
#def greet_with_name(name):
#    print(f"Hello " + {name})
#    print(f"How do you do " + {name} + "?")
#    print(f"Isn't the weather nice today " + {name} + "?")
#greet_with_name("John")


#def life_in_weeks(age):
#    days = age * 365
#    weeks = days / 7
#    months = days / 30.44
#    print(f"You have {days} days, {weeks} weeks, and {months} months left to live.")
#    return days, weeks, months
#life_in_weeks(25)

#def greet_with(name, location):
#    print(f"Hello {name}")
#    print(f"How do you do {name}?")
#    print(f"Isn't the weather nice today in {location}?")
#greet_with("John", "New York")

def calculate_love_score(name1, name2):
    # Convert names to lowercase and remove spaces
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    # Combine names
    combined_names = name1 + name2

    # Count the occurrences of each letter in the combined names
    letter_count = {}
    for letter in combined_names:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    # Calculate the love score based on the counts of letters
    love_score = sum(letter_count.values()) % 100

    return love_score
# Get user input for names
name1 = input("Enter your name: ")
name2 = input("Enter your crush's name: ")
# Calculate the love score
love_score = calculate_love_score(name1, name2)
# Display the love score
print(f"Your love score is: {love_score}%")
# This code calculates a "love score" based on the names of two people.
# It combines the names, counts the occurrences of each letter, and calculates a score based on those counts.
# The score is then displayed as a percentage.
