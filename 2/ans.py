import sys
import re

if len(sys.argv) != 2:
    print("Usage: python ans.py <filename>")
    sys.exit(1)
filename = sys.argv[1]

MAX_RED = 12
MAX_BLUE = 14
MAX_GREEN = 13

def get_max_counts(line):
    max_counts = {}
    pattern = "(\d+) (\w+)"
    matches = re.findall(pattern, line)
    for match in matches:
        color = match[1]
        count = match[0]
        if color in max_counts:
            max_counts[color] = max(max_counts[color], int(count))
        else:
            max_counts[color] = int(count)
    return max_counts

def get_game_number(line):
    pattern = "Game (\d+):"
    match = re.search(pattern, line)
    return int(match[1])

def process_line(line):
    max_counts = get_max_counts(line)

    if (max_counts["blue"] > MAX_BLUE or
        max_counts["red"] > MAX_RED or
        max_counts["green"] > MAX_GREEN):
        print(f"{line} -> not possible")
        return 0
    else:
        print(f"{line} -> possible")
        return get_game_number(line)

try:
    sum = 0
    with open(filename, "r") as file:
        for line in file:
            sum += process_line(line)
    print(sum)


except FileNotFoundError:
    print(f"Error: {filename} not found.")
