import sys
sys.setrecursionlimit(10**7)

def dfs(x):
    seen[x] = True
    if x == y-1:
        return
    for nx in g[x]:
        if seen[nx]:
            continue
        path[nx] = x
        dfs(nx)

n, x, y = map(int, input().split())
g = [[] for i in range(n)]
for i in range(n-1):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

path = [-1 for i in range(n)]
seen = [False for i in range(n)]
dfs(x-1)

ans = []
pos = y-1
while pos != x-1:
    ans.append(path[pos]+1)
    pos = path[pos]

ans.reverse()
ans.append(y)
print(*ans)