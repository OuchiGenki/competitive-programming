def f(a, n, m):
    if n == 0:
        return 0

    res = f(a, n//2, m)
    if n%2 == 0:
        return (res + res*pow(a, n//2, m)) % m
    else:
        return (res + res*pow(a, n//2, m) + pow(a, n-1, m)) % m

a, x, m = map(int, input().split())
print(f(a, x, m))