s = input()
n = len(s)
MOD = 998244353
if n % 2 == 1:
    print(0)
    exit()
dp = [[0] * (n+1) for i in range(n+1)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if s[i] =='(':
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= MOD
        elif s[i] == ')':
            if i+1-j > j:
                continue
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= MOD
        elif s[i] == '?':
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= MOD
            if i+1-j > j:
                continue
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= MOD

print(dp[n][n//2])
