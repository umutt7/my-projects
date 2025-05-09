import sys

# Check command-line arguments conditions
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

# Save the last argument as the path of the file
path = sys.argv[1]

# Counter for lines in given file
lines = 0

# Try to open the file and count the lines (except if a line starts with hashtag)
# If the file does not exist, warn the user and exit
try:
    with open(path) as file:
        for line in file:
            line = line.lstrip().rstrip("\n")
            if not (line.startswith("# ") or line.strip() == ""):
                lines += 1

except FileNotFoundError:
    sys.exit("File does not exist")

print(lines)
