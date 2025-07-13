N = int(input())
A = list(map(int, input().split()))
sum_A = sum(A)

res = 0
for i in range(N):
    res += A[i] * (sum_A - A[i])

print(res // 2)