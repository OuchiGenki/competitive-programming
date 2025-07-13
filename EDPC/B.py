n, k = map(int, input().split())
h = list(map(int, input().split()))
dp = [10**9 for i in range(n)]
dp[0] = 0

for i in range(n):
    for k in range(1, k+1):
        if i+k >= n: continue
        dp[i+k] = min(dp[i+k], dp[i] + abs(h[i]-h[i+k]))

print(dp[n-1])