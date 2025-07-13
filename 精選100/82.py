l, r = map(int, input().split())
mod = 10**9+7
ie = pow(2, -1, 10**9+7)

ans = 0
for i in range(18):
    a = max(l, 10**i)
    b = min(r, 10**(i+1)-1)
    if a <= b:
        ans += (i+1)*(b-a+1)%mod*(a+b)%mod*ie%mod
        ans %= mod

print(ans)