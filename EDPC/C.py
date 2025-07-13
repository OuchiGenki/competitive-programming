n = int(input())
a = []
b = []
c = []
for i in range(n):
    tmp1, tmp2, tmp3 = map(int, input().split())
    a.append(tmp1)
    b.append(tmp2)
    c.append(tmp3)

dp = [[0 for i in range(3)] for i in range(n)]
dp[0][0] = a[0]
dp[0][1] = b[0]
dp[0][2] = c[0]

for i in range(n):
    if i+1 >= n: continue
    for j in range(3):
        if j != 0: dp[i+1][0] = max(dp[i+1][0], dp[i][j]+a[i+1])
        if j != 1: dp[i+1][1] = max(dp[i+1][1], dp[i][j]+b[i+1])
        if j != 2: dp[i+1][2] = max(dp[i+1][2], dp[i][j]+c[i+1])

print(max(dp[n-1][0], dp[n-1][1], dp[n-1][2]))