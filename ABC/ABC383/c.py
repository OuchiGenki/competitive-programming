import sys
from collections import deque
sys.setrecursionlimit(10**7)

H, W, D = map(int, input().split())
S = [list(input()) for _ in range(H)]

start = []
for i in range(H):
    for j in range(W):
        if S[i][j] == 'H':
            start.append([i, j])

queue = deque(start)
dist = [[-1 for i in range(W)] for j in range(H)]
for y, x in start:
    dist[y][x] = 0

while queue:
    y, x = queue.popleft()

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
        queue.append([ny, nx])

answer = 0
for i in range(H):
    for j in range(W):
        if 0 <= dist[i][j] <= D:
            answer += 1
print(answer)
