import sys
sys.setrecursionlimit(10**8)

def bs(z):
    ng = -1
    ok = 2*10**6+1
    while ok-ng > 1:
        mid = (ok+ng)//2
        if mid*mid >= z:
            ok = mid
        else:
            ng = mid
    return ok

d = int(input())
ans = 10**12+10
for x in range(2*10**6+1):
    z = d-x*x
    y = bs(z)
    ans = min(min(abs(x*x+y*y-d),abs(x*x+(y-1)*(y-1)-d)), ans)

print(ans)
