import random
from sys import exit

while True:

    try:
        level = int(input("Level: "))
        if level <= 0:
            raise ValueError
    except ValueError:
        continue

    correct = random.randint(1, level)
    guess = 0

    while guess != correct:

        try:
            guess = int(input("Guess: "))
            if guess > correct:
                print("Too large!")
            elif guess < correct:
                print("Too small!")
            elif guess == correct:
                print("Just right!")
                exit()
            else:
                pass

        except ValueError:
            continue
