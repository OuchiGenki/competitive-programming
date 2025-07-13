N, S = map(int, input().split())
A = list(map(int, input().split()))
S %= sum(A)
A += A
flag = False
right = 0
sum = 0
for left in range(N):
    while right < 2*N and sum + A[right] <= S:
        sum += A[right]
        right += 1
    if sum == S:
        flag = True
    if left == right:
        right += 1
    else:
        sum -= A[left]
print('Yes' if flag else 'No')