import sys 
sys.setrecursionlimit(10**8)

def dfs(y, x):
    visited[y][x] = True
    
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        ny, nx = y+dy, x+dx
        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue
        if S[ny][nx] == '.':
            continue
        if visited[ny][nx]:
            continue
        dfs(ny, nx)

H, W = map(int, input().split())
S = [input() for i in range(H)]

visited = [[False for i in range(W)] for j in range(H)]
ans = 0

for i in range(H):
    for j in range(W):
        if visited[i][j]:
            continue
        if S[i][j] == '#':
            ans += 1
            dfs(i, j)

print(ans)