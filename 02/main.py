import os

shape_score = {
    "A": 1,
    "B": 2,
    "C": 3
}

outcome_score = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

outcome_map = {
    # rock
    "A": {
        # lose - scissors
        "X": "C",
        # draw - rock
        "Y": "A",
        # win - paper
        "Z": "B"
    },
    # paper
    "B": {
        # lose - rock
        "X": "A",
        # draw - paper
        "Y": "B",
        # win - scissors
        "Z": "C"
    },
    # scissors
    "C": {
        # lose - paper
        "X": "B",
        # draw - scissors
        "Y": "C",
        # win - rock
        "Z": "A"
    }
}

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
    strategy_guide = f.read().splitlines()

total_score = 0

for turn in strategy_guide:
    opponent_move, desired_outcome = turn.split(" ")

    player_choice = outcome_map[opponent_move][desired_outcome]

    shape = shape_score[player_choice]
    outcome = outcome_score[desired_outcome]
    round_score = (shape + outcome)
    total_score += round_score

print(f"total score: {total_score}")
