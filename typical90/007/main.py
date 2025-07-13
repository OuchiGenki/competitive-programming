def isOK(index, key):
    if a[index] <= key:
        return True
    else:
        return False

def bs(key):
    ok = -1
    ng = n
    while ng-ok > 1:
        mid = (ng+ok) // 2
        if isOK(mid, key):
            ok = mid
        else:
            ng = mid
    return ok


n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = [int(input()) for i in range(q)]
a.sort()
a.append(1<<60)

for i in range(q):
    key = b[i]
    index = bs(key)
    print(min(abs(key-a[index]), abs(key-a[index+1])))