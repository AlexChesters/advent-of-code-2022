import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
    markers = f.read().splitlines()

LOOKBACK_LENGTH = 14

for marker in markers:
    print(f"processing marker: {marker}")

    components = list(enumerate(marker))

    for item in components:
        index, character = item

        if index < LOOKBACK_LENGTH:
            continue

        lookback_chars = []

        for i in range(LOOKBACK_LENGTH - 1):
            _, lookback_char = components[index - (i + 1)]
            lookback_chars.append(lookback_char)

        lookback_chars_str = "".join(list(reversed(lookback_chars)))

        characters = f"{lookback_chars_str}{character}"

        print(f"processing characters {characters}")

        if len(set(characters)) == LOOKBACK_LENGTH:
            print(f"found marker: {characters} at position {(index + 1)}")
            break
