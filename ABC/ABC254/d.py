from collections import defaultdict

def eratosthenes(n):
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
primes = eratosthenes(n)
cnt = defaultdict(int)
for i in range(1, n + 1):
    x = i
    now = 1
    for p in primes:
        if p * p > x:
            break
        y = 0
        while x % p == 0:
            x //= p 
            y += 1
        if y % 2:
            now *= p
    now *= x
    cnt[now] += 1

ans = n
for v in cnt.values():
    ans += v * (v-1)
print(ans)