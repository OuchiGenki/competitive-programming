from collections import deque

def bfs(r, c):
    dist = [[-1] * w for i in range(h)]
    dist[r][c] = 0
    que = deque([(r, c)])
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while que:
        y, x = que.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue
            if A[ny][nx] == '#':
                continue
            if dist[ny][nx] != -1:
                continue
            dist[ny][nx] = dist[y][x] + 1
            que.append((ny, nx))
    return dist

def bfs2(s):
    dist = [-1] * n
    dist[s] = 0
    que = deque([s])
    while que:
        v = que.popleft()
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            que.append(nv)
    return dist

h, w = map(int, input().split())
A = [input() for _ in range(h)]
sy, sx, gy, gx = -1, -1, -1, -1
for i in range(h):
    for j in range(w):
        if A[i][j] == 'S':
            sy, sx = i, j
        if A[i][j] == 'T':
            gy, gx = i, j
n = int(input())
R, C, E = [], [], []
for i in range(n):
    r, c, e = map(int, input().split())
    R.append(r-1)
    C.append(c-1)
    E.append(e)
R.append(sy)
C.append(sx)
E.append(0)
R.append(gy)
C.append(gx)
E.append(0)
n += 2

G = [[] for i in range(n)]
for i in range(n):
    dist = bfs(R[i], C[i])
    for j in range(n):
        if i == j:
            continue
        if dist[R[j]][C[j]] != -1 and dist[R[j]][C[j]] <= E[i]:
            G[i].append(j)

dist = bfs2(n-2)
if dist[n-1] != -1:
    print('Yes')
else:
    print('No')
