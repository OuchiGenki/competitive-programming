N = int(input())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
sumA = sum(A)

res = 0
for i in range(N):
    res = max(res, sumA - A[i] + B[i])

print(res)