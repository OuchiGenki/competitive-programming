def BS(key):
    def isOK(index):
        if s[index] <= key:
            return True
        else:
            return False
    
    ok, ng = -1, n+1
    while ng-ok > 1:
        mid = (ng+ok) // 2
        if isOK(mid):
            ok = mid
        else:
            ng = mid
    return ok

d = int(input())
n = int(input())
m = int(input())
s = [0] #shop
h = [] #house
for i in range(n-1):
    _ = int(input())
    s.append(_)
s.append(d)
s.sort()
for i in range(m):
    _ = int(input())
    h.append(_)

ans = 0
for i in range(m):
    x1 = BS(h[i])
    x2 = x1+1
    ans += min(abs(s[x1]-h[i]), abs(s[x2]-h[i]))

print(ans)