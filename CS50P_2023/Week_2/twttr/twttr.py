def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    vowels = "AaEeIiOoUu"
    short = ""
    for c in word:
        if c not in vowels:
            short += c

    return short


if __name__ == "__main__":
    main()
