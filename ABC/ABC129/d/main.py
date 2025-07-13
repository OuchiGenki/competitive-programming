h, w = map(int, input().split())
s = [input() for i in range(h)]

r = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
    pre = 0
    cnt = 0
    for j in range(w):
        if s[i][j] == '#':
            for k in range(pre, j):
                r[i][k] = cnt
            pre = j+1
            cnt = 0
        else:
            cnt += 1
    for k in range(pre, w):
        r[i][k] = cnt

c = [[0 for i in range(w)] for j in range(h)]
for i in range(w):
    pre = 0
    cnt = 0
    for j in range(h):
        if s[j][i] == '#':
            for k in range(pre, j):
                c[k][i] = cnt
            pre = j+1
            cnt = 0
        else:
            cnt += 1
    for k in range(pre, h):
        c[k][i] = cnt

ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            ans = max(ans, r[i][j]+c[i][j]-1)
print(ans)