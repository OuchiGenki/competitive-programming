import sys
sys.setrecursionlimit(10**8)

def dfs(v):
    visited[v] = True
    for nv in g[v]:
        if visited[nv]:
            continue
        dfs(nv)
        dp[v] += dp[nv]

n = int(input())
g = [[] for i in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

dp = [1 for i in range(n)]
visited = [False for i in range(n)]
dfs(0)

ans = 0
for i in range(n):
    ans += dp[i]*(n-dp[i])

print(ans)