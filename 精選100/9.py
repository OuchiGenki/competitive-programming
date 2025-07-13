m = int(input())
sign = []
for i in range(m):
    x, y = map(int, input().split())
    sign.append((x, y))
n = int(input())
picture = set()
for i in range(n):
    x, y = map(int, input().split())
    picture.add((x, y))

search = []
for x2, y2 in picture:
    x1, y1 = sign[0]
    search.append((x2-x1, y2-y1))

for dx, dy in search:
    cnt = 0
    for x, y in sign:
        if (x+dx, y+dy) in picture:
            cnt += 1
    if cnt == m:
        print(dx, dy)
        exit()