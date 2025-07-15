def is_OK(x):
    cnt = 0
    now = 0
    for i in range(n):
        if A[i] - now >= x:
            cnt += 1
            now = A[i]
    if l - now >= x:
        cnt += 1
    return cnt >= k+1


n, l = map(int, input().split())
k = int(input())
A = list(map(int, input().split()))

ok = -1
ng = l+1
while ng - ok > 1:
    mid = (ok + ng) // 2
    if is_OK(mid):
        ok = mid
    else:
        ng = mid

print(ok)