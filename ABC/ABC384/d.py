N, S = map(int, input().split())
A = list(map(int, input().split()))
S %= sum(A)
A *= 2

right = 0
sum = 0
for left in range(N):
    while sum + A[right] <= S:
        sum += A[right]
        right += 1
    
    if sum == S:
        print('Yes')
        exit()
    
    if left == right:
        right += 1
    else:
        sum -= A[left]

print('No')
