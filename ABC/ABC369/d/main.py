import sys
sys.setrecursionlimit(10**8)

N = int(input())
A = list(map(int, input().split()))

dp = [[0 for i in range(2)] for j in range(N+1)]

for i in range(N):
    dp[i+1][0] = dp[i][0]
    dp[i+1][1] = dp[i][1]
    if i > 0:
        dp[i+1][0] = max(dp[i][0], dp[i][1] + 2*A[i])
    dp[i+1][1] = max(dp[i+1][1], dp[i][0] + A[i])

print(max(dp[N][0], dp[N][1]))
