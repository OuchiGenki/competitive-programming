T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    S = list(map(int, input()))
    dp = [[float('inf') for i in range(3)] for j in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        dp[i+1][0] = min(dp[i+1][0], dp[i][0] + abs(S[i]-0))
        dp[i+1][1] = min(dp[i+1][1], dp[i][0] + abs(S[i]-1))
        dp[i+1][1] = min(dp[i+1][1], dp[i][1] + abs(S[i]-1))
        dp[i+1][2] = min(dp[i+1][2], dp[i][0] + abs(S[i]-0))
        dp[i+1][2] = min(dp[i+1][2], dp[i][1] + abs(S[i]-0))
        dp[i+1][2] = min(dp[i+1][2], dp[i][2] + abs(S[i]-0))
    ans.append(min(dp[N][0], dp[N][1], dp[N][2]))

for i in ans:
    print(i)