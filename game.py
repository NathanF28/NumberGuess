import random

# Display game intro
print("#" * 70)
print("🎮 Welcome to the Number Guessing Game! 🎮")
print("I'm thinking of a number between 1 and 100.")
print("\nChoose difficulty level:")
print("1. Easy    (10 chances)")
print("2. Medium  (5 chances)")
print("3. Hard    (3 chances)")

# Generate random number
num = random.randint(1, 100)

# Get difficulty level
while True:
    try:
        choice = int(input("\nEnter your choice (1-3): "))
        if choice in [1, 2, 3]:
            break
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")
    except ValueError:
        print("❌ Invalid input! Please enter a number.")

# Set number of chances based on difficulty
chances = {1: 10, 2: 5, 3: 3}[choice]

# Game loop
score = 0
while chances > 0:
    try:
        guess = int(input("\nEnter your guess: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        continue

    score += 1
    if guess > num:
        print("🔽 Too high! Try a lower number.")
    elif guess < num:
        print("🔼 Too low! Try a higher number.")
    else:
        print(f"🎉 Congratulations! You found the number in {score} tries.")
        break

    chances -= 1
    print(f"⚠️ Remaining chances: {chances}")

# If player runs out of chances
if chances == 0:
    print(f"💀 Game Over! The correct number was {num}. Better luck next time!")
