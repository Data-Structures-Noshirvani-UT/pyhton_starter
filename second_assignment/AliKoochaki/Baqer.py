def keepRed(time, redTime, greenTime):
    time = int(time)
    redTime = int(redTime)
    greenTime = int(greenTime)
    while True:
        time -= redTime
        if (time < 0):
            return [time, 'r']
        elif time == 0:
            return [time, 'g']
        else:
            time -= greenTime
            if time < 0:
                return [time, 'g']
            elif time == 0:
                return [redTime * (-1), 'r']


n, l = input().split(" ")
n = int(n)
l = int(l)

cheraq = []
for i in range(n):
    cheraq.append(input().split(" "))

time = 0
distance = 0
totalDistance = 0

for i in cheraq:
    distance = int(i[0]) - totalDistance
    totalDistance += distance
    time += distance
    Time = keepRed(time, i[1], i[2])
    if Time[1] == 'r':
        time -= Time[0]

print(time + (l - int(cheraq[-1][0])))