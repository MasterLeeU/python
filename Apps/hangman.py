#Hangman Game
# Importing the random module
import random

#Generating a random word from a list
def get_random_word():
    words = ["British Columbia", "Alberta", "Saskatchewan", "Manitoba", "Ontario", "Quebec", "Newfoundland", "Labrador", "Nova Scotia", "New Brunswick", "Prince Edward Island"]
    return random.choice(words).lower() 

#Function to display the current state of the word
def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

#Function to check if the game is over
def is_game_over(word, guessed_letters, attempts):
    if set(word).issubset(set(guessed_letters)):
        print("Congratulations! You've guessed the word:", word)
        return True
    elif attempts <= 0:
        print("Game over! The word was:", word)
        return True
    return False

#Main function to run the game
def hangman():
    word = get_random_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word:")
    
    while True:
        print(display_word(word, guessed_letters))
        print("Attempts left:", attempts)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess!")

        if is_game_over(word, guessed_letters, attempts):
            break

#Calling the main function to start the game
if __name__ == "__main__":
    hangman()

# This code implements a simple Hangman game where the player has to guess a randomly chosen word letter by letter.
# The player has a limited number of incorrect guesses before the game ends.
# The game provides feedback on the current state of the word and the number of attempts left.
# The player can only input a single letter at a time, and the game checks for valid input.
# The game continues until the player either guesses the word or runs out of attempts.
# The code is structured into functions for better organization and readability.
# The get_random_word function selects a random word from a predefined list.
# The display_word function shows the current state of the word with guessed letters revealed.
# The is_game_over function checks if the game has been won or lost.
# The hangman function contains the main game loop, handling user input and game logic.
# The game is initiated by calling the hangman function when the script is run.
# The code is written in Python and is designed to be run in a console or terminal.
# The game can be easily modified by changing the list of words or adjusting the number of attempts.
# The code is simple and straightforward, making it easy to understand for beginners.
# The game can be enhanced by adding features like hints, difficulty levels, or a graphical interface.
# The code is a good example of using functions, loops, and conditionals in Python.
# The game can be played by running the script in a Python environment.
# The game can be improved by adding more words to the list or implementing a scoring system.
# The game can be played by multiple players by modifying the code to allow for player input.
# The game can be made more challenging by increasing the number of attempts or using longer words.