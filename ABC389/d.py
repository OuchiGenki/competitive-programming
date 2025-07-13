R = int(input())

def bs(x):
    ok = 0
    ng = R+1
    while ng-ok > 1:
        y = (ok+ng)//2
        if (y+0.5)**2 <= R**2 - (x+0.5)**2:
            ok = y
        else:
            ng = y
    
    return ok

res = (R-1)*4 + 1
cnt = 0

for i in range(1, R):
    cnt += bs(i)

res += cnt*4
print(res)