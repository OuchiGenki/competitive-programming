from collections import deque

H, W = map(int, input().split())
S = [list(input()) for i in range(H)]
q = deque()
for i in range(H):
    for j in range(W):
        if S[i][j] == 'E':
            q.append((i, j))

visited = [[False for i in range(W)] for j in range(H)]

while q:
    y, x = q.popleft()

    for ny, nx in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue
        if visited[ny][nx]:
            continue
        if S[ny][nx] != '.':
            continue

        if ny == y+1:
            S[ny][nx] = '^'
        elif ny == y-1:
            S[ny][nx] = 'v'
        elif nx == x+1:
            S[ny][nx] = '<'
        else:
            S[ny][nx] = '>'

        visited[y][x] = True
        q.append((ny, nx))

for row in S:
    print(''.join(row))
