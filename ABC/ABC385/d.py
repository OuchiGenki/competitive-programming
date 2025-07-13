from sortedcontainers import SortedSet
from collections import defaultdict
from bisect import bisect_left

N, M, sx, sy = map(int, input().split())
row = defaultdict(SortedSet)
col = defaultdict(SortedSet)
for i in range(N):
    x, y = map(int, input().split())
    row[y].add(x)
    col[x].add(y)

px, py = sx, sy
ans = 0
for i in range(M):
    d, c = input().split()
    c = int(c)
    if d == 'U':
        idx = bisect_left(col[px], py)
        visited = []
        while idx < len(col[px]) and col[px][idx] <= py+c:
            ny = col[px][idx]
            visited.append((px, ny))
            ans += 1
            idx += 1
        for x, y in visited:
            row[y].discard(x)
            col[x].discard(y)
        py += c
    elif d == 'D':
        idx = bisect_left(col[px], py-c)
        visited = []
        while idx < len(col[px]) and col[px][idx] <= py:
            ny = col[px][idx]
            visited.append((px, ny))
            ans += 1
            idx += 1
        for x, y in visited:
            row[y].discard(x)
            col[x].discard(y)
        py -= c
    elif d == 'L':
        idx = bisect_left(row[py], px-c)
        visited = []
        while idx < len(row[py]) and row[py][idx] <= px:
            nx = row[py][idx]
            visited.append((nx, py))
            ans += 1
            idx += 1
        for x, y in visited:
            row[y].discard(x)
            col[x].discard(y)
        px -= c
    elif d == 'R':
        idx = bisect_left(row[py], px)
        visited = []
        while idx < len(row[py]) and row[py][idx] <= px+c:
            nx = row[py][idx]
            visited.append((nx, py))
            ans += 1
            idx += 1
        for x, y in visited:
            row[y].discard(x)
            col[x].discard(y)
        px += c

print(px, py, ans)