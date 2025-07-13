def check(w):
    global M

    cnt = 1
    p = 0
    for i in range(N):
        if L[i] > w:
            return False

        if p + L[i] <= w:
            p += L[i] + 1
        else:
            cnt += 1
            p = L[i]+1
    
    if cnt <= M:
        return True
    else:
        return False
    
        
N, M = map(int, input().split())
L = list(map(int, input().split()))

ng = 0
ok = 10**18
while ok-ng > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)