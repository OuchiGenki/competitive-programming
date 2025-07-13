def f(x):
    cnt = 0
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            if i**2 == x:
                cnt += 1
            else:
                cnt += 2
    return cnt


N = int(input())
ans = 0
for AB in range(1, N):
    CD = N - AB
    ans += f(AB) * f(CD)
print(ans)