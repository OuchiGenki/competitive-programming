from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

def dfs(v):
    visited[v] = True
    for nv in G[v]:
        if visited[nv]:
            continue
        dfs(nv)

N, M = map(int, input().split())
if N-1 != M:
    print('No')
    exit()

cnt = defaultdict(int)
G = [[] for i in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    G[v-1].append(u-1)
    G[u-1].append(v-1)
    cnt[v-1] += 1
    cnt[u-1] += 1
    if cnt[v-1] > 2 or cnt[u-1] > 2:
        print('No')
        exit()

visited = [False] * N
dfs(0)
if not all(visited):
    print('No')
    exit()

print('Yes')