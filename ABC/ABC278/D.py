from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)
for i, a in enumerate(A):
    d[i] = a
Q = int(input())
base = 0
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        base = x
        d = defaultdict(int)
    elif query[0] == 2:
        i, x = query[1], query[2]
        d[i-1] += x
    else:
        i = query[1]
        print(d[i-1] + base)