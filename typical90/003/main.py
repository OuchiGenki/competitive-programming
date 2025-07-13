def bfs(s):
    q = deque()
    q.append(s)
    dist = [-1 for i in range(n)]
    dist[s] = 0
    np = 0
    while q:
        v = q.popleft()
        np = v
        for nv in g[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            q.append(nv)
    return (np, max(dist))

from collections import deque

n = int(input())
g = [[] for i in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

edge = bfs(0)[0]
print(bfs(edge)[1] + 1)