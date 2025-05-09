def main():
    frac = get_frac("Fraction: ")
    print(frac)


def get_frac(prompt):
    while True:
        try:
            fraction = input(prompt)
            x, y = fraction.split(sep="/")
            if int(x) / int(y) <= 0.1:
                return "E"
            elif 1 >= int(x) / int(y) >= 0.9:
                return "F"
            elif 0.1 < int(x) / int(y) < 0.9:
                return str(round(int(x) / int(y) * 100)) + "%"
        except (ValueError, ZeroDivisionError):
            pass


main()