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

if __name__ == "__main__":
    arguments = docopt.docopt(__doc__)
    filename = arguments["<filename>"]

    nodes = {}

    with open(filename, 'r') as file:
        moves = file.readline().strip()
        file.readline()
        for line in file:
            node_info = re.findall(r"[A-Z]+", line)
            nodes[node_info[0]] = (node_info[1], node_info[2], node_info[0])

    n = nodes['AAA']
    i = 0
    steps = 0
    while True:
        steps += 1
        m = moves[i]
        if m == 'R':
            n = nodes[n[1]]
        else:
            n = nodes[n[0]]

        if n[2].endswith('Z'):
            break;

        i += 1
        if i == len(moves):
            i = 0

    print(nodes)
    print(steps)


