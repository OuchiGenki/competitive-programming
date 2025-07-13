n, l = map(int, input().split())

dp = [0 for i in range(n+1)]
dp[0] = 1
mod = 10**9+7

for i in range(n):
    dp[i+1] += dp[i]
    dp[i+1] %= mod
    if i+l <= n:
        dp[i+l] += dp[i]
        dp[i+l] %= mod

print(dp[n])

