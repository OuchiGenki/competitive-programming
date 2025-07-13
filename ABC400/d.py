from collections import deque

H, W = map(int, input().split())
S = [list(input()) for i in range(H)]
A, B, C, D = map(lambda x: int(x)-1, input().split())

deque = deque()
deque.append((A, B))
dist = [[float('inf')]*W for i in range(H)]
dist[A][B] = 0

while deque:
    y, x = deque.popleft()

    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ny, nx = y+dy, x+dx
        if 0 > ny or ny >= H or 0 > nx or nx >= W:
            continue
        if S[ny][nx] == "#" and dist[ny][nx] > dist[y][x]+1:
            deque.append((ny, nx))
            dist[ny][nx] = dist[y][x] + 1
        elif S[ny][nx] == "." and dist[ny][nx] > dist[y][x]:
            deque.appendleft((ny, nx))
            dist[ny][nx] = dist[y][x]
    
    for dy, dx in [(-2, 0), (0, 2), (2, 0), (0, -2)]:
        ny, nx = y+dy, x+dx
        if 0 > ny or ny >= H or 0 > nx or nx >= W:
            continue
        if S[ny][nx] == "#" and dist[ny][nx] > dist[y][x]+1:
            deque.append((ny, nx))
            dist[ny][nx] = dist[y][x] + 1

print(dist[C][D])
