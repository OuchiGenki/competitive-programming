n = int(input())
C = []
for _  in range(n):
    a, b = map(int, input().split())
    C.append((a, 1))
    C.append((a+b, -1))
C.sort()
D = [C[i][0] for i in range(2*n)]
T = [C[i][1] for i in range(2*n)]
ans = [0] * n
p = 1
for i in range(1, 2*n):
    if p > 0:
        ans[p-1] += D[i] - D[i-1]
    p += T[i]
print(*ans)