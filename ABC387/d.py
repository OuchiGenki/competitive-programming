from collections import deque

H, W = map(int, input().split())
S = [input() for i in range(H)]
dist1 = [[float('inf')] * W for i in range(H)]
dist2 = [[float('inf')] * W for i in range(H)]
sy, sx, gy, gx = 0, 0, 0, 0
for i in range(H):
    for j in range(W):
        if S[i][j] == 'S':
            sy, sx = i, j
        if S[i][j] == 'G':
            gy, gx = i, j
dist1[sy][sx] = 0
dist2[sy][sx] = 0

que = deque([(sy, sx, 0)])
while que:
    y, x, op = que.popleft()
    if op == 0:
        d = [(1, 0), (-1, 0)]
    else:
        d = [(0, 1), (0, -1)]

    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue
        if dist1[ny][nx] != float('inf'):
            continue
        if S[ny][nx] == '#':
            continue
        dist1[ny][nx] = dist1[y][x] + 1
        que.append((ny, nx, op^1))

que = deque([(sy, sx, 1)])
while que:
    y, x, op = que.popleft()
    if op == 0:
        d = [(1, 0), (-1, 0)]
    else:
        d = [(0, 1), (0, -1)]

    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue
        if dist2[ny][nx] != float('inf'):
            continue
        if S[ny][nx] == '#':
            continue
        dist2[ny][nx] = dist2[y][x] + 1
        que.append((ny, nx, op^1))

if dist1[gy][gx] == dist2[gy][gx] == float('inf'):
    print(-1)
else:
    print(min(dist1[gy][gx], dist2[gy][gx]))
