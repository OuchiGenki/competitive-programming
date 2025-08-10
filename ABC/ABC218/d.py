from bisect import bisect_left

n = int(input())
XY = [list(map(int, input().split())) for _ in range(n)]
XY.sort()
ans = 0
for i in range(n):
    x1, y1 = XY[i]
    for j in range(i+1, n):
        x2, y2 = XY[j]
        if x1 == x2 or y1 == y2:
            continue
        idx1 = bisect_left(XY, [x1, y2])
        idx2 = bisect_left(XY, [x2, y1])
        if idx1 < n and idx2 < n and XY[idx1] == [x1, y2] and XY[idx2] == [x2, y1]:
            ans += 1
print(ans // 2)