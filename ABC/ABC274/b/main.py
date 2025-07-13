h, w = map(int, input().split())
c = [input() for i in range(h)]
ans = []
for i in range(w):
    cnt = 0
    for j in range(h):
        if c[j][i] == "#":
            cnt += 1
    ans.append(cnt)
print(*ans)