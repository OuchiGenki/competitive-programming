import heapq

V, E, r = map(int, input().split())
G = [[] for i in range(V)]
for i in range(E):
    s, t, d = map(int, input().split())
    G[s].append((t, d))
    
    
def dijk(s):
    dist = [10**12 for i in range(V)]
    dist[s] = 0
    cnf = [False for i in range(V)]     #confirm
    q = [(dist[s], s)]

    while q:
        d, v = heapq.heappop(q)
        if cnf[v]:
            continue
        cnf[v] = True
        for nv, weight in G[v]:
            if not cnf[nv] and dist[v]+weight < dist[nv]:
                dist[nv] = dist[v] + weight
                heapq.heappush(q, (dist[nv], nv))
    
    return dist

ans = dijk(r)

for i in ans:
    if i == 10**12:
        print("INF")
    else:
        print(i)