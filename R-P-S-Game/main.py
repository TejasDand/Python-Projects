# Rock, Paper and Scissor
from random import choice

ROCK = 'R'
PAPER = 'P'
SCISSOR = 'S'

emojis = {ROCK : '🪨', PAPER : '📄', SCISSOR : '✂️'}
choices = tuple(emojis.keys())


# Gets input from the user
def get_user_input():
    while True:
        user_choice = input("\nRock, Paper or Scissor? (R/P/S): ").upper()

        if user_choice in choices:
            return user_choice
        else:
            print("Invalid Choice! Please enter from R/P/S.")


# Prints choices of computer and user
def choices_display(user_choice, computer_choice):
    print(f"You chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")


# Logic of Winning Rock, Paper & Scissor Game
def determine_winning(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")

    elif(
        (user_choice == ROCK and computer_choice == SCISSOR) or
        (user_choice == SCISSOR and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)
    ):
        print("\nYou Win! 🎉")
    
    else:
        print("\nYou Lose! ❌")


# Play Game function
def play_Game():
    while True:
        user_input = get_user_input()
        computer_choices = choice(choices)

        choices_display(user_input, computer_choices)
        determine_winning(user_input, computer_choices)

        should_continue = input("\nContinue? (Y/N): ").upper()

        if should_continue == "N":
            break


if __name__ == "__main__":
    play_Game()