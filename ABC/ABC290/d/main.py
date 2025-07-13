import math

t = int(input())
for i in range(t):
    n, d, k = map(int, input().split())
    g = math.gcd(n, d)
    p = n//g
    print((d*(k-1))%n + (k-1)//p)