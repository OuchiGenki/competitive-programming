import sys
sys.setrecursionlimit(10**8)
mod = 998244353

n = int(input())
a = list(map(int, input().split()))

rn = pow(n, -1, mod)
dp = [rn for i in range(n)]
sum_p = 0
for i in range(n):
    dp[i] += sum_p*rn
    dp[i] %= mod
    sum_p += dp[i]
    sum_p %= mod

ans = 0
for i in range(n):
    ans += a[i]*dp[i]
    ans %= mod
print(ans)