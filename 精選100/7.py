def calc(x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1
    return dx*dx + dy*dy

n = int(input())
xy = set()
for i in range(n):
    x, y = map(int, input().split())
    xy.add((x, y))

ans = 0
for x1, y1 in xy:
    for x2, y2 in xy:
        if x2>=x1 and y2<y1:
            dx = x2-x1
            dy = y1-y2
            x3 = x2-dy
            y3 = y2-dx
            x4 = x1-dy
            y4 = y1-dx
            if (x3, y3) in xy and (x4, y4) in xy:
                ans = max(ans, calc(x1, y1, x2, y2))
print(ans)