from collections import deque

n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    g[u-1].append(v-1)

cnt = 0
for i in range(n):
    visited = [False for i in range(n)]
    visited[i] = True
    q = deque()
    q.append(i)

    while q:
        v = q.popleft()
        for nv in g[v]:
            if visited[nv]:
                continue
            cnt += 1
            visited[nv] = True
            q.append(nv)

print(cnt-m)