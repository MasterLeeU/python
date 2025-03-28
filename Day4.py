# Randomization
import random

# total_number = input(int("Enter your total number of Winners?"))
# random_integer = random.randint(1, total_number)
# print(random_integer)

#Coin Flip
# coin_flip = random.randint(1, 2)
# if coin_flip == 1:
#     print("Heads")
# else:
#     print("Tails")

# Friend List Randomizer
# friends = ["Lee", "Dean", "Francis", "Matt", "Remith"]
# print(random.choice(friends))

# random_index = random.randint(0, 4)
# print(friends[random_index])
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])
