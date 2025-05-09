import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # Find all "um", " um" etc. in s except if it's not followed by a letter
    matches = re.findall(r"(?<!\w)um(?!\w)", s, flags=re.IGNORECASE)

    # Return the number of matches
    return len(matches)


if __name__ == "__main__":
    main()
