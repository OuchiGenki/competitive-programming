import sys
sys.setrecursionlimit(10**8)

a, b, c = map(int, input().split())
if b>c:
    c += 24
if b>a:
    a += 24

if b < a < c:
    print("No")
else:
    print("Yes")