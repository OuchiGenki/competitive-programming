from collections import defaultdict
from math import gcd

def C2(n):
    return n * (n-1) // 2

n = int(input())
XY = [list(map(int, input().split())) for _ in range(n)]
A = defaultdict(int)
B = defaultdict(int)
for i in range(n):
    x1, y1 = XY[i]
    for j in range(i+1, n):
        x2, y2 = XY[j]
        dx, dy = x2 - x1, y2 - y1
        if dx == 0:
            dy = 1
        elif dy == 0:
            dx = 1
        else:
            g = gcd(abs(dx), abs(dy))
            if dx < 0:
                dx, dy = -dx, -dy
            dx //= g
            dy //= g
        A[(dx, dy)] += 1
        B[((x1+x2)/2, (y1+y2)/2)] += 1
        
A = list(A.values())
B = list(B.values())
ans = 0
m = 0
for i in range(len(A)):
    ans += C2(A[i])
for i in range(len(B)):
    ans -= C2(B[i])

print(ans)