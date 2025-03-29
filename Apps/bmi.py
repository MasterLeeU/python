# Body Mass Index Calculator
print("BMI Calculator \n"
      "Be sure to enter your values in Metric")

#User Variables
user_height = float(input("What is your height in (m)? \n"))
user_weight = float(input("What is your weight in (kg)? \n"))

# write your code here
bmi = float(user_weight/(user_height**2))
print(f"Your BMI is {bmi}")
if bmi < 18.5:
    print(f"Your BMI indicates you are under weight range")
elif bmi <=24.5:
    print("Your BMI indicates you are in the normal weight range")
else:
    print("Your BMI indicates you are over weight range")
