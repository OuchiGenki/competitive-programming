N, K = map(int, input().split())
A = list(map(int, input().split()))
res = K * (1 + K) // 2
s = set()
for i in range(N):
    if 1 <= A[i] <= K and A[i] not in s:
        s.add(A[i])
        res -= A[i]
print(res)