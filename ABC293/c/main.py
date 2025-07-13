import sys
sys.setrecursionlimit(10**8)

def dfs(y, x, s):
    global ans
    s.add(a[y][x])
    if y==h-1 and x==w-1:
        ans += 1
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= w or ny < 0 or ny >= h:
            continue
        if a[ny][nx] in s:
            continue
        dfs(ny, nx, s)
    s.remove(a[y][x])

h, w = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]

s = set()
dx = [1, 0]
dy = [0, 1]
ans = 0
dfs(0, 0, s)
print(ans)