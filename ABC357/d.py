n = int(input())
k = len(str(n))
MOD = 998244353

t = 10 ** k % MOD
inv = pow(t - 1, -1, MOD)
ans = n * (pow(t, n, MOD) - 1) * inv % MOD
print(ans)