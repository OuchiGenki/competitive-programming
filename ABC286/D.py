N, X = map(int, input().split())
dp = [[False] * (X+1) for i in range(N+1)]
dp[0][0] = True

for i in range(N):
    a, b = map(int, input().split())
    for j in range(X+1):
        if not dp[i][j]:
            continue
        for k in range(b+1):
            if j + a * k <= X:
                dp[i + 1][j + a * k] = True

if dp[N][X]:
    print('Yes')
else:
    print('No')