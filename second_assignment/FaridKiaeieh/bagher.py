numof, to_univ = [int(i) for i in input().split()]
redlamps = list()
# LENGTH , RED , GREEN
for i in range(numof):
    redlamps.append([int(i) for i in input().split()])

which = 0
where = 0
while where < to_univ:
    iso = False
    # print('WHERE:', where)
    # print('Time:', which)
    # print()
    for i in redlamps:
        iso = False
        if i[0] == where:
            # print(i[1] , which % (i[1] + i[2]))
            if i[1] > which % (i[1] + i[2]):
                which += i[1] - which % (i[1] + i[2])
        else:
            iso = True
    if iso:
        which += 1

    where += 1
print(which + 1)

