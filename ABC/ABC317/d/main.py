n = int(input())
all_z = 0
dp = [[float('inf')] * (10**5 + 1) for i in range(n+1)]
dp[0][0] = 0
for i in range(n):
    x, y, z = map(int, input().split())
    all_z += z
    cost = max(0, (y - x) // 2 + 1)
    for j in range(10**5 + 1):
        if j + z <= 10**5:
            dp[i+1][j+z] = min(dp[i+1][j+z], dp[i][j] + cost)
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        
ans = float('inf')
for i in range(10**5+1):
    if i >= all_z // 2 + 1:
        ans = min(ans, dp[n][i])
if ans == float('inf'):
    print(0)
else:
    print(ans)