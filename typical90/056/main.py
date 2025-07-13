n, s = map(int, input().split())
a, b = [], []
for i in range(n):
    A, B = map(int, input().split())
    a.append(A); b.append(B)

dp = [[False for i in range(s+1)] for j in range(n+1)]
dp[0][0] = True

for i in range(n):
    for j in range(s):
        if not dp[i][j]:
            continue
        if j+a[i] <= s:
            dp[i+1][j+a[i]] = True
        if j+b[i] <= s:
            dp[i+1][j+b[i]] = True

if not dp[n][s]:
    print("Impossible")
    exit()

p = s
ans = []
for i in range(n, 0, -1):
    if p-a[i-1] >= 0 and dp[i-1][p-a[i-1]]:
        ans.append('A')
        p = p-a[i-1]
    elif p-b[i-1] >= 0 and dp[i-1][p-b[i-1]]:
        ans.append('B')
        p = p-b[i-1]

ans.reverse()
print(*ans, sep="")