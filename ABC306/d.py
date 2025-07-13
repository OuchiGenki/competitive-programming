N = int(input())
dp = [[0, 0] for i in range(N+1)]

for i in range(N):
    x, y = map(int, input().split())
    if x == 0:
        dp[i+1][0] = max(dp[i+1][0], dp[i][0] + y)
        dp[i+1][0] = max(dp[i+1][0], dp[i][1] + y)
    elif x == 1:
        dp[i+1][1] = max(dp[i+1][0], dp[i][0] + y)
    dp[i+1][0] = max(dp[i+1][0], dp[i][0])
    dp[i+1][1] = max(dp[i+1][1], dp[i][1])

print(max(dp[N][0], dp[N][1]))
