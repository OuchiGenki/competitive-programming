from collections import deque

n, x, y = map(int, input().split())
g = [[] for i in range(n)]
for i in range(n-1):
    g[i].append(i+1)
    g[i+1].append(i)
g[x-1].append(y-1)
g[y-1].append(x-1)

ans = [set() for i in range(n)]
for i in range(n):
    q = deque()
    q.append(i)
    dist = [-1 for i in range(n)]
    dist[i] = 0
    while q:
        v = q.popleft()
        for nv in g[v]:
            if dist[nv] < 0:
                dist[nv] = dist[v]+1
                if i <= nv:
                    ans[dist[nv]].add((i+1,nv+1))
                q.append(nv)

for i in range(1, n):
    print(len(ans[i]))