def find_winner(n):
    if n == 1:
        return 1
    else:
        return (find_winner(n-1) + 1) % n + 1


n = int(input())
winner = find_winner(n)
print(winner)
