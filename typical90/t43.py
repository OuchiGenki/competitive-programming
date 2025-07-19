from collections import deque

h, w = map(int, input().split())
rs, cs = map(lambda x: int(x)-1, input().split())
rt, ct = map(lambda x: int(x)-1, input().split())
S = [input() for _ in range(h)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

que = deque()
dist = [[[float('inf')] * 4 for i in range(w)] for j in range(h)]
for i in range(4):
    que.append((rs, cs, i))
    dist[rs][cs][i] = 0

while que:
    y, x, d = que.popleft()
    cur_dist = dist[y][x][d]
    for nd in range(4):
        if (d + 2) % 4 == nd:
            continue
        ny, nx = y + dir[nd][0], x + dir[nd][1]
        if ny < 0 or ny >= h or nx < 0 or nx >= w:
            continue
        if S[ny][nx] == '#':
            continue
        if d == nd:
            if dist[ny][nx][nd] > cur_dist:
                dist[ny][nx][nd] = cur_dist
                que.appendleft((ny, nx, nd))
        else:
            if dist[ny][nx][nd] > cur_dist + 1:
                dist[ny][nx][nd] = cur_dist + 1
                que.append((ny, nx, nd))

print(min(dist[rt][ct]))
for row in dist:
    print(*row)