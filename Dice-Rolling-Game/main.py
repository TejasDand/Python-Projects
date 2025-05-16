# Dice-Rolling-Game _ Project-1
from random import choice

dice = [1, 2, 3, 4, 5, 6]
roll_count = 0  # Counter to track number of rolls

print("\n🎲 Welcome to the Dice Rolling Game!")

# Ask how many dice the user wants to roll

while True:
    roll_Dice = input("\nRoll the dice? (y/n): ").title()
    
    if roll_Dice == "Y":
        num_dice = int(input("How many dice do you want to roll? "))
    
        roll_count += 1  # Increment roll counter
        print("\nYou rolled: ", end="")
        
        for _ in range(num_dice):
            print(f"{choice(dice)} ", end="")
        
        print(f"\n🎯 Total rolls so far: {roll_count}\n")

    elif roll_Dice == "N":
        print(f"\nThanks for playing! 🎉 You rolled the dice {roll_count} time(s).")
        break

    else:
        print("❗ Invalid Choice! Please enter Y or N.")