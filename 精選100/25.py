import sys
sys.setrecursionlimit(10**8)

def dfs(y, x):
    seen[y][x] = True
    for i in range(8):
        ny = y+dy[i]
        nx = x+dx[i]
        if ny<0 or ny>=h or nx<0 or nx>=w:
            continue
        if seen[ny][nx]:
            continue
        if c[ny][nx] == 0:
            continue
        dfs(ny, nx)

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
ans = []
while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    c = []
    for i in range(h):
        c.append(list(map(int, input().split())))
    cnt = 0
    seen = [[False for i in range(w)] for j in range(h)]
    for i in range(h):
        for j in range(w):
            if seen[i][j]:
                continue
            if c[i][j] == 0:
                continue
            dfs(i, j)
            cnt += 1
    
    ans.append(cnt)

for i in ans:
    print(i)