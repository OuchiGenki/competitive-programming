n = int(input())
A = list(map(int, input().split()))
dp = [[0] * 10 for _ in range(n)]
dp[0][A[0]] = 1
MOD = 998244353
for i in range(n-1):
    for j in range(10):
        dp[i+1][(j + A[i+1]) % 10] += dp[i][j]
        dp[i+1][(j * A[i+1]) % 10] += dp[i][j]
        dp[i+1][(j + A[i+1]) % 10] %= MOD
        dp[i+1][(j * A[i+1]) % 10] %= MOD
for i in range(10):
    print(dp[n-1][i])