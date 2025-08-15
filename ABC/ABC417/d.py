n = int(input())
PAB = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * 1001 for _ in range(n+1)]
for i in range(1001):
    dp[n][i] = i
for i in range(n-1, -1, -1):
    p, a, b = PAB[i]
    for j in range(1001):
        if p >= j:
            dp[i][j] = dp[i+1][j+a]
        else:
            dp[i][j] = dp[i+1][max(0, j-b)]

cum = [0]
for i in range(n):
    _, _, b = PAB[i]
    cum.append(cum[-1] + b)

def bs(x):
    ng = -1
    ok = n+1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if x - cum[mid] <= 1000:
            ok = mid
        else:
            ng = mid
    return ok

q = int(input())
for _ in range(q):
    x = int(input())
    if x <= 1000:
        print(dp[0][x])
    else:
        idx = bs(x)
        if idx == n+1:
            print(x - cum[n])
        else:
            x = max(0, x - cum[idx])
            print(dp[idx][x])
