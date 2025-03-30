# Rock Paper Scissors Game
import random

user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
if user_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice. Please choose Rock, Paper, or Scissors.")
else:
    print(f"You chose: {user_choice}")
# Computer's choice is random
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
if user_choice == "rock" and computer_choice == "scissors":
    print("You win! Rock beats scissors.")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win! Scissors beat paper.")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win! Paper beats rock.")
elif user_choice == computer_choice:
    print("It's a tie!")
else:
    str(print(f"You lose! " + {computer_choice} + " beats " + {user_choice} + "."))
