def dist(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2

n = int(input())
ab = []
for i in range(n):
    A, B = map(int, input().split())
    ab.append((A, B))
cd = []
for i in range(n):
    C, D = map(int, input().split())
    cd.append((C, D))
ab.sort(reverse=True, key=lambda x: x[1])
cd.sort()

red = [False for i in range(n)]
blue = [False for i in range(n)]
ans = 0
for i in range(n):
    if blue[i]:
        continue

    xb=cd[i][0]
    yb=cd[i][1]

    for j in range(n):
        if red[j]:
            continue

        xr=ab[j][0]
        yr=ab[j][1]

        if xr<xb and yr<yb:
            ans += 1
            red[j] = True
            blue[i] = True
            break

print(ans)