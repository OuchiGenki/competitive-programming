from collections import deque

N1, N2, M = map(int, input().split())
G = [[] for i in range(N1 + N2)]
for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

q = deque([0, N1 + N2 - 1])
dist = [-1] * (N1 + N2)
dist[0] = 0
dist[N1 + N2 - 1] = 0
visited = [False] * (N1 + N2)

while q:
    v = q.popleft()
    visited[v] = True

    for nv in G[v]:
        if dist[nv] != -1:
            continue
        dist[nv] = dist[v] + 1
        q.append(nv)

res1 = max(dist[:N1])
res2 = max(dist[N1:])
print(res1 + res2 + 1)