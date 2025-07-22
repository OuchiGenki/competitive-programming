n, m = map(int, input().split())
A = list(map(int, input().split()))
dp = [[-float('inf')] * (m+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(m+1):
        if j + 1 <= m:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + (j+1) * A[i])
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
print(dp[n][m])