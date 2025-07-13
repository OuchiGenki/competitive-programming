N = int(input())
A = list(map(int, input().split()))
A.sort()

res = 0
for i in range(N):
    res += (N-1) * A[i]

cnt = 0
right = N
for left in range(N):
    while right-1 > left and A[left] + A[right-1] >= 10**8:
        right -= 1
    cnt += N - right
    if right-1 == left:
        right += 1

print(res - 10**8*cnt)