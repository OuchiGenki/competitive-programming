from collections import deque

def distance(x1, y1, x2, y2):
    return (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)

n, m = map(int, input().split())

x = []
y = []
d = []
for i in range(-n, n+1):
    for j in range(-n, n+1):
        if distance(0, 0, j, i) == m:
            x.append(j)
            y.append(i)
            d.append([j, i])

dist = [[0 for i in range(n+1)] for j in range(n+1)]

que = deque()
que.append([1, 1])

while que:
    x, y = que.popleft()
    for dx, dy in d:
        if x+dx<1 or x+dx>n or y+dy<1 or y+dy>n:
            continue
        if dist[y+dy][x+dx] != 0:
            continue
        if y+dy==1 and x+dx==1:
            continue
        dist[y+dy][x+dx] = dist[y][x] + 1
        que.append([x+dx, y+dy])

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 and j==1: continue
        if dist[i][j] == 0:
            dist[i][j] = -1

for i in range(1, n+1):
    for j in range(1, n+1):
        if j < n:
            print(dist[i][j], end=" ")
        else:
            print(dist[i][j])