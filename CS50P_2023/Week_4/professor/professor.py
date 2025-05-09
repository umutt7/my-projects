import random


def main():
    level = get_level()
    correct = 0
    for _ in range(10):
        first = generate_integer(level)
        second = generate_integer(level)
        sum = int(first) + int(second)
        wrongs = 0
        get = 0

        while wrongs != 3:
            print(f"{first} + {second} = ", end="")

            try:
                get = int(input())
            except ValueError:
                continue

            if get != sum:
                print("EEE")
                wrongs += 1
                continue
            else:
                correct += 1
                break

        if wrongs == 3:
            print(f"{first} + {second} = {sum}")

    print("Score: " + str(correct))


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if not 0 < level < 4:
                raise ValueError
            return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
