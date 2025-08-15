import sys
sys.setrecursionlimit(10**8)

def dfs(v, c):
    visited[v] = True
    color[v] = c
    for nv in to[v]:
        if visited[nv]:
            continue
        dfs(nv, c^1)


n, q = map(int, input().split())
to = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    to[a-1].append(b-1)
    to[b-1].append(a-1)
visited = [False] * n
color = [-1] * n

dfs(0, 0)

for _ in range(q):
    c, d = map(int, input().split())
    if color[c-1] == color[d-1]:
        print('Town')
    else:
        print('Road')