from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
cnt = defaultdict(int)
for i in range(n):
    cnt[A[i]] += 1
V = list(cnt.values())
dp = [[0] * 4 for _ in range(len(V) + 1)]
dp[0][0] = 1
for i in range(len(V)):
    for j in range(4):
        dp[i+1][j] += dp[i][j]
        if j < 3:
            dp[i+1][j+1] += dp[i][j] * V[i]
print(dp[len(V)][3])
