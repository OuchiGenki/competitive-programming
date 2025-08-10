from collections import deque
n, a, b = map(int, input().split())
s = deque(input())
for i in range(a):
    s.popleft()
for i in range(b):
    s.pop()
print(''.join(s))