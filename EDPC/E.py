inf = 1<<60

n, w = map(int, input().split())
dp = [[inf for i in range(10**5+1)] for j in range(n+1)]
dp[0][0] = 0

for i in range(n):
    nw, nv = map(int, input().split())
    for j in range(10**5+1):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        if j+nv > 10**5: continue
        dp[i+1][j+nv] = min(dp[i+1][j+nv], dp[i][j]+nw)

ans = 0
for i in range(10**5+1):
    if dp[n][i] <= w:
        ans = max(ans, i)
print(ans)