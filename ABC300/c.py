import sys
sys.setrecursionlimit(10**8)

def dfs(y, x):
    visited[y][x] = True
    cnt = 0

    for dy, dx in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        ny, nx = y + dy, x + dx
        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue
        if visited[ny][nx]:
            continue
        if C[ny][nx] == '.':
            continue
        cnt += dfs(ny, nx)
    
    cnt += 1
    return cnt


H, W = map(int, input().split())
C = [input() for i in range(H)]
ans = [0 for i in range(min(H, W))]

visited = [[False for i in range(W)] for j in range(H)]
for i in range(H):
    for j in range(W):
        if visited[i][j]:
            continue
        if C[i][j] == '.':
            continue
        res = dfs(i, j)
        size = (res - 1) // 4
        ans[size-1] += 1

print(*ans)