n = int(input())
cnt = [[0 for i in range(1010)] for j in range(1010)]
for i in range(n):
    lx, ly, rx, ry = map(int, input().split())
    cnt[ly][lx] += 1
    cnt[ry][rx] += 1
    cnt[ry][lx] -= 1
    cnt[ly][rx] -= 1

for i in range(1001):
    for j in range(1, 1001):
        cnt[i][j] += cnt[i][j-1]
for i in range(1001):
    for j in range(1, 1001):
        cnt[j][i] += cnt[j-1][i]

ans = [0 for i in range(1<<18)]
for i in range(1001):
    for j in range(1001):
        ans[cnt[i][j]] += 1

for i in range(1, n+1):
    print(ans[i])