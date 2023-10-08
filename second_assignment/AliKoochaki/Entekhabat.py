def entekhab(kandida):
    if len(kandida) == 3:
        print(kandida[2])
        exit()
    elif len(kandida) == 2:
        print(kandida[0])
        exit()
    else:
        if len(kandida) % 2 == 1:
            kandida = kandida[::2]
            kandida = kandida[1:]
            return entekhab(kandida)
        else:
            return entekhab(kandida[::2])


n = int(input())
kandida = range(1, n + 1)
entekhab(kandida)