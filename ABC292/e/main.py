import sys
sys.setrecursionlimit(10**7)

def dfs(v):
    global cnt
    visited[v] = True
    for nv in g[v]:
        if visited[nv]:
            continue
        cnt += 1
        dfs(nv)

n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    g[u-1].append(v-1)

cnt = 0
for i in range(n):
    visited = [False for i in range(n)]
    dfs(i)

print(cnt - m)