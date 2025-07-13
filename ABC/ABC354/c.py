N = int(input())
AC = [list(map(int, input().split())) for i in range(N)]
idx = {tuple(AC[i]):(i+1) for i in range(N)}
AC.sort(reverse=True)

minC = float('inf')
num = N
cards = []

for i in range(N):
    a, c = AC[i][0], AC[i][1]
    if minC < c:
        num -= 1
    else:
        minC = c
        cards.append(idx[(a, c)])

cards.sort()    

print(num)
print(*cards)