from bisect import bisect_right

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
cumsum = [0]
for i in range(N):
    cumsum.append(cumsum[i] + A[i])

if cumsum[-1] <= M:
    print('infinite')
    exit()

def bs():
    ok = -1
    ng = 10**10
    while ng-ok > 1:
        mid = (ok+ng)//2
        tmp = 0
        for i in range(N):
            tmp += min(A[i], mid)
        if tmp <= M:
            ok = mid
        else:
            ng = mid
    return ok

max_x = bs()
print(max_x)
