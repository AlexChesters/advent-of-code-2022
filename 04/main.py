import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
    section_assignment_pairs = f.read().splitlines()

def generate_set(start, end):
    result = set()

    for i in range(int(start), int(end) + 1):
        result.add(i)

    return result

number_of_subsets = 0

for pairs in section_assignment_pairs:
    first_pair, second_pair = pairs.split(",")

    first_start, first_end = first_pair.split("-")
    second_start, second_end = second_pair.split("-")

    first_set = generate_set(first_start, first_end)
    second_set = generate_set(second_start, second_end)

    if first_set.issubset(second_set) or second_set.issubset(first_set):
        number_of_subsets += 1

print(f"total number of subsets: {number_of_subsets}")
