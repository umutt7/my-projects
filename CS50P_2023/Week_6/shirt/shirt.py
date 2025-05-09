import os
from PIL import Image, ImageOps
import sys

# Check command-line conditions
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif os.path.splitext(sys.argv[1])[1].lower() != os.path.splitext(sys.argv[2])[1].lower():
    sys.exit("Input and output have different extensions")

# Save the arguments as paths
input = sys.argv[1]
output = sys.argv[2]

# Try to open, crop, edit, and save the input as output
try:
    shirt = Image.open("shirt.png")
    with Image.open(input) as file:
        input_crop = ImageOps.fit(file, shirt.size)
        input_crop.paste(shirt, mask = shirt)
        input_crop.save(output)

except FileNotFoundError:
    sys.exit("Input does not exist")
