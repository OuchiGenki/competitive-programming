import math

def f(x):
    return x + p*(2**(-x/1.5))
def fd(x):
    return 1 - p*(2/3)*math.log(2)*2**(-(2/3)*x)

def isOK(x):
    if fd(x) >= 0:
        return True
    else:
        return False

p = float(input())
ng = float(-1)
ok = float(10**18+1)
while ok-ng > 10**(-10):
    mid = (ng+ok) / 2
    if isOK(mid):
        ok = mid
    else:
        ng = mid

if ok<0:
    print(p)
else:
    print(f(ok))