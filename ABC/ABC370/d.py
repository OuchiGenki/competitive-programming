from sortedcontainers import SortedSet
from bisect import bisect_left

H, W, Q = map(int, input().split())
wall = [[True] * W for i in range(H)]
row = [SortedSet([i for i in range(W)]) for _ in range(H)]
col = [SortedSet([i for i in range(H)]) for _ in range(W)]

for i in range(Q):
    r, c = map(lambda x: int(x)-1, input().split())
    if wall[r][c]:
        wall[r][c] = False
        row[r].discard(c)
        col[c].discard(r)
    else:
        if row[r]:
            x = bisect_left(row[r], c)
            if 0 <= x < len(row[r]):
                p = row[r][x]
                wall[r][p] = False
                row[r].discard(p)
                col[p].discard(r)
            if 0 <= x-1 < len(row[r]):
                p = row[r][x-1]
                wall[r][p] = False
                row[r].discard(p)
                col[p].discard(r)

        if col[c]:
            y = bisect_left(col[c], r)
            if 0 <= y < len(col[c]):
                p = col[c][y]
                wall[p][c] = False
                row[p].discard(c)
                col[c].discard(p)
            if 0 <= y-1 < len(col[c]):
                p = col[c][y-1]
                wall[p][c] = False
                row[p].discard(c)
                col[c].discard(p)
    
ans = 0
for i in range(H):
    for j in range(W):
        if wall[i][j]:
            ans += 1
print(ans)