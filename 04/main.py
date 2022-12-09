import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
    section_assignment_pairs = f.read().splitlines()

def generate_list(start, end):
    result = []

    for i in range(int(start), int(end) + 1):
        result.append(i)

    return result

number_of_overlaps = 0

for pairs in section_assignment_pairs:
    first_pair, second_pair = pairs.split(",")

    first_start, first_end = first_pair.split("-")
    second_start, second_end = second_pair.split("-")

    first_list = generate_list(first_start, first_end)
    second_list = generate_list(second_start, second_end)

    overlaps = set(first_list).intersection(second_list)

    if overlaps:
        number_of_overlaps += 1

print(f"total number of overlaps: {number_of_overlaps}")
