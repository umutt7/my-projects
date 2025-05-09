import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


# Function to check if IP is valid
def validate(ip):
    # Search this regex: "numbers.numbers.numbers.numbers"
    matches = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)

    try:
        # Seperate the numbers
        first, second, third, fourth = matches.groups()

        # Check if the numbers are between 0-255 inclusive
        if (
            0 <= int(first) < 256
            and 0 <= int(second) < 256
            and 0 <= int(third) < 256
            and 0 <= int(fourth) < 256
        ):
            return True
        else:
            return False

    except AttributeError:
        return False


if __name__ == "__main__":
    main()
