import sys
from math import ceil
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n, m = map(int, input().split())
ans = 1<<60
for a in range(1, ceil(m**0.5)+1):
    b = ceil(m/a)
    if a*b >= m and a<=b<=n:
        ans = min(ans, a*b)

if ans == 1<<60:
    print(-1)
else:
    print(ans)