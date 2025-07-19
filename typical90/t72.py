import sys
sys.setrecursionlimit(10**8)

h, w = map(int, input().split())
C = [input() for _ in range(h)]
ans = -1

def dfs(y, x, sy, sx, depth):
    global ans
    visited[y][x] = True
    for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ny, nx = y + d[0], x + d[1]
        if ny < 0 or ny >= h or nx < 0 or nx >= w:
            continue
        if C[ny][nx] == '#':
            continue
        if visited[ny][nx]:
            if ny == sy and nx == sx and depth >= 3:
                ans = max(ans, depth+1)
            continue
        dfs(ny, nx, sy, sx, depth + 1)
    visited[y][x] = False

visited = [[False] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if C[i][j] == '#':
            continue
        dfs(i, j, i, j, 0)

print(ans)