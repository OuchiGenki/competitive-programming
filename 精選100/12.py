n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)

ans = 0
for i in range(2**n):
    cnt = 0
    check = []
    seen = [False for i in range(n)]
    s = set()
    for j in range(n):
        if i>>j & 1:
            cnt += 1
            check.append(j)
    flag = True
    for j in range(cnt):
        for k in range(cnt):
            if j == k: continue
            if check[k] not in g[check[j]]:
                flag = False
    if flag:
        ans = max(ans, cnt)

print(ans)