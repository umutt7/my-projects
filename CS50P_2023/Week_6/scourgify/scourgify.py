import csv
import sys


# Check command-line conditions
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif (not sys.argv[1].endswith(".csv")) or (not sys.argv[2].endswith(".csv")):
    sys.exit("Not a CSV file")

# Save the last two arguments as file paths
path_first = sys.argv[1]
path_last = sys.argv[2]

# Try to open the first path, if the file not found, warn the user and exit
try:
    # Create an empty list to save the content of the .csv
    list = []

    with open(path_first) as file:
        # With .DictReader, name the fieldnames as follows
        reader = csv.DictReader(file)
        for row in reader:
            # In every row, split the first column with comma, and save those values seperately, and append them to the list
            last, first = row["name"].split(", ")
            list.append({"first": first, "last": last, "house": row["house"]})

# If the file not found, warn the user and exit
except FileNotFoundError:
    sys.exit("Could not read" + path_first)

# Write the list to the last path
with open(path_last, "w") as file:
    writer = csv.DictWriter(file, fieldnames=("first", "last", "house"))
    writer.writeheader()
    for row in list:
        writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
