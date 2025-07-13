L, N1, N2 = map(int, input().split())
v1, l1 = [], []
v2, l2 = [], []
for i in range(N1):
    v, l = map(int, input().split())
    v1.append(v)
    l1.append(l)
for i in range(N2):
    v, l = map(int, input().split())
    v2.append(v)
    l2.append(l)

i, j = 0, 0
p, q = 0, 0
ans = 0
while i < N1 and j < N2:
    if v1[i] == v2[j]:
        ans += min(p + l1[i], q + l2[j]) - max(p, q)
    if p + l1[i] < q + l2[j]:
        p += l1[i]
        i += 1
    else:
        q += l2[j]
        j += 1
print(ans)