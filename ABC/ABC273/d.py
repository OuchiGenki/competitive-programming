from bisect import bisect_left
from collections import defaultdict
from sortedcontainers import SortedSet

h, w, ty, tx = map(int, input().split())
n = int(input())
row = defaultdict(SortedSet)
col = defaultdict(SortedSet)
for _ in range(n):
    r, c = map(int, input().split())
    row[r].add(c)
    col[c].add(r)

q = int(input())
for _ in range(q):
    d, l = input().split()
    l = int(l)

    if d == 'L':
        idx = bisect_left(row[ty], tx)
        if idx == 0:
            min_x = 1
        else:
            min_x = row[ty][idx-1]+1
        tx = max(min_x, tx - l)
    elif d == 'R':
        idx = bisect_left(row[ty], tx)
        if idx == len(row[ty]):
            max_x = w
        else:
            max_x = row[ty][idx] - 1
        tx = min(max_x, tx + l)
    elif d == 'U':
        idx = bisect_left(col[tx], ty)
        if idx == 0:
            min_y = 1
        else:
            min_y = col[tx][idx-1]+1
        ty = max(min_y, ty - l)
    elif d == 'D':
        idx = bisect_left(col[tx], ty)
        if idx == len(col[tx]):
            max_y = h
        else:
            max_y = col[tx][idx] - 1
        ty = min(max_y, ty + l)
    print(ty, tx)