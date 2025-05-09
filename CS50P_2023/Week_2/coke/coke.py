due = 50

while due > 0:
    print("Amount Due: " + str(due))

    coin = int(input("Insert Coin: "))

    if coin == 25 or coin == 10 or coin == 5:
        due -= coin
        if due <= 0:
            print("Change Owed: " + str(abs(due)))
            break