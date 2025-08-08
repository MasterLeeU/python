# Python Password Generator
import random
numbers = ['0','1','2','3','4','5','6','7','8','9']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n''o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X','Y','Z']
symbols = ['`','~','!','@','#','$','%','^','&','*','(',')','-','=','_','+']

print("Welcome to a Random Password Generator")
num_letters = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like to your password?\n"))

pass_list= []
range(0, 100)
for char in range(0, num_letters):
     pass_list.append(random.choice(letters))

for char in range(0, num_numbers):
     pass_list.append(random.choice(numbers))

for char in range(0, num_symbols):
    pass_list.append(random.choice(symbols))
random.shuffle(pass_list)

password = ""
for char in pass_list:
     password += char

print(f"Your password is\n {password}")
