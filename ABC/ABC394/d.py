from collections import deque

S = input()
N = len(S)
deque = deque()

for i in range(N):
    if S[i] in ['(', '[', '<']:
        deque.appendleft(S[i])
    else:
        if not deque:
            print('No')
            exit()
        if S[i]==')' and deque[0]=='(':
            deque.popleft()
        elif S[i]==']' and deque[0]=='[':
            deque.popleft()
        elif S[i]=='>' and deque[0]=='<':
            deque.popleft()

if not deque:
    print('Yes')
else:
    print('No')
