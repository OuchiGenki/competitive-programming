from collections import deque

N = int(input())
H = list(map(int, input().split()))
C = []
stack = deque()
for i in range(N):
    C.append(len(stack))
    while stack and H[N-i-1] > stack[0]:
        stack.popleft()
    stack.appendleft(H[N-i-1])
C.reverse()
print(*C)