# numbers = ["0","1","2","3","4","5","6","7","8","9"]
# lower_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","w","x","y","z"]
# upper_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","W","X","Y","Z"]

#Range Function
total = 0 
for number in range (1, 101):
    total += number
print(total)

for number in range(1, 101):
    if number % 3 ==0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
         print ("fizz")
    elif number % 5 == 0:
         print ("buzz")
    else:
        print(number)
