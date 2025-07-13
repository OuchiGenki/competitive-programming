import sys
sys.setrecursionlimit(10**8)

n = int(input())
s = [input() for i in range(n)]

points = [[0, i+1] for i in range(n)]

for i in range(n):
    for a in s[i]:
        if a=="o":
            points[i][0] += 1

points.sort(key=lambda x:(-x[0], x[1]))

for li in points:
    print(li[1], end=" ")
