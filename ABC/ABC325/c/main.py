import sys
sys.setrecursionlimit(10**8)

h, w = map(int, input().split())
s = [input() for i in range(h)]

seen = [[False for i in range(w)] for j in range(h)]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def dfs(i, j):
    seen[i][j] = True
    for a in range(8):
        ni = i+dy[a]
        nj = j+dx[a]
        if ni<0 or ni>=h or nj<0 or nj>=w:
            continue
        if s[ni][nj] == '.':
            continue
        if seen[ni][nj]:
            continue
        dfs(ni, nj)

ans = 0
for i in range(h):
    for j in range(w):
        if seen[i][j]:
            continue
        if s[i][j] == '.':
            continue
        ans += 1
        dfs(i, j)

print(ans)