import heapq

h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
P = list(map(int, input().split()))

dist = [[float('inf')] * w for _ in range(h)]
cnf = [[False] * w for _ in range(h)]
hq = [(0, 0, 0)]
dist[0][0] = 0

for i in range(h):
    for j in range(w):
        A[i][j] = P[i+j]-A[i][j]
print()
for i in A:
    print(*i)
print()
while hq:
    c, y, x = heapq.heappop(hq)
    print(c, y, x)
    if cnf[y][x]:
        continue
    cnf[y][x] = True
    for d in [(0, 1), (1, 0)]:
        ny, nx = y + d[0], x + d[1]
        if ny < 0 or ny >= h or nx < 0 or nx >= w:
            continue
        if cnf[ny][nx]:
            continue
        if y + x + 1 >= h + w - 1:
            continue
        if dist[y][x] + A[y][x] < dist[ny][nx]:
            dist[ny][nx] = c + A[y][x]
            heapq.heappush(hq, (c+A[y][x], ny, nx))

for row in dist:
    print(*row)