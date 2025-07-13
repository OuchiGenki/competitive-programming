from collections import deque

N, M, D = map(int, input().split())
A = deque(sorted(list(map(int, input().split()))))
B = deque(sorted(list(map(int, input().split()))))

while len(A) > 0 and len(B) > 0:
    if abs(A[-1] - B[-1]) <= D:
        print(A[-1] + B[-1])
        exit()
    if A[-1] < B[-1]:
        B.pop()
    else:
        A.pop()

print(-1)