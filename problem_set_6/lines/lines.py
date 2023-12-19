import sys


# Check if two command-line arguments are provided
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# Check if the file has a .py extension
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file")

# Try to open the file, if FileNotFoundError exit program
try:
    file = open(sys.argv[1], "r")
except FileNotFoundError:
    sys.exit("File does not exist")

# Iterate over the lines and track how many there are, set var to 0
code_lines: int = 0

for l in file.read().splitlines():
    # // Check if line is empty
    if len(l.strip()) == 0:
        continue

    # // Check if line starts with a comment
    if not l.strip().startswith("#"):
        code_lines += 1

print(code_lines)
