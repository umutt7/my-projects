def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# Check validness
def is_valid(s):
    # If length is not 2 <= x <= 6, or firts two chars are not alphabetical
    # or the plate itself is not alpabetical and/or numeric, return false
    if len(s) < 2 or len(s) > 6 or not s[:2].isalpha() or not s.isalnum():
        return False

    # Digit counter
    digit_count = 0

    # Check plate char by char
    for c1 in range(len(s)):

        # If the first digit is 0, return false. Else, add 1 to counter
        if s[c1] == "0" and digit_count == 0:
            return False
        elif s[c1].isdigit():
            digit_count += 1

        # If one of the next chars are alpha, return false
        for c2 in range(c1+1,len(s)):
            if s[c1].isdigit() and s[c2].isalpha():
                return False

    # If all conditions are met, return true
    return True


main()
