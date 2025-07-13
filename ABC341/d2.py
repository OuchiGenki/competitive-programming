from math import lcm

N, M, K = map(int, input().split())
ng, ok = 0, 10**18
while ok - ng > 1:
    mid = (ok + ng) // 2
    if mid // N + mid // M - (mid // lcm(N, M)) * 2 >= K:
        ok = mid
    else:
        ng = mid
print(ok)