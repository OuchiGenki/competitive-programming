V, E = map(int, input().split())
INF = float("inf")
dist = [[INF for i in range(V)] for j in range(V)]
for i in range(E):
    s, t, d = map(int, input().split())
    dist[s][t] = d
for i in range(V):
    dist[i][i] = 0

for k in range(V):
    for u in range(V):
        for v in range(V):
            dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])
            
for i in range(V):
    for j in range(V):
        if dist[i][j] == INF:
            dist[i][j] = "INF"

flag = False
for i in range(V):
    if dist[i][i] < 0:
        flag = True

if flag:
    print("NEGATIVE CYCLE")
else:
    for i in dist:
        print(*i)