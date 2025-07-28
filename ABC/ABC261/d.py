from collections import defaultdict

n, m = map(int, input().split())
X = list(map(int, input().split()))
bonus = defaultdict(int)
for _ in range(m):
    c, y = map(int, input().split())
    bonus[c] = y
dp = [[-float('inf')] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for j in range(n):
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + X[i] + bonus[j+1])
        dp[i+1][0] = max(dp[i+1][0], dp[i][j])
print(max(dp[n]))