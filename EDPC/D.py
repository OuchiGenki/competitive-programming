N, W = map(int, input().split())
w = []
v = []
for i in range(N):
    tmp_w, tmp_v = map(int, input().split())
    w.append(tmp_w)
    v.append(tmp_v)

dp = [[0 for i in range(W+1)] for j in range(N+1)]

for i in range(N):
    nw = w[i]
    nv = v[i]
    for j in range(W):
        if j+nw <= W:
            dp[i+1][j+nw] = max(dp[i+1][j+nw], dp[i][j]+nv)
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])

ans = 0
for i in range(W+1):
    ans = max(ans, dp[N][i])
print(ans)