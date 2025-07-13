N = int(input())
A = list(map(int, input().split()))
ans = 0
right = 0
s = set()

for left in range(0, N, 2):
    while right+1 < N and A[right] == A[right+1] and A[right] not in s:
        s.add(A[right])
        right += 2
    ans = max(ans, right - left)
    if left == right:
        right += 2
    else:
        s.discard(A[left])

right = 1
for left in range(1, N, 2):
    while right+1 < N and A[right] == A[right+1] and A[right] not in s:
        s.add(A[right])
        right += 2
    ans = max(ans, right - left)
    if left == right:
        right += 2
    else:
        s.discard(A[left])

print(ans)