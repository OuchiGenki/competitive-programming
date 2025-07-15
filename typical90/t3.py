from collections import deque

n = int(input())
G = [[] for i in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

que = deque([0])
dist = [-1] * n
dist[0] = 0
while que:
    v = que.popleft()
    for nv in G[v]:
        if dist[nv] != -1:
            continue
        dist[nv] = dist[v] + 1
        que.append(nv)

s = dist.index(max(dist))
que = deque([s])
dist = [-1] * n
dist[s] = 0
while que:
    v = que.popleft()
    for nv in G[v]:
        if dist[nv] != -1:
            continue
        dist[nv] = dist[v] + 1
        que.append(nv)

print(max(dist) + 1)