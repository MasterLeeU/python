# Roller Coaster
print("Welcome to the Cosmic Coaster!")

# Height Verification
height = int(input("What is your height in cm? "))
total = 0

if height >= 120:
    print("Welcome aboard the Cosmic Coster!")

    # Age Verification
    age = int(input("Enter your Age? "))
    if age < 12:
        total = 5
        print("Child ticket are $5.")
    elif age <= 18:
        total = 10
        print("Youth tickets are $10.")
    elif age >= 45 and age <=55:
        print("You get to ride for Free")
    else:
        total = 15
        print("Adult tickets are $15.")
    
    # Photo Op 
    photo_op = input("Would you like a photo? Type y for Yes and n for No.")
    if photo_op == "y":
        # Add $3 to total
        total += 3
    print(f"Your Total is {total}")

else:
    print("Wah wahhh, Hey Shorty, maybe next time.")
