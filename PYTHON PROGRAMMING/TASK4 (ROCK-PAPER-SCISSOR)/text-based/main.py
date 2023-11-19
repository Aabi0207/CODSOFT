# Import the random package to randomize the computers choices
import random

# Import the ASCII arts of Rock, Paper and Scissor form the ascii file
from ascii import *


def print_choice(player, choice):
    """
        This function prints the users and the computers chioices
    """

    if choice == 1:
        print(f"{player} choice is :\n{rock}")
    elif choice == 2:
        print(f"{player} choice is :\n{paper}")
    elif choice == 3:
        print(f"{player} choice is: \n{scissor}")


def state_winner(your_choice, comp_choice):
    """
        This function stats the winner according to the users and computers choices
    """
    if your_choice == comp_choice:
        print("It's a draw! 🤷‍♂️")
    elif your_choice == 1 and comp_choice == 3:
        print("Congratulations! You won the game. 🏆")
    elif your_choice == 2 and comp_choice == 1:
        print("Congratulations! You won the game. 🏆")
    elif your_choice == 3 and comp_choice == 2:
        print("Congratulations! You won the game. 🏆")
    else:
        print("Computer won the game! Better Luck next Time! 😉")

def play_game():
    """
        This function starts the game and controls the functionality to make the choices.
    """

    is_correct_choice = True
    while is_correct_choice:
        your_choice = int(input("Choose one digit from the below:\n1. Rock\n2. Paper\n3. Scissor\n"))
        if 0 > your_choice > 4:
            print("Invalid Input! Please try again.")
        else:
            is_correct_choice = False

    print_choice("Your", your_choice)

    computer_choice = random.randint(1, 3)
    print_choice("Computers", computer_choice)

    state_winner(your_choice, computer_choice)

play_game()

# This while loop asks the user after finishing one game do they want to play it again
while True:
    play_again = input("Do you want to play again? Type 'y' for yes and 'n' for no.")
    if play_again == "y":
        play_game()
    else:
        break
