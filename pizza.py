# Banner
print("Welcome to the big slice pizza shop!")

size = input("What size of pizza S, M, or L? ")
pepperoni = input("Do you want extra pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")

# How much do they payL
total = 0
if size == "S":
    total += 15
elif size == "M":
    total += 20
elif size == "L":
    total += 25
else:
    print("Incorrect Pizza size entered")

# Pepperoni addition
if pepperoni == "Y":
    if size == "S":
        total += 2
    else:
        total += 3

# Extra cheese
if extra_cheese == "Y":
    total += 5

# Give Customer total charges
print(f" You ordered a {size} pizza, you choose {pepperoni} extra pepperoni, and {extra_cheese} extra cheese, this comes to ${total}")
