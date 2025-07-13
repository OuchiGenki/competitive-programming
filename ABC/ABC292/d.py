import sys
sys.setrecursionlimit(10**8)

def dfs(v):
    global num_of_edges
    visited[v] = True
    cnt = 0
    for nv in G[v]:
        num_of_edges += 1
        if visited[nv]:
            continue
        cnt += dfs(nv)
    return cnt + 1


N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)
visited = [False] * N
flag = True

for i in range(N):
    num_of_edges = 0
    if visited[i]:
        continue
    num_of_nodes = dfs(i)
    if num_of_edges // 2 != num_of_nodes:
        flag = False

if flag:
    print('Yes')
else:
    print('No')
