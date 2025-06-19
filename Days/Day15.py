# Virtual Coffee Machine
# 3 Drink, Esspresso, Latte and Cappaccino
# Coin Operated
# Resources Check
menu = {
    "espresso": {
        "ingredients": {
            "water": 100,
            "milk": 0,
            "coffee": 50
        },
        "cost": 2.5
    },
    "latte":{
        "ingredients":{
            "water": 100,
            "milk": 100,
            "coffee": 50,
        },
        "cost": 3.5
    },
    "cappaccino": {
        "ingredients":{
            "water": 50,
            "milk": 150,
            "coffee": 50,
        },
        "cost": 5
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print("Caffine Addicts Super Fix System\n"
      "Please Enter your selection")

# TODO: 1. Print report on Machine Resources
is_on = True

while is_on:
    choice = input("Please make a selection: Espresso / Latte / Cappaccino")
    if choice =="off":
        is_on = False
    elif choice == "report":
        print(f"Water:  {resources['water']}ml")
        print(f"Milk: {resources ['milk']}ml")
        print(f"Coffee:{resources ['coffee']}g")
