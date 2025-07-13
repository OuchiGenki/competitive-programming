N = int(input())

def bs(a):
    ok = 0
    ng = 10**9+1
    while (ng-ok) > 1:
        b = (ok+ng)//2
        if 2**a * b**2 <= N:
            ok = b
        else:
            ng = b
    return ok

ans = 0
for a in range(1, 100):
    b = bs(a)
    if 2**a *b**2 <= N:
        ans += int((b+1)/2)

print(ans)
