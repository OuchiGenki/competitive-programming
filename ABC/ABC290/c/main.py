n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = list(set(a))
ans = 0
for i in range(k):
    if i >= len(a):
        break
    if a[i] == i:
        ans += 1
    else:
        break
print(ans)