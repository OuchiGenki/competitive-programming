V, E = map(int, input().split())
G = [[] for i in range(V)]
for j in range(E):
    s, t, w = map(int, input().split())
    G[s].append((t, w))
    G[t].append((s, w))

import heapq

marked = [False for _ in range(V)]
marked_cnt = 0

marked[0] = True
marked_cnt += 1

q = []

for v, w in G[0]:
    heapq.heappush(q, (w, v))
    
total = 0
    
while marked_cnt < V:
    w, v = heapq.heappop(q)
    
    if marked[v]:
        continue
    
    marked[v] = True
    marked_cnt += 1
    total += w
    
    for nv, nw in G[v]:
        heapq.heappush(q, (nw, nv))

print(total)
    