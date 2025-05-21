import random

def roll_dice(keep=None):
    """Roll five dice, keeping those in the 'keep' list."""
    if keep is None:
        keep = []
    return keep + [random.randint(1, 6) for _ in range(5 - len(keep))]

def display_dice(dice):
    print("Your dice:", " ".join(str(d) for d in dice))

def calculate_score(dice):
    # Simple scoring: sum of all dice
    return sum(dice)

num_players = int(input("Enter number of players: "))
scores = []

for player in range(1, num_players + 1):
    print(f"\n--- Player {player}'s turn ---")
    dice = roll_dice()
    for turn in range(3):
        print(f"\nRoll {turn + 1}:")
        display_dice(dice)
        if turn < 2:
            keep_input = input("Enter positions (1-5) of dice to keep, separated by spaces, or press Enter to re-roll all: ")
            if keep_input.strip() == "":
                dice = roll_dice()
            else:
                keep_indices = [int(i) - 1 for i in keep_input.split() if i.isdigit() and 1 <= int(i) <= 5]
                keep = [dice[i] for i in keep_indices]
                dice = roll_dice(keep)
        else:
            print("Final roll!")
    print("\nYour final dice:")
    display_dice(dice)
    score = calculate_score(dice)
    print(f"Player {player}'s score for this round is: {score}")
    scores.append(score)

print("\n--- Final Scores ---")
for i, score in enumerate(scores, 1):
    print(f"Player {i}: {score}")