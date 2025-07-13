N = int(input())
A = list(map(int, input().split()))

res = 0
right = 0
for left in range(N):
    while right < N and (left == right or A[right-1] < A[right]):
        right += 1
    res += right-left

print(res)