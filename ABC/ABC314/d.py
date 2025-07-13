N = int(input())
S = list(input())
Q = int(input())

cng = []
init = []
for i in range(Q):
    t, x, c = input().split()
    t, x = int(t), int(x)

    if t == 1:
        cng.append((i, x-1, c))
    elif t == 2:
        init.append((i, 'lower'))
    elif t == 3:
        init.append((i, 'upper'))

if len(init) > 0:
    opr_idx, opr = init[-1]
else:
    opr_idx, opr = -1, None

for i in range(N):
    if opr == 'lower':
        S[i] = S[i].lower()
    elif opr == 'upper':
        S[i] = S[i].upper()
    else:
        continue

for i in range(len(cng)):
    cng_idx, t, c = cng[i]
    if cng_idx > opr_idx:
        S[t] = c
    else:
        if opr == 'lower':
            S[t] = c.lower()
        elif opr == 'upper':
            S[t] = c.upper()

print(''.join(S))
