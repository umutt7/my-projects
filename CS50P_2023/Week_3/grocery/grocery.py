grocery = {

}

while True:
    try:
        add = input().upper().strip()
        if add in grocery:
            grocery[add] += 1
        else:
            grocery.update({add: 1})
    except (EOFError):
        sorted_grocery = dict(sorted(list(grocery.items())))
        for item in sorted_grocery:
            print(sorted_grocery[item], item, sep=" ")
        break
    except (KeyError):
        pass