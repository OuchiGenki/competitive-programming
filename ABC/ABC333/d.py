import sys
sys.setrecursionlimit(10**8)

def dfs(v):
    visited[v] = True
    cnt = 0

    for nv in G[v]:
        if visited[nv]:
            continue
        cnt += dfs(nv)
    
    cnt += 1

    return cnt


N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    u, v = map(int,input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

if len(G[0]) == 1:
    print(1)
    exit()

visited = [False]*N
visited[0] = True

res = 0
for v in G[0]:
    res = max(res, dfs(v))

print(N - res)