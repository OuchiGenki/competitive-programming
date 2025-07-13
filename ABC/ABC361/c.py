N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
res = float('inf')
for i in range(N):
    if i+N-K-1 >= N:
        break
    res = min(res, abs(A[i+N-K-1]-A[i]))
print(res)