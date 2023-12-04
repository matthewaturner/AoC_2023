import sys

if len(sys.argv) != 2:
    print("Usage: python ans.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

def get_first_num(line):
    for i in range(len(line)):
        if ord(line[i]) >= 48 and ord(line[i]) <= 57:
            return line[i]

try:
    sum = 0
    with open(filename, "r") as file:
        for line in file:
            sum += int(get_first_num(line) + get_first_num(line[::-1]))
    print('Total is: ' + str(sum))

except FileNotFoundError:
    print(f"Error: {filename} not found.")

