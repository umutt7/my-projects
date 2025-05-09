import inflect

p = inflect.engine()

names = []

while True:
    try:
        add = input("Name: ")
        names.append(add)

    except EOFError:
        print()
        mylist = p.join(names)
        print("Adieu, adieu, to " + mylist)
        break
