from collections import deque

n, x = map(int, input().split())
S = input()
stack = deque()
for i in range(n):
    if S[i] == 'U':
        if stack and stack[0] != 'U':
            stack.popleft()
        else:
            stack.appendleft('U')
    else:
        stack.appendleft(S[i])
stack.reverse()
for c in stack:
    if c == 'U':
        x //= 2
    elif c == 'L':
        x = x * 2
    elif c == 'R':
        x = x * 2 + 1
print(x)