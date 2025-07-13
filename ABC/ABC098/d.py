N = int(input())
A = list(map(int, input().split()))

right = 0
xor = 0
sum = 0
res = 0
for left in range(N):
    while right < N and sum ^ A[right] == sum + A[right]:
        xor ^= A[right]
        sum += A[right]
        right += 1
    res += right - left
    if left == right:
        right += 1
    else:
        xor ^= A[left]
        sum -= A[left]

print(res)