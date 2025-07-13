import copy
from collections import deque

H, W = map(int, input().split())
S = [list(input()) for i in range(H)]
T = copy.deepcopy(S)
visited = [[False] * W for i in range(H)]
que = deque()
for i in range(H):
    for j in range(W):
        if S[i][j] == 'E':
            que.append((i, j))
            visited[i][j] = True

while que:
    y, x = que.popleft()
    for ny, nx, char in [(y+1, x, '^'), (y-1, x, 'v'), (y, x+1, '<'), (y, x-1, '>')]:
        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue
        if S[ny][nx] == '#':
            continue
        if visited[ny][nx]:
            continue
        visited[ny][nx] = True
        T[ny][nx] = char
        que.append((ny, nx))

for row in T:
    print(''.join(row))
