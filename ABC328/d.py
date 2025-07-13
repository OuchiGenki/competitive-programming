from collections import deque

S = input()
N = len(S)
d = deque()

for i in range(len(S)):
    d.appendleft(S[i])
    if len(d) >= 3 and d[0]+d[1]+d[2] == 'CBA':
        d.popleft()
        d.popleft()
        d.popleft()

print(''.join(reversed(list(d))))