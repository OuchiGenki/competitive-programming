N, R, C = map(int, input().split())
S = input()
cy, cx = 0, 0
py, px = R, C
exists = set()
exists.add((0, 0))
ans = ''

for i in range(N):
    if S[i] == 'N':
        py += 1
        cy += 1
    elif S[i] == 'W':
        px += 1
        cx += 1
    elif S[i] == 'S':
        py -= 1
        cy -= 1
    elif S[i] == 'E':
        px -= 1
        cx -= 1
    exists.add((cy, cx))

    if (py, px) in exists:
        ans += '1'
    else:
        ans += '0'

print(ans)