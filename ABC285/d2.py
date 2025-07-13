from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)

def dfs(v):
    global flag
    visited[v] = True
    for nv in G[v]:
        if visited[nv]:
            if not finished[nv]:
                flag = False
            continue
        dfs(nv)
    finished[v] = True


N = int(input())
G = defaultdict(list)
for i in range(N):
    s, t = input().split()
    G[s].append(t)

visited = defaultdict(bool)
finished = defaultdict(bool)
flag = True
for v in list(G.keys()):
    if visited[v]:
        continue
    dfs(v)

if flag:
    print('Yes')
else:
    print('No')