# Import get_int from cs50 library
from cs50 import get_int


def main():
    # Use get_height function
    n = get_height()

    # for (i = 0; i < n; i++)
    for i in range(n):
        # for (j = n-i; j < 0; j--)
        for j in range(n-i, 1, -1):
            # Print the spaces at the start of higher lines
            print(" ", end="")
        # Print number of bricks
        bricks(i + 1)
        # Print the middle space
        print("  ", end="")
        # Print the same number of bricks
        bricks(i + 1)
        # New line
        print("")


def get_height():
    # Ask for a number until it's valid
    height = 0
    while True:
        try:
            height = get_int("Height: ")
        except ValueError:
            print("That's not a valid input!")
        else:
            if height > 0 and height < 9:
                return height


def bricks(a):
    for i in range(a):
        print("#", end="")


main()