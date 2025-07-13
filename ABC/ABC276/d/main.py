n = int(input())
a = list(map(int, input().split()))

def cnt(n, x):
    res = 0
    while n%x==0:
        res += 1
        n //= x
    return res

xyz = []
minx = 1<<60
miny = 1<<60
for i in range(n):
    x = cnt(a[i], 2)
    a[i] //= 2**x
    y = cnt(a[i], 3)
    a[i] //= 3**y
    z = a[i]
    minx = min(minx, x)
    miny = min(miny, y)
    xyz.append([x, y, z])

for i in range(n):
    if xyz[0][2] != xyz[i][2]:
        print(-1)
        exit()

ans = 0
for i in range(n):
    ans += xyz[i][0]-minx
    ans += xyz[i][1]-miny
print(ans)