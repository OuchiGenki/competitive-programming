from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(int)
now = 1
max_num = 0

for i in range(M):
    d[A[i]] += 1
    if d[A[i]] > max_num:
        now = A[i]
        max_num = d[A[i]]
    elif d[A[i]] == max_num and A[i] < now:
        now = A[i]
    print(now)