from collections import defaultdict

n, k = map(int, input().split())
A = list(map(int, input().split()))
cum = [0]
for i in range(n):
    cum.append(cum[-1] + A[i])
freq = defaultdict(int)
ans = 0
for r in range(1, n + 1):
    freq[cum[r-1]] += 1
    ans += freq[cum[r] - k]
print(ans)