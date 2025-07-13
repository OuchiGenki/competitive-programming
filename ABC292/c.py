def cnt(n):
    res = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if n//i == i:
                res += 1
            else:
                res += 2
    return res

N = int(input())
ans = 0
for AB in range(1, N):
    CD = N - AB
    ans += cnt(AB) * cnt(CD)
print(ans)