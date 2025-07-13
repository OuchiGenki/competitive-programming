from bisect import bisect_left, bisect_right

def f(b, k, x):
    if bisect_right(A, b+x) - bisect_left(A, b-x) >= k:
        return True
    else:
        return False

def solve(b, k):
    ok = 10**9
    ng = -1
    while (ok-ng) > 1:
        mid = (ok + ng) // 2
        if f(b, k, mid):
            ok = mid
        else:
            ng = mid
    print(ok)

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
for i in range(Q):
    b, k = map(int, input().split())
    solve(b, k)