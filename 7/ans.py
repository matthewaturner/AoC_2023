"""
Usage: ans.py <filename>

Arguments:
  filename  The name of the file to process

Options:
  -h --help     Show this screen.
"""

import docopt
import re
from math import ceil, floor

def parse_numbers(input):
    pattern = r'\s(\d+)'
    return [int(x) for x in re.findall(pattern, input)]

def hand_to_ints(hand):
    card_map = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
        '1': 1
    }
    return [card_map[c] for c in hand]

def sort_hand(hand):
    counts = {}
    for card in hand:
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1

    h = []
    for card, count in sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True):
        h += [card]*count

    rank = 0

    if h[0] == h[1] == h[2] == h[3] == h[4]:
        rank = 6
    elif h[0] == h[1] == h[2] == h[3]:
        rank = 5
    elif h[0] == h[1] == h[2] and h[3] == h[4]:
        rank = 4
    elif h[0] == h[1] == h[2]:
        rank = 3
    elif h[0] == h[1] and h[2] == h[3]:
        rank = 2
    elif h[0] == h[1]:
        rank = 1
    else:
        rank = 0

    return [rank] + hand

if __name__ == "__main__":
    arguments = docopt.docopt(__doc__)
    filename = arguments["<filename>"]

    all_hands = []

    with open(filename, 'r') as file:
        for line in file:
            hand = hand_to_ints(line.split()[0])
            bid = int(line.split()[1])

            all_hands.append((sort_hand(hand), bid))

    all_hands = sorted(all_hands, key=lambda x: x[0])

    sum = 0
    rank = 1
    for hand, bid in all_hands:
        print(f"{hand}, {bid} = {rank}*{bid}={rank*bid}")
        sum += bid*rank
        rank += 1

    print(sum)

