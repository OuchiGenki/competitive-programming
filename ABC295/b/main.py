import sys
sys.setrecursionlimit(10**8)

def f(x):
    if x!='.' and x!='#':
        return int(x)
    else:
        return x

def update(r1, c1, n):
    for r2 in range(r):
        for c2 in range(c):
            if abs(r1-r2) + abs(c1-c2) <= n:
                g[r2][c2] = '.'

r, c = map(int, input().split())
b = [list(map(f, input())) for i in range(r)]

g = [['.' for i in range(c)] for j in range(r)]
for i in range(r):
    for j in range(c):
        if b[i][j] == '#':
            g[i][j] = '#'

for i in range(r):
    for j in range(c):
        if b[i][j]!='.' and b[i][j]!='#':
            update(i, j, b[i][j])

for i in g:
    print(*i, sep="")