from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
d = defaultdict(int)
base = 0
for i in range(N):
    d[i] = A[i]

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        base = query[1]
        d = defaultdict(int)
    elif query[0] == 2:
        i, x = query[1], query[2]
        d[i-1] += x
    else:
        i = query[1]
        print(base + d[i-1])