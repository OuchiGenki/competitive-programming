import sys
sys.setrecursionlimit(10**8)

def P(n):
    if n == 0:
        return 1
    else:
        return n * P(n-1)

def C(n, r):
    return P(n) // (P(r) * P(n - r))

def solve(a, b, k):
    if a == 0:
        return 'b' * b
    elif b == 0:
        return 'a' * a
    else:
        if k <= C(a+b-1, a-1):
            return 'a' + solve(a-1, b, k)
        else:
            return 'b' + solve(a, b-1, k - C(a+b-1, a-1))

a, b, k = map(int, input().split())
print(solve(a, b, k))