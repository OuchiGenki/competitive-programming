import sys
sys.setrecursionlimit(10**8)

n, d, p = map(int, input().split())
f = list(map(int, input().split()))

sum = [0]
for i in range(n):
    sum