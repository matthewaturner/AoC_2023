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

# select the outer box of symbols around the part number
def is_part_number(part_result):
    i = part_result[1][0]
    j = part_result[1][1]
    length = part_result[2]
    lines = TEXT[max(i-1, 0):min(i+2, TOTAL_ROWS)]
    for l in range(len(lines)):
        lines[l] = lines[l][max(j-1, 0):min(j+1+length, TOTAL_COLS)]
        print(lines[l])
    pattern = "[^0-9\.\s]" # all symbols
    return bool(re.search(pattern, ''.join(lines)))

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
        if is_part_number(n):
            print("IS PART NUMBER")
            sum += int(n[0])
    print(f"Sum: {sum}")

