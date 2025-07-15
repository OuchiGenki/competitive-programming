from collections import deque

n, m = map(int, input().split())
S = [input() for i in range(n)]

visited = [[False] * m for i in range(n)]
visited[1][1] = True
que = deque([(1, 1)])
res = [[False] * m for i in range(n)]

while que:
    y, x = que.popleft()
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ny, nx = y, x
        res[ny][nx] = True
        while S[ny+d[0]][nx+d[1]] != '#':
            ny += d[0]
            nx += d[1]
            res[ny][nx] = True
        if visited[ny][nx]:
            continue
        visited[ny][nx] = True
        que.append((ny, nx))

ans = 0
for i in range(n):
    for j in range(m):
        if res[i][j]:
            ans += 1
print(ans)