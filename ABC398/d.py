from collections import defaultdict

N, R, C = map(int, input().split())
S = input()

exists = defaultdict(tuple)
exists[(0, 0)] = True
cy, cx = 0, 0
py, px = R, C
answer = []

for i in range(N):
    if S[i] == 'N':
        py += 1
        cy += 1
        if exists[(py, px)]:
            answer.append('1')
        else:
            answer.append('0')
        exists[(cy, cx)] = True

    if S[i] == 'W':
        px += 1
        cx += 1
        if exists[(py, px)]:
            answer.append('1')
        else:
            answer.append('0')
        exists[(cy, cx)] = True
    if S[i] == 'S':
        py -= 1
        cy -= 1
        if exists[(py, px)]:
            answer.append('1')
        else:
            answer.append('0')
        exists[(cy, cx)] = True
    if S[i] == 'E':
        px -= 1
        cx -= 1
        if exists[(py, px)]:
            answer.append('1')
        else:
            answer.append('0')
        exists[(cy, cx)] = True

print(''.join(answer))
