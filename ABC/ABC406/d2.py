H, W, N = map(int, input().split())
row = [[] for i in range(H)]
col = [[] for i in range(W)]
for i in range(N):
    x, y = map(int, input().split())
    row[x-1].append(y-1)
    col[y-1].append(x-1)
used = set()
s = set()

Q = int(input())
for i in range(Q):
    li = list(map(int, input().split()))
    if tuple(li) in s:
        print(0)
        continue

    s.add(tuple(li))
    cnt = 0
    if li[0] == 1:
        x = li[1]-1
        for j in row[x]:
            if not (x, j) in used:
                cnt += 1
                used.add((x, j))
    else:
        y = li[1]-1
        for j in col[y]:
            if not (j, y) in used:
                cnt += 1
                used.add((j, y))
    print(cnt)