import sys
sys.setrecursionlimit(10**7)

def dfs(v):
    visited[v] = True
    for nv in g[v]:
        if visited[nv]:
            continue
        dfs(nv)
    vs.append(v)

def rdfs(v):
    global res
    res += 1
    visited[v] = True
    for nv in rg[v]:
        if visited[nv]:
            continue
        rdfs(nv)

n, m = map(int, input().split())
g = [[] for i in range(n)]
rg = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    rg[b-1].append(a-1)

vs = []
visited = [False for i in range(n)]
for i in range(n):
    if visited[i]==False:
        dfs(i)

visited = [False for i in range(n)]
cnt = []
for i in range(n-1, -1, -1):
    if visited[vs[i]]==False:
        res = 0
        rdfs(vs[i])
        cnt.append(res)

ans = 0
for i in cnt:
    ans += i*(i-1)//2
print(ans)