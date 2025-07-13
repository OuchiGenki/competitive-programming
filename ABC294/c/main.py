def isOK(index, key):
    if c[index] <= key:
        return True
    else:
        return False

def binary(key):
    ok = -1
    ng = n+m
    while (ng-ok) > 1:
        mid = (ok+ng)//2
        if isOK(mid, key):
            ok = mid
        else:
            ng = mid
    return ok

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = a+b
c.sort()

ansA, ansB = [], []
for i in range(n):
    ansA.append(binary(a[i])+1)
for i in range(m):
    ansB.append(binary(b[i])+1)

print(*ansA)
print(*ansB)