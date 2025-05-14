import random
print("Welcome to the Dice game!")
print("Roll the dice and get to 50 points to win!")

total_score = 0
target_score = 50

while total_score < target_score:
    input("Press Enter to roll the dice...")
    dice = random.randint(1, 6)
    total_score += dice
    print(f"You rolled a {dice}. Your total score is now {total_score}.")

print("Congratulations! You reached 50 points and won the game!")

               
