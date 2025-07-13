import sys
sys.setrecursionlimit(10**8)

n, m, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

cumB = [0]
for i in range(m):
    cumB.append(cumB[i]+b[i])

sub = 0
for i in range(n):
    ng = -1
    ok = m
    while (ok-ng)>1:
        mid = (ok+ng)//2
        if a[i]+b[mid] > p:
            ok = mid
        else:
            ng = mid
    
    sub += (a[i]*(m-ok))+(cumB[-1]-cumB[ok]) - p*(m-ok)

print(sum(a)*m + sum(b)*n - sub)