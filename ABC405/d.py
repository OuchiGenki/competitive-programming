from collections import deque

H, W = map(int, input().split())
S = [list(input()) for i in range(H)]
dist = [[-1 for i in range(W)] for j in range(H)]
path = [['.' for i in range(W)] for j in range(H)]

q = deque()
for i in range(H):
    for j in range(W):
        if S[i][j] == 'E':
            q.append((i, j))
            dist[i][j] = 0
            path[i][j] = 'E'
        if S[i][j] == '#':
            path[i][j] = '#'

while q:
    y, x = q.popleft()
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dy, dx in d:
        ny = y + dy
        nx = x + dx
        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue
        if S[ny][nx] == '#':
            continue
        if dist[ny][nx] != -1:
            continue

        dist[ny][nx] = dist[y][x] + 1
        if dy == -1 and dx == 0:
            path[ny][nx] = 'v'
        elif dy == 0 and dx == 1:
            path[ny][nx] = '<'
        elif dy == 1 and dx == 0:
            path[ny][nx] = '^'
        elif dy == 0 and dx == -1:
            path[ny][nx] = '>'
        q.append((ny, nx))

for row in path:
    print(''.join(row))
