from cs50 import get_string
from sys import exit
from decimal import Decimal


def main():
    # Get string, count letters, and words, and sentences
    str = get_string("Text: ")
    letters = count_letters(str)
    words = count_words(str)
    sentences = count_sentences(str)

    # Calculate letters-per-words and sentences-per-words
    letters_per_words = (letters / words) * 100
    sentences_per_words = (sentences / words) * 100

    # Apply Coleman-Liau index
    index = Decimal(0.0588 * letters_per_words - 0.296 * sentences_per_words - 15.8)
    index = round(index)

    # print(f"{letters} {words} {sentences}")

    # Special conditions for >16 and <1 index
    if index > 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {index}")

    exit(0)


def count_letters(text):

    count = 0
    # for (int i = 0, n = strlen(text); i < n; i++)
    for i in text:
        if i.isalpha():
            count += 1
    # Return count of letters
    return count


def count_words(text):

    count = 0
    n = len(text)
    # Same for function but in more C way
    for i in range(n):
        if text[i] == " " or i == n - 1:
            count += 1
    # Return count of words
    return count


def count_sentences(text):

    count = 0

    for i in text:
        if i == "." or i == "!" or i == "?":
            count += 1

    return count


main()