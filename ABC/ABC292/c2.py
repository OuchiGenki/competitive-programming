def f(x):
    cnt = 0
    for i in range(1, int(x**0.5)+1):
        if x % i ==0:
            if x // i == i:
                cnt += 1
            else:
                cnt += 2
    return cnt

ans = 0
N = int(input())
for AB in range(1, N):
    CD = N - AB
    ans += f(AB) * f(CD)
print(ans)