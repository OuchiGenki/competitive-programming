from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
base = 0
d = defaultdict(int)
for i in range(N):
    d[i] = A[i]

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        base = x
        d = defaultdict(int)
    elif query[0] == 2:
        i, x = query[1]-1, query[2]
        d[i] += x
    else:
        i = query[1]-1
        print(base + d[i])