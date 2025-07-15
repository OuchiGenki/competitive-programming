from collections import defaultdict

n, k = map(int, input().split())
A = list(map(int, input().split()))
now = 0
cnt = defaultdict(int)
ans = 0
right = 0
for left in range(n):
    while right < n and now <=  k:
        if cnt[A[right]] == 0 and now == k:
            break
        if cnt[A[right]] == 0:
            now += 1
        cnt[A[right]] += 1
        right += 1
    ans = max(ans, right - left) 
    if left == right:
        right += 1
    cnt[A[left]] -= 1
    if cnt[A[left]] == 0:
        now -= 1
print(ans)