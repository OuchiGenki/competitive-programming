N = int(input())
A = list(map(lambda x: int(x)-1, input().split()))

ans = 0
flavor = [0 for i in range(10**5)]
right = 0
for left in range(N):
    while right < N and flavor[A[right]] == 0:
        flavor[A[right]] += 1
        right += 1
    ans = max(ans, right-left)
    if left == right:
        right += 1
    else:
        flavor[A[left]] -= 1

print(ans)