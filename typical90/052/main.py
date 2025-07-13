n = int(input())
a = [list(map(int, input().split())) for j in range(n)]
mod = 10**9+7
ans = 1
for i in range(n):
    ans *= sum(a[i])
    ans %= mod
print(ans)