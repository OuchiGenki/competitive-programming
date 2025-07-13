import sys
sys.setrecursionlimit(10**8)

def dfs(x, s):
    global v, e
    v += 1
    visited[x] = True
    for nx in g[x]:
        e += 1
        if visited[nx]:
            continue
        dfs(nx, s)

n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

visited = [False for i in range(n)]
flag = True
for i in range(n):
    if visited[i]:
        continue
    v = 0
    e = 0
    dfs(i, i)
    if 2*v != e:
        flag = False

if flag:
    print("Yes")
else:
    print("No")