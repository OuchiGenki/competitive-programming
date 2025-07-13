N, M = map(int, input().split())
A = [0] * N

for i in range(M):
    l, r = map(lambda x: int(x)-1, input().split())
    A[l] += 1
    if r+1 < N:
        A[r+1] += -1

for i in range(1, N):
    A[i] += A[i-1]

print(min(A))