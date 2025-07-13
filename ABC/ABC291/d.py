N = int(input())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
dp = [[0]*2 for i in range(N+1)]
dp[1][0] = 1
dp[1][1] = 1

for i in range(1, N):
    if A[i-1] != A[i]:
        dp[i+1][0] += dp[i][0]
    if B[i-1] != A[i]:
        dp[i+1][0] += dp[i][1]
    if A[i-1] != B[i]:
        dp[i+1][1] += dp[i][0]
    if B[i-1] != B[i]:
        dp[i+1][1] += dp[i][1]
    dp[i+1][0] %= 998244353
    dp[i+1][1] %= 998244353

print((dp[N][0] + dp[N][1]) % 998244353) 