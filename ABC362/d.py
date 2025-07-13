import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
G  = [[] for i in range(N)]
for i in range(M):
    u, v, b = map(int, input().split())
    G[u-1].append((b, v-1))
    G[v-1].append((b, u-1))

q = []
heapq.heappush(q, (A[0], 0))
dist = [float('inf') for i in range(N)]
dist[0] = A[0]
cnf = [False for i in range(N)]

while q:
    w, v = heapq.heappop(q)
    if cnf[v]:
        continue
    cnf[v] = True
    for dw, nv in G[v]:
        if not cnf[nv] and dist[v] + dw + A[nv] < dist[nv]:
            dist[nv] = dist[v] + dw + A[nv]
            heapq.heappush(q, (dist[nv], nv))

print(*dist[1:])