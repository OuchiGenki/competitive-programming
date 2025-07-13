def bs(x):
    ok = 0
    ng = R
    while ng - ok > 1:
        y = (ok + ng) // 2
        if (x+0.5)**2 + (y+0.5)**2 <= R**2:
            ok = y
        else:
            ng = y
    return ok


R = int(input())
ans = 1 + (R-1)*4
for i in range(1, R):
    x = i
    y_max = bs(x)
    ans += y_max * 4
print(ans)