import sys
sys.setrecursionlimit(10**7)

H, W, K = map(int, input().split())
S = [list(input()) for i in range(H)]

def dfs(y, x, depth):
    global K, ans

    if depth == K:
        ans += 1
        visited[y][x] = False
        return

    visited[y][x] = True
    
    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ny = y + dy
        nx = x + dx
        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue
        if S[ny][nx] == '#':
            continue
        if visited[ny][nx]:
            continue
        dfs(ny, nx, depth+1)
    
    visited[y][x] = False

ans = 0
visited = [[False] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        dfs(i, j, 0)

print(ans)