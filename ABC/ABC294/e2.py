L, N1, N2 = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N1)]
B = [list(map(int, input().split())) for i in range(N2)]

i, j, p, q, ans = 0, 0, 0, 0, 0
while i < N1 and j < N2:
    if A[i][0] == B[j][0]:
        ans += min(p + A[i][1], q + B[j][1]) - max(p, q)
    if p + A[i][1] < q + B[j][1]:
        p += A[i][1]
        i += 1
    else:
        q += B[j][1]
        j += 1
print(ans)