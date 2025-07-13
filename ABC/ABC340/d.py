import heapq

N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    a, b, x = map(int, input().split())
    G[i].append((a, i+1))
    G[i].append((b, x-1))

q = [(0, 0)]
cnf = [False for i in range(N)]
dist = [float('inf') for i in range(N)]
dist[0] = 0
while q:
    w, v = heapq.heappop(q)
    if cnf[v]:
        continue
    cnf[v] = True
    for nw, nv in G[v]:
        if cnf[nv]:
            continue
        if dist[v] + nw < dist[nv]:
            dist[nv] = dist[v] + nw
            heapq.heappush(q, (dist[v] + nw, nv))

print(dist[N-1])