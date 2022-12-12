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

print(f"starting grid (empty): {grid}")

for idx, row in enumerate(stacks):
    grid_row = []

    parsed_row = re.split("[\s]+", row)
    print(f"parsed row: {parsed_row}")

    for item in re.split("[\s]+", row):
        if item:
            print(f"adding item {item} to row {grid_row}")
            grid_row.append(item)

    print(f"adding row {grid_row} to grid")

    grid[idx].extend(grid_row)

for item in grid:
    for idx in range(8):
        try:
            item[idx]
        except IndexError:
            item.append('[0]')

print(f"grid before transposing: {grid}")

grid = list(numpy.transpose(grid))

for idx, column in enumerate(grid):
    grid[idx] = column.tolist()

print(f"starting grid: {grid}")

for procedure in rearrangement_procedure:
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

    while crate_count > moved_crate_count:
        print(f"crates moved: {moved_crate_count}")
        crate_to_move = starting_column[crate_index]

        if crate_to_move == "[0]":
            crate_index += 1
            continue

        print(f"moving element {crate_to_move} from {starting_column}")

        starting_column[crate_index] = "[0]"

        reversed_destination = list(reversed(destination_column))

        print(f"reversed destination before: {reversed_destination}")

        have_moved_crate = False

        for existing_item_idx, existing_item in enumerate(reversed_destination):
            if existing_item == "[0]":
                print(f"placing new crate at {existing_item_idx}")
                reversed_destination[existing_item_idx] = crate_to_move
                moved_crate_count += 1
                crate_index += 1
                have_moved_crate = True
                break

        if not have_moved_crate:
            moved_crate_count += 1
            crate_index += 1
            # reversed_destination.insert(0, crate_to_move)
            reversed_destination.append(crate_to_move)

        print(f"reversed destination after: {reversed_destination}")

        destination_column = list(reversed(reversed_destination))

    grid[starting_column_index] = starting_column
    grid[destination_column_index] = destination_column

    print(f"starting column: {starting_column}")
    print(f"destination column: {destination_column}")

    print(f"new grid: {json.dumps(grid, indent=2)}")
    print("----------")

first_characters = []

for row in grid:
    print(f"analysing row: {row}")
    for item in row:
        if item != "[0]":
            match = re.match("\[(?P<letter>[A-Z]{1})\]", item)
            first_characters.append(match.group("letter"))
            break

print(f"first characters:", "".join(first_characters))
