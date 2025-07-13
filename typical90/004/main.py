h, w = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]
b = [[0 for i in range(w)] for j in range(h)]
yoko = []
for i in range(h):
    res = 0
    for j in range(w):
        res += a[i][j]
    yoko.append(res)
tate = []
for i in range(w):
    res = 0
    for j in range(h):
        res += a[j][i]
    tate.append(res)

for i in range(h):
    for j in range(w):
        b[i][j] = yoko[i] + tate[j] - a[i][j]

for i in b:
    print(*i)