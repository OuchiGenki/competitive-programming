def isOK_A(index, key):
    if a[index] < key:
        return True
    else:
        return False
def isOK_C(index, key):
    if c[index] <= key:
        return True
    else:
        return False

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
c.sort()

ans = 0
resA = resC = 0
for key in b:
    ok, ng = -1, n
    while ng-ok > 1:
        mid = (ng+ok) // 2
        if isOK_A(mid, key):
            ok = mid
        else:
            ng = mid
    resA = ok+1

    ok, ng = -1, n
    while ng-ok > 1:
        mid = (ng+ok) // 2
        if isOK_C(mid, key):
            ok = mid
        else:
            ng = mid
    resC = n-ok-1

    ans += resA*resC

print(ans)