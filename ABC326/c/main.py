import sys
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

def bs(x):
    ok = -1
    ng = n
    while (ng-ok)>1:
        mid = (ok+ng)//2
        if a[mid] < x:
            ok = mid
        else:
            ng = mid
    return ok

ans = 0
for x in a:
    idx1 = bs(x)
    idx2 = bs(x+m)
    ans = max(ans, idx2-idx1)

print(ans)