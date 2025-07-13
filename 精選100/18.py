n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

def isOK(key, index):
    if S[index] <= key:
        return True
    else:
        return False

ans = 0
for i in range(q):
    key = T[i]
    ok = -1
    ng = n
    while ng-ok > 1:
        mid = (ng+ok) // 2
        if isOK(key, mid):
            ok = mid
        else:
            ng = mid
    if S[ok] == key:
        ans += 1

print(ans)