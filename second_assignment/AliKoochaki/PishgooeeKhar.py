def awnser(word):
    for i in wordAnaAwnser:
        if word == i[0]:
            return i[1] + " kachal!"
    return "kachal!"


numbers = input().split(" ")
n = int(numbers[0])
m = int(numbers[1])

wordAnaAwnser = []
for i in range(n):
    wordAnaAwnser.append(input().split(" "))

goatWord = input().split(" ")

for i in goatWord:
    print(awnser(i), end=" ")