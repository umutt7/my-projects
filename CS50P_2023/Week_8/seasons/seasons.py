from datetime import date
from sys import exit
import inflect

p = inflect.engine()


def main():
    # Get user's birthday
    birthday = input("Date of Birth: ")

    # Check if birthday is YYYY-MM-DD format
    if len(birthday) != 10 or birthday[4] != "-" or birthday[7] != "-":
        exit("Invalid date")
    # Check if birthday is valid, month is between 1 and 12, day is between 1 and 31
    try:
        year, month, day = birthday.split("-")
        date(int(year), int(month), int(day))
    except ValueError:
        exit("Invalid date")

    print(subtract_dates(birthday))


# Substact birthday from today's date
def subtract_dates(birthday):
    # Get today's date
    today = date.today()

    # Split birthday into year, month, and day
    year, month, day = birthday.split("-")

    # Convert it to date object
    birthday = date(int(year), int(month), int(day))

    # Calculate difference between today and birthday
    difference = today - birthday

    # Calculate number of minutes
    minutes = difference.days * 24 * 60

    return f"{p.number_to_words(minutes, andword='').capitalize()} minutes"


if __name__ == "__main__":
    main()
