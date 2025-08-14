import random as r

easy_words = ["apple", "train", "tiger", "lotus", "coffee", "ship", "ball"]
medium_words = ["historical", "passport", "geography", "adventure", "schedule", "frozen", "advocate"]
hard_words = ["entreprenuer", "fluroescent", "bureaucracy", "handkercheif", "camouflage", "onomatopoeia", "fascinating"]

print("\n----- Welcome to the word guessing game -----")
print("Choose a difficulty level (Easy, Medium or Hard)")

level = input("\nEnter difficulty level: ").strip().capitalize()

if level == "Easy":
    secret = r.choice(easy_words)
elif level == "Medium":
    secret = r.choice(medium_words)
elif level == "Hard":
    secret = r.choice(hard_words)
else:
    print("Invalid choice! Defaulting to easy level...")
    secret = r.choice(easy_words)

attempts = 0
print("\nGuess the secret word! 👀")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"🎉 Congratulations! You guessed the word ({secret}) it in {attempts} attempts.")
        break

    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("\nHint: ", hint, "\n")
print("\n-----> GAME OVER!  <-----\n")