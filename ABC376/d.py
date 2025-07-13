from collections import deque

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)

dist = [-1] * N
dist[0] = 0
queue = deque([0])

while queue:
    v = queue.popleft()
    for nv in G[v]:
        if nv == 0:
            print(dist[v]+1)
            exit()
        if dist[nv] == -1:
            dist[nv] = dist[v] + 1
            queue.append(nv)

print(-1)