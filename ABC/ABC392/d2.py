from bisect import bisect_left, bisect_right

N = int(input())
K = []
A = []
for i in range(N):
    li = list(map(int, input().split()))
    K.append(li[0])
    A.append(sorted(li[1:]))

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        res = 0
        for a in A[i]:
            res += bisect_right(A[j], a) - bisect_left(A[j], a)
        ans = max(ans, res / (K[i] * K[j]))
print(ans)