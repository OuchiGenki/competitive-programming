n = int(input())
cnt = [0 for i in range(10**6+10)]
for i in range(n):
    a, b = map(int, input().split())
    cnt[a] += 1
    cnt[b+1] -= 1
ans = cnt[0]
for i in range(1, 10**6+1):
    cnt[i] += cnt[i-1]
    ans = max(ans, cnt[i])
print(ans)