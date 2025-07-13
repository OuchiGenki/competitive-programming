X, Y, Z = map(int, input().split())
S = input()
N = len(S)
dp = [[float('inf')] * 2 for i in range(N+1)]
dp[0][0] = 0

for i in range(N):
    if S[i] == 'a':
        dp[i+1][0] = min(dp[i+1][0], dp[i][0] + X)
        dp[i+1][0] = min(dp[i+1][0], dp[i][1] + Z + X)
        dp[i+1][1] = min(dp[i+1][1], dp[i][1] + Y)
        dp[i+1][1] = min(dp[i+1][1], dp[i][0] + Z + Y)
    elif S[i] == 'A':
        dp[i+1][1] = min(dp[i+1][1], dp[i][1] + X)
        dp[i+1][1] = min(dp[i+1][1], dp[i][0] + Z + X)
        dp[i+1][0] = min(dp[i+1][0], dp[i][0] + Y)
        dp[i+1][0] = min(dp[i+1][0], dp[i][1] + Z + Y)

print(min(dp[N][0], dp[N][1]))