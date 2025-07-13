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


N = int(input())
prime_list = eratosthenes(10**7 + 1)
ans = 0
for x in range(100):
    if prime_list[x] ** 8 <= N:
        ans += 1

right = len(prime_list) - 1
for left in range(10**3+1):
    p = prime_list[left]
    while left < right and p**2 * prime_list[right-1]**2 > N:
        right -= 1
    if right - left <= 1:
        break
    ans += right - left - 1

print(ans)