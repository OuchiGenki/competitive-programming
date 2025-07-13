w, n = map(int, input().split())
l, r = [], []
a = []
for i in range(n):
    L, R = map(int, input().split())
    l.append(L)
    r.append(R)
    a.append(L)
    a.append(R)

b = sorted(set(a))
d = {v: i for i, v in enumerate(b)}
for i in range(n):
    l[i] = d[l[i]]
    r[i] = d[r[i]]

field = [0 for i in range(10**6)]
ans = [0 for i in range(n)]
for i in range(n):
    maxH = 0
    for j in range(l[i], r[i]+1):
        maxH = max(maxH, field[j])
    for j in range(l[i], r[i]+1):
        field[j] = maxH+1
    ans[i] = maxH+1
for i in ans:
    print(i)