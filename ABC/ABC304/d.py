from bisect import bisect_left
from collections import defaultdict

w, h = map(int, input().split())
n = int(input())
P, Q = [], []
for i in range(n):
    p, q = map(int, input().split())
    P.append(p)
    Q.append(q)
a = int(input())
A = list(map(int, input().split()))
b = int(input())
B = list(map(int, input().split()))

cnt = defaultdict(int)
for i in range(n):
    xi = bisect_left(A, P[i])
    yi = bisect_left(B, Q[i])
    cnt[(xi, yi)] += 1
if len(cnt) < (a+1) * (b+1):
    cnt[-1] = 0

print(min(cnt.values()), max(cnt.values()))
