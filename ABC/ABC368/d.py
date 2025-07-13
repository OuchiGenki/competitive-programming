import sys
sys.setrecursionlimit(10**8)


def dfs(v):
    cnt = 0
    visited[v] = True
    for nv in G[v]:
        if visited[nv]:
            continue
        cnt += dfs(nv)
    if v in S or cnt > 0:
        cnt += 1
    return cnt


N, K = map(int, input().split())
G = [[] for i in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
V = list(map(lambda x: int(x)-1, input().split()))
S = set(V)

visited = [False for i in range(N)]
ans = dfs(V[0])
print(ans)