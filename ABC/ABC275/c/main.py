s = [input() for i in range(9)]
ans = 0
n = [i for i in range(9)]

ans = 0
for x1 in range(9):
    for y1 in range(9):
        for x2 in range(x1+1, 9):
            for y2 in range(y1, 9):
                if s[y1][x1]!="#" or s[y2][x2]!="#":
                    continue
                x3 = x2 - (y2 - y1)
                y3 = y2 + (x2 - x1)
                x4 = x1 - (y2 - y1)
                y4 = y1 + (x2 - x1)

                if min(x3,y3,x4,y4) < 0 or max(x3,y3,x4,y4) >= 9:
                    continue

                if s[y3][x3]=="#" and s[y4][x4]=="#":
                    ans += 1

print(ans)
