from collections import deque

n, m = map(int, input().split())
g = [[] for i in range(n)]
deg = [0 for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    g[x-1].append(y-1)
    deg[y-1] += 1

q = deque()
for i in range(n):
    if deg[i] == 0:
        q.append(i)

a = [0 for i in range(n)]
cnt = 1
while len(q):
    if len(q) > 1:
        print("No")
        exit()
    v = q.popleft()
    a[v] = cnt
    cnt += 1
    for nv in g[v]:
        deg[nv] -= 1
        if deg[nv] == 0:
            q.append(nv)

print("Yes")
print(*a)