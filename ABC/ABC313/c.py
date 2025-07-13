N = int(input())
A = list(map(int, input().split()))
A.sort()
q = sum(A) // N
r = sum(A) % N
base = [q] * N
for i in range(r):
    base[N-i-1] += 1

res = 0
for i in range(N):
    res += abs(A[i] - base[i])

print(res // 2)