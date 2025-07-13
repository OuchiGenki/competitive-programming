from collections import deque

n, m = map(int, input().split())
a = [0 for i in range(n)]
cnt = [0 for i in range(n)]
g = [[] for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    g[x-1].append(y-1)
    cnt[y-1] += 1

q = deque()
for i in range(n):
    if cnt[i] == 0:
        q.append(i)

i = 1
while q:
    if len(q) > 1:
        print("No")
        exit()

    v = q.pop()
    a[v] = i
    i += 1

    for nv in g[v]:
        cnt[nv] -= 1
        if cnt[nv] == 0:
            q.append(nv)

print("Yes")
print(*a)