n = int(input())
A = list(map(int, input().split()))
revA = A[::-1]
l = [1] * n
r = [1] * n

height = 1
right = 0
for left in range(n):
    while right < n and A[right] >= height:
        l[right] = min((n+1)//2, height)
        height += 1
        right += 1
    if left == right:
        right += 1
    height -= 1

height = 1
right = 0
for left in range(n):
    while right < n and revA[right] >= height:
        r[right] = min((n+1)//2, height)
        height += 1
        right += 1
    if left == right:
        right += 1
    height -= 1
r = r[::-1]

ans = 0
for i in range(n):
    ans = max(ans, min(l[i], r[i]))
print(ans)
