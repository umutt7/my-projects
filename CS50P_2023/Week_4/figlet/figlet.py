from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

fonts = figlet.getFonts()

if len(sys.argv) == 1:
    text = input("Input: ")
    font = figlet.setFont(font=random.choice(fonts))
    print("Output: ")
    print(figlet.renderText(text))

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    if sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    text = input("Input: ")
    font = figlet.setFont(font=sys.argv[2])
    print("Output: ")
    print(figlet.renderText(text))

else:
    sys.exit("Invalid usage")
