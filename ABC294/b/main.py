import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

h, w = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]
ans = [['.' for i in range(w)] for j in range(h)]

for i in range(h):
    for j in range(w):
        if a[i][j]!=0:
            ans[i][j] = chr(65+a[i][j]-1)

for i in ans:
    print(*i, sep="")