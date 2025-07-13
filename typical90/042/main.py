k = int(input())
mod = 10**9+7
if k%9 == 0:
    dp = [0 for i in range(k+1)]
    dp[0] = 1

    for i in range(1, k+1):
        for j in range(1, 10):
            if i-j < 0:
                continue
            dp[i] += dp[i-j]
            dp[i] %= mod
    
    print(dp[k])

else:
    print(0)