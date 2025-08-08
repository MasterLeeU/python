print("Welcome to the big slice pizza shop!") # Banner Title

size = input("What size of pizza S, M, or L? ") # Gets size of Pizza
pepperoni = input("Do you want extra pepperoni? Y or N? ") # Offer Pepproni
extra_cheese = input("Do you want extra cheese? Y or N? ") # Offer Extra Cheese

total = 0 # Calculate total cost of Pizza
if size == "S":
    total += 15
elif size == "M":
    total += 20
elif size == "L":
    total += 25
else:
    print("Incorrect Pizza size entered")

if pepperoni == "Y": # Add additional cost for pepperoni
    if size == "S":
        total += 2
    else:
        total += 3

if extra_cheese == "Y": # Add additional cost for extra cheese
    total += 5

# Give Customer total charges
print(f" You ordered a {size} pizza, you choose {pepperoni} extra pepperoni, and {extra_cheese} extra cheese, this comes to ${total}")
