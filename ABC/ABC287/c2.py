import sys
sys.setrecursionlimit(10**8)

def dfs(v):
    visited[v] = True
    for nv in G[v]:
        if visited[nv]:
            continue
        dfs(nv)


N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

if M != N-1:
    print('No')
    exit()

for i in range(N ):
    if len(G[i]) > 2:
        print('No')
        exit()

visited = [False] * N
dfs(0)
if not all(visited):
    print('No')
    exit()

print('Yes')