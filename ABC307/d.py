from collections import deque

N = int(input())
S = input()
stack = deque()
cnt = 0

for i in range(N):
    if S[i] == '(':
        stack.append(S[i])
        cnt += 1
    elif S[i] == ')':
        if cnt:
            while stack[-1] != '(':
                stack.pop()
            stack.pop()
            cnt -= 1
        else:
            stack.append(S[i])
    else:
        stack.append(S[i])

print(''.join(stack))