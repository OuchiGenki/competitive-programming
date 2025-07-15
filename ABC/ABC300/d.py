def sieve(n):
    primes = [True] * (n+1)
    primes[0] = False
    primes[1] = False
    for p in range(2, int(n**0.5) + 1):
        if not primes[p]:
            continue
        for i in range(p ** 2, n+1, p):
            primes[i] = False
    return [i for i in range(n+1) if primes[i]]

n = int(input())
primes = sieve(10**6)
m = len(primes)
cum = [0 for i in range(10**6+1)]
for p in primes:
    cum[p] = 1
for i in range(10**6):
    cum[i+1] += cum[i]
ans = 0

for ai in range(m):
    a = primes[ai]
    if a**5 >= n:
        break
    for bi in range(ai+1, m):
        b = primes[bi]
        if a**2 * b**3 >= n:
            break
        r = int((n/a/a/b) ** 0.5)
        if r < b:
            break
        ans += cum[r] - cum[b]


print(ans)