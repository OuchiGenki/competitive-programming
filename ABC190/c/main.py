n, m = map(int, input().split())
a = []
b = []
for i in range(m):
    A, B = map(int, input().split())
    a.append(A-1)
    b.append(B-1)
k = int(input())
c = []
d = []
for i in range(k):
    C, D = map(int, input().split())
    c.append(C-1)
    d.append(D-1)

ans = 0
for i in range(2**k):
    plate = [False for i in range(n)]
    for j in range(k):
        if i >> j & 1:
            plate[c[j]] = True
        else:
            plate[d[j]] = True
    res = 0
    for j in range(m):
        if plate[a[j]] and plate[b[j]]:
            res += 1
    ans = max(ans, res)

print(ans)