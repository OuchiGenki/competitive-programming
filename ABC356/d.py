n, m = map(int, input().split())
ans = 0
MOD = 998244353
for i in range(61):
    if not m & (1 << i):
        continue
    a = n // (2 ** i)
    b = n % (2 ** i)
    ans += (2 ** i) * (a // 2)
    if a % 2:
        ans += b + 1
    ans %= MOD
print(ans)