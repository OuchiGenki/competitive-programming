from math import lcm

N, M, K = map(int, input().split())
lcm_NM = lcm(N, M)

ng = 0
ok = 10**18
while ok - ng > 1:
    mid = (ok + ng) // 2
    if mid // N + mid // M - (mid // lcm_NM)*2 >= K:
        ok = mid
    else:
        ng = mid

print(ok)