import sys
sys.setrecursionlimit(10**8)

def dfs(v, now):
    global ans, N

    if v == N-1:
        ans = min(ans, now)
        return

    visited[v] = True
    for nv, nw in G[v]:
        if visited[nv]:
            continue
        dfs(nv, now^nw)
    
    visited[v] = False
        


N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    u, v, w = map(int, input().split())
    G[u-1].append((v-1, w))
    G[v-1].append((u-1, w))

ans = float('inf')
visited = [False] * N
dfs(0, 0)
print(ans)