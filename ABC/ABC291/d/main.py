n = int(input())
a = []
b = []
mod = 998244353
for i in range(n):
    tmpA, tmpB = map(int, input().split())
    a.append(tmpA)
    b.append(tmpB)
dp = [[0 for i in range(2)] for j in range(n+1)]

for i in range(n):
    if i == 0:
        dp[i+1][0] = 1
        dp[i+1][1] = 1
        
    if a[i-1] != a[i]:
        dp[i+1][0] += dp[i][0]
        dp[i+1][0] %= mod
    if a[i-1] != b[i]:
        dp[i+1][1] += dp[i][0]
        dp[i+1][0] %= mod
    if b[i-1] != a[i]:
        dp[i+1][0] += dp[i][1]
        dp[i+1][0] %= mod
    if b[i-1] != b[i]:
        dp[i+1][1] += dp[i][1]
        dp[i+1][0] %= mod

print((dp[n][0]+dp[n][1]) % mod)