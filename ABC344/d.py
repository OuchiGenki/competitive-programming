t = input()
n = int(input())
A, S = [], []
for i in range(n):
    lst = input().split()
    A.append(int(lst[0]))
    S.append(lst[1:])
dp = [[float('inf')] * (len(t) + 1) for i in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for j in range(len(t) + 1):
        for s in S[i]:
            if t[:j] + s == t[:j + len(s)]:
                dp[i + 1][j + len(s)] = min(dp[i + 1][j + len(s)], dp[i][j] + 1)
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])

if dp[n][len(t)] != float('inf'):
    print(dp[n][len(t)])
else:
    print(-1)
