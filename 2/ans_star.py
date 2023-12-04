import sys
import re

if len(sys.argv) != 2:
    print("Usage: python ans.py <filename>")
    sys.exit(1)
filename = sys.argv[1]

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

def process_line(line):
    max_counts = get_max_counts(line)
    power = 1
    for key, value in max_counts.items():
        power *= value
    return power

try:
    sum = 0
    with open(filename, "r") as file:
        for line in file:
            sum += process_line(line)
    print(sum)

except FileNotFoundError:
    print(f"Error: {filename} not found.")
