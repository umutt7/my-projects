def main():
    response = input("Greeting: ")
    print(value(response))


def value(greeting):
    if greeting.lower().strip().startswith("hello"):
        return 0
    elif greeting.lower().strip().startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
