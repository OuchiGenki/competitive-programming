def isOK(s1, x, index):
    if s1 + li2[index][x] <= p:
        return True
    else:
        return False

def bs(s1, index):
    ok = -1
    ng = len(li2[index])

    while (ng-ok)>1:
        mid = (ng+ok)//2
        if isOK(s1, mid, index):
            ok = mid
        else:
            ng = mid
    
    return ok+1

n, k, p = map(int, input().split())
a = list(map(int, input().split()))

n1 = n//2
n2 = n-n1

li1 = [[] for j in range(n1+1)]
for i in range(2**n1):
    cnt = 0
    res = 0
    for j in range(n1):
        if (i>>j)&1:
            cnt += 1
            res += a[j]
    li1[cnt].append(res)

li2 = [[] for j in range(n2+1)]
for i in range(2**n2):
    cnt = 0
    res = 0
    for j in range(n2):
        if (i>>j)&1:
            cnt += 1
            res += a[n1+j]
    li2[cnt].append(res)

for i in range(n1+1):
    li1[i].sort()
for i in range(n2+1):
    li2[i].sort()

ans = 0
for i in range(n1+1):
    for j in li1[i]:
        index = k-i
        if 0 <= index <= n2:
            ans += bs(j, index)
print(ans)