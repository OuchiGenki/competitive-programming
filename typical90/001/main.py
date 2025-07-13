def isOK(x):
    cnt = 0
    pre = 0
    for i in range(n):
        if a[i] - pre >= x and l-a[i] >= x:
            cnt += 1
            pre = a[i]
    if cnt >= k:
        return True
    else:
        return False

n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))

ok = -1
ng = l+1
while ng-ok > 1:
    mid = (ok+ng) // 2
    if isOK(mid):
        ok = mid
    else:
        ng = mid
print(ok)