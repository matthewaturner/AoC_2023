"""
Usage: ans.py <filename>

Arguments:
  filename  The name of the file to process

Options:
  -h --help     Show this screen.
"""

import docopt
import sys
import re

TEXT = []
TOTAL_ROWS = 0
TOTAL_COLS = 0
GEARS = {}

# Similar to code in previous answer, but now we are interested in mapping only the * symbols.
# We find all gears next to each part number then indentify gears by their i,j coordinates
# and store the list of parts next to them in the global GEARS dict.
def map_gears(part_result):
    i = part_result[1][0]
    j = part_result[1][1]
    length = part_result[2]

    start_i = max(i-1, 0)
    end_i   = min(i+2, TOTAL_ROWS)
    start_j = max(j-1, 0)
    end_j   = min(j+1+length, TOTAL_COLS)

    lines = TEXT[start_i:end_i]
    for l in range(len(lines)):
        lines[l] = lines[l][start_j:end_j]
        print(lines[l])

    pattern = "\*" # all gears
    for l in range(len(lines)):
        for g in re.finditer(pattern, lines[l]):
            gear_key = (start_i+l, start_j+g.start())
            print(f"Found gear at: {gear_key}")
            if gear_key in GEARS:
                GEARS[gear_key].append(int(part_result[0]))
            else:
                GEARS[gear_key] = [int(part_result[0])]

# select all part numbers, with their i,j coordinates and length
def get_all_numbers():
    results = []
    pattern = "\d+"
    for i in range(len(TEXT)):
        for m in re.finditer(pattern, TEXT[i]):
            results.append((m.group(), (i, m.start()), len(m.group())))
    return results

def read_all_text():
    global TEXT, TOTAL_ROWS, TOTAL_COLS
    with open(filename, "r") as file:
        for line in file:
            TEXT.append(line)
    TOTAL_ROWS = len(TEXT)
    TOTAL_COLS = len(TEXT[0])
    
# main loop
if __name__ == "__main__":
    arguments = docopt.docopt(__doc__)
    filename = arguments["<filename>"]

    sum = 0
    read_all_text()
    numbers = get_all_numbers()
    for n in numbers:
        print(n)
        map_gears(n)

    for k, v in GEARS.items():
        if (len(v) == 2):
            print(f"Found pair: {k} -> {v}")
            sum += v[0] * v[1]
    
    print(sum)

