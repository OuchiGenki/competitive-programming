n = int(input())
a = []
b = []
for i in range(n):
    tmpA, tmpB = map(int, input().split())
    a.append(tmpA)
    b.append(tmpB)

ans = 1<<60
for i in range(n):
    for j in range(n):
        if a[i] > b[j]:
            continue
        res = 0
        for k in range(n):
            p1 = a[k]
            p2 = b[k]
            if p1 < a[i]:
                res += 2*(a[i]-p1)
            res += b[j]-a[i]
            if b[j] < p2:
                res += 2*(p2-b[j])
        ans = min(ans, res)
print(ans)