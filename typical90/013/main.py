import heapq

inf = 1<<60
n, m = map(int, input().split())
g = [[] for i in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    g[a-1].append([c, b-1])
    g[b-1].append([c, a-1])

def dijkstra(s):
    dist = [inf for i in range(n)]
    dist[s] = 0
    hq = []
    heapq.heappush(hq, [0, s])

    while hq:
        min_cost, v = heapq.heappop(hq)
        for cost, nv in g[v]:
            if dist[nv] > dist[v]+cost:
                dist[nv] = dist[v]+cost
                heapq.heappush(hq, [dist[nv], nv])
    
    return dist

dist1 = dijkstra(0)
distN = dijkstra(n-1)

for i in range(n):
    print(dist1[i] + distN[i])