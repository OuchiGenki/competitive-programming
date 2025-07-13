L, N1, N2 = map(int, input().split())
V1, L1 = [], []
for i in range(N1):
    v, l = map(int, input().split())
    V1.append(v)
    L1.append(l)
V2, L2 = [], []
for i in range(N2):
    v, l = map(int, input().split())
    V2.append(v)
    L2.append(l)

ans = 0
i, j, p, q = 0, 0, 0, 0
while i < N1 and j < N2:
    if V1[i] == V2[j]:
        ans += min(p + L1[i], q + L2[j]) - max(p, q)
    if p + L1[i] < q + L2[j]:
        p += L1[i]
        i += 1
    else:
        q += L2[j]
        j += 1

print(ans)