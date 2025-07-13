import sys
sys.setrecursionlimit(10**8)

def dfs(v):
    visited[v] = True
    for nv in G[v]:
        if visited[nv]:
            continue
        dfs(nv)


N, M = map(int, input().split())
if M != N-1:
    print('No')
    exit()

G = [[] for i in range(N)]
cnt = [0] * N
for i in range(M):
    u, v = map(int, input().split())
    cnt[u-1] += 1
    cnt[v-1] += 1
    G[u-1].append(v-1)
    G[v-1].append(u-1)
    if cnt[u-1] > 2 or cnt[v-1] > 2:
        print('No')
        exit()

visited = [False] * N
dfs(0)

if all(visited):
    print('Yes')
else:
    print('No')