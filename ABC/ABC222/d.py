n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [[0] * (3001) for _ in range(n+1)]
MOD = 998244353
for i in range(A[0], B[0]+1):
    dp[1][i] = 1
for i in range(2, n+1):
    cum = [0]
    for j in range(3001):
        cum.append(cum[-1] + dp[i-1][j])
    for j in range(3001):
        if j < A[i-1] or B[i-1] < j:
            dp[i][j] = 0
            continue
        dp[i][j] += cum[j+1]
        dp[i][j] %= MOD
print(sum(dp[n]) % MOD)
        