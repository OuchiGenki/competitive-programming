n = int(input())
x, y = map(int, input().split())
dp = [[[float('inf')] * 301 for i in range(301)] for j in range(n+1)]
dp[0][0][0] = 0
for i in range(n):
    a, b = map(int, input().split())
    for j in range(301):
        nj = min(j+a, 300)
        for k in range(301):
            nk = min(k+b, 300)
            dp[i+1][nj][nk] = min(dp[i+1][nj][nk], dp[i][j][k] + 1)
            dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
ans = float('inf')
for i in range(x, 301):
    for j in range(y, 301):
        ans = min(ans, dp[n][i][j])
if ans == float('inf'):
    print(-1)
else:
    print(ans)