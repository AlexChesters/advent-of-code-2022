import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
    markers = f.read().splitlines()

for marker in markers:
    print(f"processing marker: {marker}")

    components = list(enumerate(marker))

    for item in components:
        index, character = item

        if index < 3:
            continue

        _, one_back = components[index - 1]
        _, two_back = components[index - 2]
        _, three_back = components[index - 3]

        characters = f"{three_back}{two_back}{one_back}{character}"

        print(f"processing characters {characters}")

        if len(set(characters)) == 4:
            print(f"found marker: {characters} at position {(index + 1)}")
            break
