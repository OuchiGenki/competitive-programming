import sys
sys.setrecursionlimit(10**8)

n, a, b = map(int,input().split())
d = list(map(int, input().split()))
for i in range(n):
    d[i] -= 1
for i in range(n):
    d[i] = d[i]%(a+b)
d = sorted(d)
for i in range(n):
    if (d[(i+1)%(n)]+a+b-d[(i)%(n)])%(a+b) <= a:
        print("Yes")
        exit()

print("No")