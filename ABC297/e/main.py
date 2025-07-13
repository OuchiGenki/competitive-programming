import sys
from heapq import *
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

q = [0]
ans = []

while len(ans) <= k:
    base = heappop(q)
    if len(ans) > 0 and  base == ans[-1]:
        continue
    ans.append(base)
    for i in range(n):
        heappush(q, base+a[i])

print(ans[k])