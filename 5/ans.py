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

import re

def parse_seeds(input):
    pattern = r'\s(\d+)'
    return [int(x) for x in re.findall(pattern, input)]

def parse_groups(input):
    pattern = r'.*:(?:\n\d+\s\d+\s\d+)+'
    return re.findall(pattern, input)

def parse_maps(input):
    pattern = r'(\d+)\s(\d+)\s(\d+)'
    return [(int(x), int(y), int(z)) for x, y, z in re.findall(pattern, input)]

if __name__ == "__main__":
    arguments = docopt.docopt(__doc__)
    filename = arguments["<filename>"]

    with open(filename, 'r') as file:
        seed_line = file.readline()
        seeds = parse_seeds(seed_line)
        groups = parse_groups(file.read())
        maps = [parse_maps(group) for group in groups]
        #print(maps)

    lowest_location = None
    lowest_seed = None

    for seed in seeds:
        n = seed
        for map in maps:
            for rule in map:
                destination = rule[0]
                source = rule[1]
                range = rule[2]

                # if this map rule applies to this seed, convert it
                if source <= n and n < (source + range):
                    before = n
                    n += destination - source
                    print(f"{before} -> {n} :: {rule}")
                    # only process one rule per map
                    break
        if lowest_location == None or n < lowest_location:
            lowest_location = n
            lowest_seed = seed
        print(f" # Seed {seed} maps to {n}")
        print(f"Lowest location is seed {seed} with location {lowest_location}")