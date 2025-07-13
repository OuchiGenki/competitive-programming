n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b)
    g[b-1].append(a)

for i in range(n):
    g[i].sort()
    print(len(g[i]), *g[i])