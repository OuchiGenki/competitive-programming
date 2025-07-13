import sys
sys.setrecursionlimit(10**8)

def dfs(y, x, c):
    visited[y][x] = True

    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ny, nx = y + dy, x + dx
        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue
        if visited[ny][nx]:
            continue
        if snuke[c] != S[ny][nx]:
            continue
        dfs(ny, nx, snuke[c])


H, W = map(int, input().split())
S = [input() for _ in range(H)]

if S[0][0] != 's':
    print('No')
    exit()

snuke = {'s': 'n', 'n': 'u', 'u': 'k', 'k': 'e', 'e': 's'}
visited = [[False] * W for i in range(H)]

dfs(0, 0, 's')

if visited[H-1][W-1]:
    print('Yes')
else:
    print('No')