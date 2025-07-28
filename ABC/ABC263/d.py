n, l, r = map(int, input().split())
A = list(map(int, input().split()))
dp = [[float('inf')] * 3 for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
    dp[i+1][0] = min(dp[i+1][0], dp[i][0] + l)
    dp[i+1][1] = min(dp[i+1][1], dp[i][0] + A[i])
    dp[i+1][1] = min(dp[i+1][1], dp[i][1] + A[i])
    dp[i+1][2] = min(dp[i+1][2], dp[i][0] + r)
    dp[i+1][2] = min(dp[i+1][2], dp[i][1] + r)
    dp[i+1][2] = min(dp[i+1][2], dp[i][2] + r)
print(min(dp[n]))
