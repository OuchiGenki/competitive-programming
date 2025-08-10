import heapq

n, m = map(int, input().split())
to = [[] for _ in range(n)]
deg = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    to[a - 1].append(b - 1)
    deg[b - 1] += 1
hq = []
for i in range(n):
    if deg[i] == 0:
        heapq.heappush(hq, i)
ans = []
while hq:
    v = heapq.heappop(hq)
    ans.append(v + 1)
    for nv in to[v]:
        deg[nv] -= 1
        if deg[nv] == 0:
            heapq.heappush(hq, nv)
if len(ans) != n:
    print(-1)
else:
    print(*ans)