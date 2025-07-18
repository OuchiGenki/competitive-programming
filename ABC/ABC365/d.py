N = int(input())
S = input()
dp = [[0 for i in range(3)] for j in range(N+1)]

for i in range(N):
    if S[i] == 'S':
        dp[i+1][0] = max(dp[i+1][0], dp[i][1]+1)
        dp[i+1][0] = max(dp[i+1][0], dp[i][2]+1)
    elif S[i] == 'R':
        dp[i+1][0] = max(dp[i+1][0], dp[i][1])
        dp[i+1][0] = max(dp[i+1][0], dp[i][2])
    if S[i] == 'P':
        dp[i+1][1] = max(dp[i+1][1], dp[i][0] + 1)
        dp[i+1][1] = max(dp[i+1][1], dp[i][2] + 1)
    elif S[i] == 'S': 
        dp[i+1][1] = max(dp[i+1][1], dp[i][0])
        dp[i+1][1] = max(dp[i+1][1], dp[i][2])
    if S[i] == 'R':
        dp[i+1][2] = max(dp[i+1][2], dp[i][0] + 1)
        dp[i+1][2] = max(dp[i+1][2], dp[i][1] + 1)
    elif S[i] == 'P':
        dp[i+1][2] = max(dp[i+1][2], dp[i][0])
        dp[i+1][2] = max(dp[i+1][2], dp[i][1])

print(max(dp[N]))