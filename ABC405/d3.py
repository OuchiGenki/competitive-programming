from collections import deque
import copy

H, W = map(int, input().split())
S = [list(input()) for i in range(H)]
T = copy.deepcopy(S)
visited = [[False] * W for _ in range(H)]

queue = deque()
for i in range(H):
    for j in range(W):
        if S[i][j] == 'E':
            queue.append((i, j))
            visited[i][j] = True

while queue:
    y, x = queue.popleft()
    for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        ny = y + dy
        nx = x + dx
        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue
        if S[ny][nx] != '.':
            continue
        if visited[ny][nx]:
            continue

        if dy == -1 and dx == 0:
            T[ny][nx] = 'v'
        elif dy == 1 and dx == 0:
            T[ny][nx] = '^'
        elif dy == 0 and dx == 1:
            T[ny][nx] = '<'
        else:
            T[ny][nx] = '>'
        visited[ny][nx] = True
        queue.append((ny, nx))

for row in T:
    print(''.join(row))