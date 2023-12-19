import sys
import csv
from tabulate import tabulate

# Check if two command-line arguments are provided
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# Check if the file has a .csv extension
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a csv file")

# Try to open the file, if FileNotFoundError exit program
try:
    file = open(sys.argv[1], "r")
except FileNotFoundError:
    sys.exit("File does not exist")


with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)
    table = []
    for row in reader:
        table.append(row)
    print(tabulate(table, headers="keys", tablefmt="grid"))
