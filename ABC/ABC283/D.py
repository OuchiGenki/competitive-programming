from collections import deque

S = input()
N = len(S)
stack = deque()
box = set()
for i in range(N):
    if ord('a') <= ord(S[i]) <= ord('z'):
        if S[i] in box:
            print('No')
            exit()
        stack.append(S[i])
        box.add(S[i])
    elif S[i] == '(':
        stack.append(S[i])
    elif S[i] == ')':
        while stack[-1] != '(':
            box.discard(stack[-1])
            stack.pop()
        stack.pop()

print('Yes')