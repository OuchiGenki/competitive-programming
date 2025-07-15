n = int(input())
s = input()
t = 'atcoder'
m = len(t)
MOD = 10**9 + 7
dp = [[0] * (m+1) for i in range(n+1)]
dp[0][0] = 1
for i in range(n):
    for j in range(m+1):
        if j < m and s[i] == t[j]:
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= MOD
        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= MOD
print(dp[n][m])