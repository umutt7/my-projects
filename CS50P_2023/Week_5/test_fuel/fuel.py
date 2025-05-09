def main():
    frac = input("Fraction: ")
    print(gauge(convert(frac)))


def convert(fraction):
    x, y = fraction.split(sep="/")
    if int(x) / int(y) > 1:
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError

    return int(int(x) / int(y) * 100)


def gauge(percentage):
    if int(percentage) <= 1:
        return "E"
    elif int(percentage) >= 99:
        return "F"
    else:
        return f"{int(percentage)}%"


if __name__ == "__main__":
    main()
