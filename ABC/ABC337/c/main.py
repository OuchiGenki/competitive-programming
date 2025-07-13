from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)

for i in range(N):
    if A[i] == -1:
        start = i+1
    else:
        d[A[i]] = i+1

v = start
ans = []
for i in range(N):
    ans.append(v)
    v = d[v]

print(*ans)