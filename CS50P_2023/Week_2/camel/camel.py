name = input("camelCase: ")

print("snake_case: ", end="")

# Check the name char by char
for c in name:
    # If the char is lower, print as it is
    if c.islower():
        print(c, end="")
    # If it's upper, print an underscore than the lowerized char
    elif c.isupper():
        print("_" + c.lower(), end="")

print()