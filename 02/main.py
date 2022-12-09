# First column - opponent's move
# A = rock
# B = paper
# C = scissors

# Second column - what you should play in response
# X = rock
# Y = paper
# Z = scissors

# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)

import os

shape_score = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

outcome_score = {
    "loss": 0,
    "draw": 3,
    "win": 6
}

move_map = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
    strategy_guide = f.read().splitlines()

total_score = 0

for turn in strategy_guide:
    opponent_move, best_response = turn.split(" ")

    if best_response == move_map[opponent_move]:
        total_score += (3 + shape_score[best_response])
        continue

    if opponent_move == "A":
        if best_response == "Y":
            total_score += (6 + shape_score[best_response])

        if best_response == "Z":
            total_score += (0 + shape_score[best_response])
        continue

    if opponent_move == "B":
        if best_response == "Z":
            total_score += (6 + shape_score[best_response])

        if best_response == "X":
            total_score += (0 + shape_score[best_response])
        continue

    if opponent_move == "C":
        if best_response == "X":
            total_score += (6 + shape_score[best_response])

        if best_response == "Y":
            total_score += (0 + shape_score[best_response])
        continue

print(f"total score: {total_score}")
