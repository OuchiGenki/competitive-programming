import sys
sys.setrecursionlimit(10**8)

def dfs(y, x, S):
    global ans
    if y == H-1 and x == W-1:
        ans += 1
        return
    
    visited[y][x] = True

    for ny, nx in [(y+1, x), (y, x+1)]:
        if ny >= H or nx >= W:
            continue
        if visited[ny][nx]:
            continue
        if A[ny][nx] in S:
            continue
        dfs(ny, nx, S | set([A[ny][nx]]))
    
    visited[y][x] = False


H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]
visited = [[False] * W for i in range(H)]
ans = 0
dfs(0, 0, set([A[0][0]]))
print(ans)