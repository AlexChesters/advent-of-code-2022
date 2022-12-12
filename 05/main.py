import os
import re
import json

import numpy

with open(os.path.join(os.path.dirname(__file__), "starting_stacks.txt"), "r", encoding="utf-8") as f:
    starting_stacks = f.read().rstrip()

with open(os.path.join(os.path.dirname(__file__), "rearrangement_procedure.txt"), "r", encoding="utf-8") as f:
    rearrangement_procedure = f.read().rstrip().split("\n")

procedure_regex = "move (?P<crate_count>[0-9]+) from (?P<starting_column>[0-9]+) to (?P<destination_column>[0-9]+)"

stacks = starting_stacks.split("\n")

grid = [[] for _ in range(8)]

for idx, row in enumerate(stacks):
    grid_row = []

    parsed_row = re.split("[\s]+", row)

    for item in re.split("[\s]+", row):
        if item:
            grid_row.append(item)

    grid[idx].extend(grid_row)

grid = list(numpy.transpose(grid))

for idx, column in enumerate(grid):
    grid[idx] = column.tolist()

for procedure in rearrangement_procedure:
    print(f"starting grid: {json.dumps(grid, indent=2)}")

    match = re.match(procedure_regex, procedure)
    crate_count = int(match.group("crate_count"))
    starting_column_index = int(match.group("starting_column")) - 1
    destination_column_index = int(match.group("destination_column")) - 1

    print(f"moving {crate_count} crates from column index {starting_column_index} to column index {destination_column_index}")

    starting_column = grid[starting_column_index]
    destination_column = grid[destination_column_index]

    print(f"starting column: {starting_column}")
    print(f"destination column: {destination_column}")

    moved_crate_count = 0
    crate_index = 0
    crates_to_move = []

    while crate_count > moved_crate_count:
        crate_to_move = starting_column[crate_index]

        if crate_to_move == "[0]":
            crate_index += 1
            continue

        starting_column[crate_index] = "[0]"
        crates_to_move.append(crate_to_move)
        moved_crate_count += 1
        crate_index += 1

    print(f"crates to move: {crates_to_move}")

    destination_column[:0] = crates_to_move

    grid[starting_column_index] = starting_column
    grid[destination_column_index] = destination_column

    print(f"starting column: {starting_column}")
    print(f"destination column: {destination_column}")

    print(f"new grid: {json.dumps(grid, indent=2)}")
    print("----------")

first_characters = []

for row in grid:
    for item in row:
        if item != "[0]":
            match = re.match("\[(?P<letter>[A-Z]{1})\]", item)
            first_characters.append(match.group("letter"))
            break

print(f"first characters:", "".join(first_characters))
