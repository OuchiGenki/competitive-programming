k = int(input())
if k % 9:
    print(0)
    exit()
dp = [0] * (k+1)
dp[0] = 1
for i in range(1, k+1):
    for j in range(1, 10):
        if i - j < 0:
            continue
        dp[i] += dp[i-j]
        dp[i] %= 10**9 + 7
print(dp[k])