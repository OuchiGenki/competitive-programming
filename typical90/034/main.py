n, k = map(int, input().split())
a = list(map(int, input().split()))
s = set()

left = right = 0
ans = 0
d = dict()
while left < n:
    while right < n:
        if a[right] in d:
            d[a[right]] += 1
        else:
            if len(d) == k:
                break
            d[a[right]] = 1
        right += 1
        ans = max(ans, right-left)
    d[a[left]] -= 1
    if d[a[left]] == 0:
        d.pop(a[left])
    left += 1

print(ans)