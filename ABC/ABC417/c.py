from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
cnt = defaultdict(int)
ans = 0
for j in range(n):
    cnt[A[j]+(j+1)] += 1
    ans += cnt[(j+1) - A[j]]
print(ans)
