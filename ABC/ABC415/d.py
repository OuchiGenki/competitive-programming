n, m = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(m)]
AB.sort(key=lambda x: x[0]-x[1])
A, B = zip(*AB)
C = [A[i] - B[i] for i in range(m)]
ans = 0
i = 0
while i < m:
    if (n - A[i]) < 0:
        i += 1
        continue
    x = (n - A[i]) // C[i]
    n -= x * C[i]
    ans += x
    if n - C[i] < 0:
        break
    ans += 1
    n -= C[i]
    i += 1

print(ans)