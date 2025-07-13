k = int(input())

def prime_fact(n):
    res = []
    for i in range(2, n):
        if i*i > n: break
        if n%i != 0: continue
        cnt = 0
        while n%i == 0:
            cnt += 1
            n //= i
        res.append((i, cnt))
    res.append((n, 1))
    return res

res = prime_fact(k)

def factorial(n):
    if n==1: return 1
    return n * factorial(n-1)

ans = 1
for a, b in res:
    cnt = 0
    for i in range(a, a*b+1, a):
        num = i
        while num%a == 0:
            cnt += 1
            num //= a
            if cnt >= b:
                ans = max(ans, i)
                break
        if cnt >= b:
            break

print(ans)