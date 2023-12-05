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

def score_card(goal_numbers, have_numbers):
    num_matches = 0
    for n in have_numbers:
        if n in goal_numbers:
            num_matches += 1
    if num_matches == 0:
        return 0
    return int(pow(2, num_matches-1))

def parse_numbers(numbers_str):
    pattern = "\s(\d+)"
    return re.findall(pattern, numbers_str)

if __name__ == "__main__":
    arguments = docopt.docopt(__doc__)
    filename = arguments["<filename>"]

    sum = 0
    with open(filename, "r") as file:
        for line in file:
            numbers = line.split(":")[1].split("|")
            print(numbers)
            goal_numbers = parse_numbers(numbers[0])
            have_numbers = parse_numbers(numbers[1])
            score = score_card(goal_numbers, have_numbers)
            sum += score
    print(sum)

