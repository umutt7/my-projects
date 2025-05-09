### AM-PM FARKINI DAHİL ET

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(
        r"^([0-9][0-9]?)\:?([0-9][0-9]?)? (AM|PM) to ([0-9][0-9]?)\:?([0-9][0-9]?)? (AM|PM)$",
        s,
        re.IGNORECASE,
    )

    # Check matches for Nonetype
    if matches is None:
        raise ValueError

    # Create an empty list with size of 3 for the first time
    time_first = [None] * 3

    # Assign the values to the list -> [hour, minute, am/pm]
    for i in range(1, 4):
        if matches.group(i) is None:
            time_first[i - 1] = 0
        else:
            time_first[i - 1] = matches.group(i)

    # Check for wrong input, if there is a None value, raise ValueError
    for i in range(1, 4):
        if time_first[i - 1] is None:
            raise ValueError

    # Create an empty list with size of 3 for the second time
    time_second = [None] * 3

    # Assign the values to the list -> [hour, minute, am/pm]
    for i in range(4, 7):
        if matches.group(i) is None:
            time_second[i - 4] = 0
        else:
            time_second[i - 4] = matches.group(i)

    # Check for wrong input, if there is a None value, raise ValueError
    for i in range(4, 7):
        if time_second[i - 4] is None:
            raise ValueError

    first_time = convert_time(time_first)
    second_time = convert_time(time_second)

    # Return the converted time
    return f"{first_time} to {second_time}"


def convert_time(time):
    # Check hours for value error
    if int(time[0]) > 12:
        raise ValueError

    # Check minutes for value error
    if int(time[1]) > 59 or 0 < int(time[1]) < 10:
        raise ValueError

    if time[2].lower() == "am":
        if time[0] == "12":
            time[0] = "00"

    if time[2].lower() == "pm":
        if int(time[0]) < 12:
            time[0] = int(time[0]) + 12

    # make hours 2 digits
    if len(str(time[0])) == 1:
        time[0] = "0" + str(time[0])

    # make minutes 2 digits
    if time[1] is None or time[1] == 0:
        time[1] = "00"

    return f"{time[0]}:{time[1]}"


if __name__ == "__main__":
    main()
