from cs50 import get_int
from sys import exit


def main():
    # Get card number
    card = get_int("Number: ")
    # Find digits
    digits = digit_finder(card)
    sum = 0
    checksum = 0

    # If 12 < digits < 19
    if digits > 12 and digits < 19:
        # Copy the number to tmp_card
        tmp_card = card

        for i in range(1, digits+1, 1):
            # If digits are odd
            if i % 2 == 1:
                # Add the number to checksum
                checksum += tmp_card % 10
            # If digits are even
            else:
                # Get the digit value
                tmp = tmp_card % 10
                # If value is two digits
                if (tmp*2 > 9):
                    sum += (tmp*2 % 10) + (tmp*2 // 10)
                else:
                    sum += tmp * 2
            # If remaining tmp_card value is two digits, store it as starting digits
            if tmp_card > 9 and tmp_card < 100:
                starting_digits = tmp_card

            tmp_card = tmp_card // 10
        # Check conditions
        if (sum + checksum) % 10 == 0:
            if digits == 15 and (starting_digits == 34 or starting_digits == 37):
                print("AMEX")
            elif digits == 16 and (starting_digits < 56 and starting_digits > 50):
                print("MASTERCARD")
            elif (digits == 13 or digits == 16) and (starting_digits // 10 == 4):
                print("VISA")
            else:
                print("INVALID")

    else:
        print("INVALID")

    exit(0)


def digit_finder(card_number):
    count = 0
    while card_number != 0:
        count += 1
        card_number = card_number // 10
    return count


main()