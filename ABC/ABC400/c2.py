def bs(a):
    global N
    ok = 0
    ng = 10**9
    while ng - ok > 1:
        b = (ok + ng) // 2
        if 2**a * b**2 <= N:
            ok = b
        else:
            ng = b
    return ok

N = int(input())
a = 1
ans = 0
while 2**a <= N:
    ans += (bs(a)+1) // 2
    a += 1
print(ans)