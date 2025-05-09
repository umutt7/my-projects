import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Search the regex, recort the video code
    match = re.search(r"\"https?://(?:www\.)?youtube\.com/embed/(\w+)\"", s)

    try:
        # Concatenate the start of the link with video code
        video = "https://youtu.be/" + match.group(1)
        if match:
            return video

    except AttributeError:
        return None


if __name__ == "__main__":
    main()
