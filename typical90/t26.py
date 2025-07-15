import sys
sys.setrecursionlimit(10**8)

n = int(input())
G = [[] for i in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
visited = [False] * n
colors = [-1] * n

def dfs(v, c):
    visited[v] = True
    colors[v] = c
    for nv in G[v]:
        if visited[nv]:
            continue
        dfs(nv, c^1)

dfs(0, 0)
if colors.count(0) < colors.count(1):
    print(*[i+1 for i in range(n) if colors[i] == 1][:n//2])
else:
    print(*[i+1 for i in range(n) if colors[i] == 0][:n//2])