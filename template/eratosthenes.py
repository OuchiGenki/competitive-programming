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