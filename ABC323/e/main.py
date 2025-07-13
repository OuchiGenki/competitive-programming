import sys
sys.setrecursionlimit(10**8)

n, x = map(int, input().split())
t = list(map(int, input().split()))

mod = 998244353

dp = [0 for i in range(x+1)]
dp[0] = 1
#dp[i][0] = 1*pow(n,-1,mod) #始まる確率
rn = pow(n, -1, mod)

for i in range(x+1):
    for j in t:
        if i-j < 0:
            continue
        dp[i] += dp[i-j]*rn
    dp[i] %= mod
        
ans = 0
for i in range(t[0]):
    if x-i < 0:
        continue
    ans += dp[x-i]*rn
    ans %= mod
print(ans)
