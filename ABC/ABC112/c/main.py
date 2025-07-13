n = int(input())
xyh = []
si = -1
for i in range(n):
    x, y, h = map(int, input().split())
    if h > 0:
        si = i
    xyh.append((x, y, h))

ans = []
for cx in range(101):
    for cy in range(101):
        flag = True
        H = xyh[si][2] + abs(xyh[si][0]-cx) + abs(xyh[si][1]-cy)
        for i in range(n):
            x = xyh[i][0]
            y = xyh[i][1]
            h = xyh[i][2]
            if h>0 and H!=(h+abs(x-cx)+abs(y-cy)):
                flag = False
            if h==0 and H-abs(x-cx)-abs(y-cy) > 0:
                flag = False
        if flag:
            print(cx, cy, H)
            exit()