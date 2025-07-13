import sys
sys.setrecursionlimit(10**8)

def dfs(x, y):
    seen.add((x, y))
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx, ny) not in xy:
            continue
        if (nx, ny) not in seen:
            dfs(nx, ny)

n = int(input())
xy = []
for i in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))
seen = set()
dx = [-1, -1, 0, 0, 1, 1]
dy = [-1, 0, -1, 1, 0, 1]

ans = 0
for i in range(n):
    if xy[i] not in seen:
        x, y = xy[i]
        dfs(x, y)
        ans += 1
print(ans)