from math import gcd
a, b, c = map(int, input().split())
l = gcd(a, gcd(b, c))
print(a//l + b//l + c//l - 3)