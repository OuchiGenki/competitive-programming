n, k, d = map(int, input().split())
a = list(map(int, input().split()))

dp = [[[-1 for x in range(k+1)] for y in range(d)] for z in range(n+1)]
dp[0][0][0] = 0

for x in range(n):
    for y in range(d):
        for z in range(k+1):
            if dp[x][y][z] == -1:
                continue

            yy = (y + a[x]) % d
            if z<k:
                dp[x+1][yy][z+1] = max(dp[x+1][yy][z+1], dp[x][y][z] + a[x])
            dp[x+1][y][z] = max(dp[x+1][y][z], dp[x][y][z])

print(dp[n][0][k])