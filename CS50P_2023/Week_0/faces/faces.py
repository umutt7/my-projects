# Replace the emoticons and return
def convert(string):
    return string.replace(":(", "🙁").replace(":)", "🙂")

# Get message and print the converted version
def main():
    message = input()
    print(convert(message))

main()