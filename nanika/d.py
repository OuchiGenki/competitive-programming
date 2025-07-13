def isOK(a, b, index):
    c = l[index]
    if c<a+b:
        return True
    else:
        return False

n = int(input())
l = list(map(int, input().split()))
l.sort()

ans = 0
for i in range(n):
    for j in range(i, n):
        if i == j:
            continue
        a = l[i]
        b = l[j]
        if l[len(l)-1] <= abs(a-b):
            continue
        ok = j
        ng = n
        while (ng-ok) > 1:
            mid = (ok+ng)//2
            if isOK(a,b,mid):
                ok = mid
            else:
                ng = mid
        if ok > j:
            ans += ok-j
print(ans)