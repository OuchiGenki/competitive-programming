from math import gcd

n = int(input())
XY = [list(map(int, input().split())) for _ in range(n)]
S = set()
for i in range(n):
    x1, y1 = XY[i]
    for j in range(n):
        if i == j:
            continue
        x2, y2 = XY[j]
        dx = x1 - x2
        dy = y1 - y2
        g = gcd(dx, dy)
        S.add((dx // g, dy // g))
print(len(S))