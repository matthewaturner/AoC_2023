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
from math import ceil, floor

def parse_numbers(input):
    pattern = r'\s(\d+)'
    return [int(x) for x in re.findall(pattern, input)]

if __name__ == "__main__":
    arguments = docopt.docopt(__doc__)
    filename = arguments["<filename>"]

    with open(filename, 'r') as file:
        time_line = file.readline()
        dist_line = file.readline()
        times = parse_numbers(time_line)
        distances = parse_numbers(dist_line)
    
    running_total = 1
    for time, distance in zip(times, distances):
        a = -1
        b = time
        c = -distance
        print(f"a: {a}, b: {b}, c: {c}")

        # Quadratic formula
        t_low = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
        t_high = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
        print(f"Time Low: {t_low}, Time High: {t_high}")

        combos = int(ceil(t_high - 1)) - int(floor(t_low + 1)) + 1
        running_total *= combos

        print(f"Combos: {combos}")
        print(f"Running Total: {running_total}")
    
    print(f"\nTotal Combos: {running_total}")
