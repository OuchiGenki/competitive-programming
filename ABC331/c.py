from bisect import bisect_right

N = int(input())
A = list(map(int, input().split()))
A = [(A[i], i) for i in range(N)]
A.sort()
B = []
C = []
for i in range(N):
    B.append(A[i][0])
    C.append(A[i][1])

cum = [0]
for i in range(N):
    cum.append(cum[i] + B[i])

ans = [0 for i in range(N)]

for i in range(N):
    ans[C[i]] = cum[N] - cum[bisect_right(B, B[i])]

print(*ans)