H, W, N = map(int, input().split())
pos_r = [[] for j in range(H)]
pos_c = [[] for j in range(W)]
exists = dict()
for i in range(N):
    x,y = map(int, input().split())
    exists[(x-1, y-1)] = True
    pos_r[x-1].append(y-1)
    pos_c[y-1].append(x-1)

Q = int(input())
s = set()
for i in range(Q):
    query = list(map(int, input().split()))
    if tuple(query) in s:
        print(0)
        continue

    if query[0] == 1:
        x = query[1]
        res = 0
        for g in pos_r[x-1]:
            if exists[(x-1, g)]:
                res += 1
                exists[(x-1, g)] = False
        print(res)

    else:
        y = query[1]
        res = 0
        for g in pos_c[y-1]:
            if exists[(g, y-1)]:
                res += 1
                exists[(g, y-1)] = False
        print(res)
    
    s.add(tuple(query))
