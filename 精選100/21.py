def isOK(lim):
    tl = []
    for i in range(n):
        tl.append((lim-h[i])//s[i])
    tl.sort()
    for i in range(n):
        if tl[i] < i:
            return False
    return True

n = int(input())
h = []
s = []
for i in range(n):
    a, b = map(int, input().split())
    h.append(a)
    s.append(b)

ng = -1
ok = 2**50
while ok-ng > 1:
    mid = (ng+ok)//2
    if isOK(mid):
        ok = mid
    else:
        ng = mid

print(ok)