N, K = map(int, input().split())

A = []
for i in range(N+1):
    if i < K:
        A.append(1)
    elif i == K:
        A.append(K)
    else:
        A.append(A[i-1] - A[i-K-1] + A[i-1])
    A[i] %= 10**9

print(A[N])