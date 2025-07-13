import sys
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
g = [[] for i in range(n)]
ans = [[10**18, 10**18] for i in range(n)]

for i in range(m):
    a, b, x, y = map(int, input().split())
    g[a-1].append([b-1,x,y])
    g[b-1].append([a-1,-x,-y])

def dfs(v, x, y):
    ans[v] = [x, y]
    for li in g[v]:
        nv = li[0]
        nx = x+li[1]
        ny = y+li[2]
        if ans[nv] != [10**18, 10**18]:
            continue
        dfs(nv, nx, ny)

dfs(0, 0, 0)

for i in range(n):
    ansX = ans[i][0]
    ansY = ans[i][1]
    if ans[i][0]==10**18:
        print("undecidable")
    else:
        print(*ans[i])