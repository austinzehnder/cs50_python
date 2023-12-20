import sys
import os
from PIL import Image, ImageOps

# Check if two command-line arguments are provided
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Open input image
input_file = sys.argv[1]
try:
    input_image = Image.open(input_file)
except FileNotFoundError:
    sys.exit("Input does not exist")

output_file = sys.argv[2]

# Split file name from extension
input_ext = os.path.splitext(input_file)[1].lower()
output_ext = os.path.splitext(output_file)[1].lower()

# Check for valid input extension
if input_ext not in [".jpeg", ".jpg", ".png"]:
    sys.exit("Invalid input")

# Check for valid output extension
if output_ext not in [".jpeg", ".jpg", ".png"]:
    sys.exit("Invalid output")

# Check for matching extensions
if input_ext != output_ext:
    sys.exit("Input and output have different extensions")

# Open and resize overlay image
shirt = Image.open("shirt.png")
shirt_width, shirt_height = shirt.size
input_image = ImageOps.fit(input_image, (shirt_width, shirt_height))

# Paste overlay image on top of input image
input_image.paste(shirt, (0, 0), shirt)

# Save pasted image as output filename
input_image.save(output_file)
