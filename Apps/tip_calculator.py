# Tip Calulator

# Banner
print("Welcome to the tip calulator!")

# collect inputs
bill = float(input("How much was the total bill? \n"))
tip = int(input("How much would you like to tip? 10, 15, 18, or 20? \n "))
split = int(input("How many people will the bill be split? \n"))

# create the calculations
total_with_tip = tip / 100 * bill + bill
total_tip_amount = (bill * (tip/100))
bill_per_person = round(total_with_tip / split, 2)

print(f"The total bill with tip is {total_with_tip}\n The total tip ammount was {total_tip_amount} \n The total split for each {bill_per_person}")