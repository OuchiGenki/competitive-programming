from collections import defaultdict
from sortedcontainers import SortedList
from bisect import bisect_left

n, k = map(int, input().split())
P = list(map(int, input().split()))
C = SortedList()
Z = defaultdict(int)
bottom = defaultdict(int)
ans = [-1] * n

for i in range(n):
    idx = bisect_left(C, P[i])
    if idx == len(C):
        C.add(P[i])
        Z[P[i]] = 1
    else:
        bottom[P[i]] = C[idx]
        Z[P[i]] = Z[C[idx]] + 1
        C.remove(C[idx])
        C.add(P[i])
    
    if Z[P[i]] == k:
        p = P[i]
        while True:
            ans[p-1] = i+1 
            p = bottom[p]
            if p == 0:
                break
        C.remove(P[i])

for a in ans:
    print(a)