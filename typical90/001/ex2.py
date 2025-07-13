def check(x1, y1, r1, x2, y2, r2):
    d = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
    if r1+r2 <= d:
        return True
    else:
        return False

def isOK(key):
    res = True
    for i in range(n+m):
        for j in range(n+m):
            if i == j:
                continue
            if i >= n:
                xyr[i][2] = key
            if j >= n:
                xyr[j][2] = key
            if check(*xyr[i], *xyr[j]) == False:
                res = False
    return res

n, m = map(int, input().split())
xyr = []
min_r = 1<<60
for i in range(n):
    x, y, r = map(int, input().split())
    min_r = min(min_r, r)
    xyr.append([x, y, r])
for i in range(m):
    x, y = map(int, input().split())
    xyr.append([x, y, 0])
if m == 0:
    print(min_r)
    exit()

ok = -1
ng = 1000
while ng - ok > 10**(-10):
    mid = (ok+ng) / 2
    if isOK(mid):
        ok = mid
    else:
        ng = mid
print(ok)