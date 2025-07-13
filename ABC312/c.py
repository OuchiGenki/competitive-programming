from bisect import bisect_right, bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

ng = -1
ok = 10**9 + 1
while (ok - ng) > 1:
    x = (ok + ng) // 2
    if bisect_right(A, x) - (M - bisect_left(B, x)) >= 0:
        ok = x
    else:
        ng = x

print(ok)