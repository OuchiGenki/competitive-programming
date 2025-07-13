r, c = map(int, input().split())
a = [list(map(int, input().split())) for i in range(r)]

ans = 0
for i in range(2**r):
    res = 0
    cnt = [0 for i in range(c)]
    for j in range(r):
        if i>>j & 1:
            for k in range(c):
                if a[j][k] == 1:
                    cnt[k] += 1
        else:
            for k in range(c):
                if a[j][k] == 0:
                    cnt[k] += 1
    for j in range(c):
        res += max(cnt[j], r-cnt[j])
    ans = max(ans, res)
print(ans)