N = int(input())
A = list(map(int, input().split()))
B = [0 for i in range(N)]
X = [0 for i in range(N)]
for i in range(N):
    if i > 0:
        X[i] += X[i-1]
    if i < N-1:
        X[i+1] += 1
    if i+A[i]+X[i]+1 < N:
        X[i+A[i]+X[i]+1] -= 1
    B[i] = max(0, A[i] + X[i] - (N-i-1))

print(*B)