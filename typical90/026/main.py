import sys
sys.setrecursionlimit(10**7)

def dfs(v, c):
    visited[v] = True
    if c == 0:
        c1.append(v)
    else:
        c2.append(v)
    for nv in g[v]:
        if visited[nv]:
            continue
        dfs(nv, (c+1)%2)

n = int(input())
g = [[] for i in range(n)]
visited = [False for i in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

c1 = []
c2 = []
dfs(0, 0)

if len(c1) >= len(c2):
    for i in range(n//2):
        print(c1[i]+1, end=" ")
else:
    for i in range(n//2):
        print(c2[i]+1, end=" ")