N, M = map(int, input().split())
W = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    W[a-1][b-1] = c
    W[b-1][a-1] = c

dp = [[0 for i in range(N)] for j in range(2**N)]

for i in range(N):
    dp[1 << i][i] = 0

for i in range(1, 2**N):
    for j in range(N):
        if not (i & (1 << j)):
            continue
        for k in range(N):
            if i & (1 << k):
                continue
            if W[j][k] == 0:
                continue
            dp[i|(1<<k)][k] = max(dp[i|(1<<k)][k], dp[i][j] + W[j][k])

ans = 0
for i in range(2**N):
    ans = max(ans, max(dp[i]))
print(ans)