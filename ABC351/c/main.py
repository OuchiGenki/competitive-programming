from collections import deque

N = int(input())
A = list(map(int, input().split()))
d = deque()

for i in range(N):
    d.appendleft(A[i])
    while len(d) >= 2 and d[0] == d[1]:
        b1 = d.popleft()
        b2 = d.popleft()
        d.appendleft(b1 + 1)

print(len(d))