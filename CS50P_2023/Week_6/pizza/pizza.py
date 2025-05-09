import csv
import sys
from tabulate import tabulate


# Check command-line conditions
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

# Save the last argument as file path
path = sys.argv[1]

# Try to open the file, if file not found, warn the user and exit
try:
    # Create an empty list to save the content of the file
    menu = []

    with open(path) as file:
        # With .DictReader, name the fieldnames as follows
        reader = csv.DictReader(file, fieldnames=("pizza", "small", "large"))
        # Append the list in order to content and fieldnames
        for row in reader:
            menu.append(
                {"pizza": row["pizza"], "small": row["small"], "large": row["large"]}
            )
except FileNotFoundError:
    sys.exit("File does not found")

# Print the list as an ASCII table
print(tabulate(menu, headers="firstrow", tablefmt="grid"))
