n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 1<<60
for i in range(2**n):
    cnt = 0
    cost = 0
    max_h = 0
    for j in range(n):
        if i>>j & 1:
            if a[j] <= max_h:
                cost += max_h+1-a[j]
                cnt += 1
                max_h += 1
            else:
                cnt += 1
                max_h = a[j]
        else:
            if a[j] > max_h:
                cnt += 1
                max_h = a[j]
        if cnt == k:
            ans = min(ans, cost)
            continue
print(ans)