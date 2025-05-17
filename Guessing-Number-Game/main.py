# Guessing-Number-Game _ Project-2
from random import randint

print("\n🎯 Welcome to the Number Guessing Game!")

# Get the guessing range from user
num1 = int(input("From which number do you want to start guessing? "))
num2 = int(input("Up to which number do you want to guess? "))

random_number = randint(num1, num2)
guesses = 10  # Set maximum attempts

while guesses > 0:
    
    try:
        guess = int(input(f"\nGuess the number ({guesses} attempts left): "))

        if guess == random_number:
            print(f"\n🎉 Congratulations! You guessed the number correctly in {guesses} attempts.")
            break
        
        elif guess > random_number:
            print("🔺 Too High! Try Again.")
        else:
            print("🔻 Too Low! Try Again.")

        guesses -= 1  # Decrease attempt after each wrong guess

    except ValueError:
        print("❗ Please enter a valid number!")


if guesses == 0:
    print(f"\n❌ You ran out of attempts! The number was: {random_number}")