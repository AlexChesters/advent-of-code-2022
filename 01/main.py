import os

calories_map = {}

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
    calories = f.read().splitlines()

elf_index = 0

for index, calorie in enumerate(calories):
    if not calorie:
        elf_index += 1
        continue

    count = calories_map.get(elf_index, [])
    count.append(int(calorie))
    calories_map[elf_index] = count

calorie_counts = []

for _key, val in calories_map.items():
    calorie_counts.append(sum(val))

sorted_calorie_counts = sorted(calorie_counts, reverse=True)
print(f"answer is {sorted_calorie_counts[0] + sorted_calorie_counts[1] + sorted_calorie_counts[2]}")
