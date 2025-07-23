from collections import defaultdict

n = int(input())
TX = set()
A = defaultdict(int)
for _ in range(n):
    t, x, a = map(int, input().split())
    TX.add((t, x))
    A[(t, x)] = a

dp = [[-float('inf')] * 5 for _ in range(10**5 + 1)]
dp[0][0] = 0

for i in range(10**5):
    for j in range(5):
        if (i+1, j-1) in TX:
            dp[i+1][j-1] = max(dp[i+1][j-1], dp[i][j] + A[(i+1, j-1)])
        else:
            if j - 1 >= 0:
                dp[i+1][j-1] = max(dp[i+1][j-1], dp[i][j])
        if (i+1, j) in TX:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + A[(i+1, j)])
        else:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if (i+1, j+1) in TX:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + A[(i+1, j+1)])
        else:
            if j + 1 <= 4:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])

print(max(dp[10**5]))