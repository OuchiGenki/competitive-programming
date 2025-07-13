import sys
import pypyjit
pypyjit.set_param("max_unroll_recursion=-1")
sys.setrecursionlimit(10**8)

def dfs(v):
    visited[v] = True
    for nv, w in G[v]:
        if visited[nv]:
            continue
        X[nv] = X[v] + w
        dfs(nv)

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    u, v, w = map(int, input().split())
    G[u-1].append((v-1, w))
    G[v-1].append((u-1, -w))

visited = [False for i in range(N)]
X = [0 for i in range(N)]

for i in range(N):
    if not visited[i]:
        dfs(i)

print(*X)