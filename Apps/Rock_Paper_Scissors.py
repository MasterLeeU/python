# Rock Paper Scissors Game
import random

user_choice = input("Enter Rock, Paper, or Scissors: ")
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
    print(f"You lose! " + {computer_choice} + " beats " + {user_choice} + ".")
