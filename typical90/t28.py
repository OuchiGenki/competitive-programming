from collections import defaultdict

n = int(input())
cnt = [[0] * (10**3+10) for i in range(10**3+10)]
for i in range(n):
    lx, ly, rx, ry = map(int, input().split())
    cnt[ly][lx] += 1
    cnt[ry][rx] += 1
    cnt[ly][rx] -= 1
    cnt[ry][lx] -= 1
for i in range(10**3+1):
    for j in range(10**3+1):
        cnt[i+1][j] += cnt[i][j]
for i in range(10**3+1):
    for j in range(10**3+1):
        cnt[i][j+1] += cnt[i][j]

ans = defaultdict(int)
for i in range(10**3+1):
    for j in range(10**3+1):
        ans[cnt[i][j]] += 1
for i in range(1, n+1):
    print(ans[i])
