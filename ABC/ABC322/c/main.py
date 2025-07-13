import sys
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
a = list(map(int, input().split()))

def bs(i):
    ng = -1
    ok = m
    while ok-ng > 1:
        mid = (ok+ng)//2
        if i <= a[mid]:
            ok = mid
        else:
            ng = mid
    return a[ok]

for i in range(1, n+1):
    print(bs(i)-i)