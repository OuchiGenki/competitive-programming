import sys
sys.setrecursionlimit(10**8)

n = int(input())
a = [list(input()) for i in range(n)]
b = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        b[i][j] = a[i][j]

for i in range(n-1):
    b[0][i+1] = a[0][i]
    b[i+1][n-1] = a[i][n-1]
    b[n-1][i] = a[n-1][i+1]
    b[i][0] = a[i+1][0]

for i in range(n):
    print(*b[i], sep="")