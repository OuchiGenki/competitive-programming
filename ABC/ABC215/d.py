def f(x):
    res = set()
    for i in range(2, x):
        if i * i > x:
            break
        while x % i == 0:
            x //= i
            res.add(i)
    if x != 1:
        res.add(x)
    return res

n, m = map(int, input().split())
A = list(map(int, input().split()))
ans = set([i+1 for i in range(m)])
used = [False] * (10**5+1)

for a in A:
    primes = f(a)
    for p in primes:
        if a % p == 0 and not used[p]:
            i = 1
            while p * i <= m:
                ans.discard(p*i)
                i += 1
            used[p] = True

ans = list(ans)
ans.sort()
print(len(ans))
for row in ans:
    print(row)