from itertools import *
from math import sqrt

def dist(x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1
    return sqrt(dx**2 + dy**2)

n = int(input())
xy = []
for i in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))

iter = [i for i in range(n)]
sum = 0
divisor = 0
for li in list(permutations(iter)):
    divisor += 1
    for j in range(n-1):
        sum += dist(*xy[li[j]], *xy[li[j+1]])

print(sum/divisor)