import sys
import csv

# Check if two command-line arguments are provided
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Check if the file has a .csv extension
if not sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
    sys.exit("Not a csv file")

input_file = sys.argv[1]
output_file = sys.argv[2]

# Try to open the file, if FileNotFoundError exit program
try:
    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        fieldnames = ["first", "last", "house"]

        with open(output_file, "w") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                name = row["name"].split(", ")
                first = name[1].strip('"')
                last = name[0]
                house = row["house"]

                writer.writerow({
                    "first": first,
                    "last": last,
                    "house": house
                })

except FileNotFoundError:
    sys.exit("File does not exist")
