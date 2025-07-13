mod = 10**9+7
n = int(input())
s = input()
b = "atcoder"
dp = [[0 for i in range(8)] for j in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1

for i in range(n):
    for j in range(7):
        if s[i] == b[j]:
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= mod
        dp[i+1][j+1] += dp[i][j+1]
        dp[i+1][j+1] %= mod

print(dp[n][7])