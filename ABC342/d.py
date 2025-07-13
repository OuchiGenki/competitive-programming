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
A = list(map(int, input().split()))
primes = eratosthenes(2 * 10 ** 5)
cnt = [0 for i in range(2 * 10 ** 5 + 1)]
zero = 0
for i in range(n):
    if A[i] == 0:
        zero += 1
        continue
    res = 1
    for p in primes:
        if p * p > A[i]:
            break
        x = 0
        while A[i] % p == 0:
            A[i] //= p
            x += 1
        y = x % 2
        res *= p ** y
    res *= A[i]
    cnt[res] += 1

not_zero = n - zero
ans = n * (n-1) // 2 - not_zero * (not_zero - 1) // 2
for i in range(2 * 10 ** 5 + 1):
    ans += cnt[i] * (cnt[i] - 1) // 2
print(ans)