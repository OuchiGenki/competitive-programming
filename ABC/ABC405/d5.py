from collections import deque
import copy

H, W = map(int, input().split())
S = [list(input()) for i in range(H)]
T = copy.deepcopy(S)
visited = [[False] * W for i in range(H)]
q = deque()
for i in range(H):
    for j in range(W):
        if S[i][j] == 'E':
            q.append((i, j))
            visited[i][j] = True

while q:
    y, x = q.popleft()
    for ny, nx, c in [(y+1, x, '^'), (y-1, x, 'v'), (y, x+1, '<'), (y, x-1, '>')]:
        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue
        if S[ny][nx] != '.':
            continue
        if visited[ny][nx]:
            continue

        visited[ny][nx] = True
        T[ny][nx] = c
        q.append((ny, nx))

for row in T:
    print(''.join(row))