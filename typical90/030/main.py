n, k = map(int, input().split())
c = [0 for i in range(n+1)]
for i in range(2, n+1):
    if c[i] != 0:
        continue
    for j in range(i, n+1, i):
        c[j] += 1
ans = 0
for i in c:
    if i >= k:
        ans += 1
print(ans)