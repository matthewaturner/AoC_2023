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

# scoring is different in the second game version
def score_card(goal_numbers, have_numbers):
    num_matches = 0
    for n in have_numbers:
        if n in goal_numbers:
            num_matches += 1
    return num_matches

def parse_numbers(numbers_str):
    pattern = "\s(\d+)"
    return re.findall(pattern, numbers_str)

if __name__ == "__main__":
    arguments = docopt.docopt(__doc__)
    filename = arguments["<filename>"]

    # read in all games
    games = []
    with open(filename, "r") as file:
        for line in file:
            games.append(line)

    # start with one copy of each game
    # this is basically a dp problem and we keep track of num copies
    # of each game in this array
    copies = [1] * len(games)

    for i in range(len(games)):
        numbers = games[i].split(":")[1].split("|")
        goal_numbers = parse_numbers(numbers[0])
        have_numbers = parse_numbers(numbers[1])
        score = score_card(goal_numbers, have_numbers)

        # record new copies of subsequent games
        print(f"game {i} scored {score}")
        print(f"Adding {copies[i]} to games {i+1} to {min(score, len(copies))}")
        for j in range(score):
            if i+j+1 < len(copies):
                copies[i+j+1] += copies[i]
            else:
                break

    print(sum(copies))

