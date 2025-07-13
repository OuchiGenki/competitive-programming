import sys
sys.setrecursionlimit(10**8)

n, k, g = map(int, input().split())
li = [list(map(int, input().split())) for i in range(n)]
costs = []
p = []
for i in range(n):
    costs.append(li[i][0])
    p.append(li[i][1:])
    p[i].extend(100 for i in range(5-k))

dp = [[[[[[10**18 for a in range(6)] for b in range(6)] for c in range(6)] for d in range(6)] for e in range(6)] for f in range(n+1)]
dp[0][0][0][0][0][0] = 0

for a in range(n):
    for b in range(6):
        for c in range(6):
            for d in range(6):
                for e in range(6):
                    for f in range(6):
                        nb = min(5, b+p[a][0])
                        nc = min(5, c+p[a][1])
                        nd = min(5, d+p[a][2])
                        ne = min(5, e+p[a][3])
                        nf = min(5, f+p[a][4])
                        dp[a+1][b][c][d][e][f] = min(dp[a+1][b][c][d][e][f], dp[a][b][c][d][e][f])
                        dp[a+1][nb][nc][nd][ne][nf] = min(dp[a+1][nb][nc][nd][ne][nf], dp[a][b][c][d][e][f]+costs[a])

ans = 10**18
for a in range(g, 6):
    for b in range(g, 6):
        for c in range(g, 6):
            for d in range(g, 6):
                for e in range(g, 6):
                    ans = min(ans, dp[n][a][b][c][d][e])

if ans == 10**18:
    print(-1)
else:
    print(ans)