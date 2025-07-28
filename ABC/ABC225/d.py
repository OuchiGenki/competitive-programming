from collections import defaultdict

n, q = map(int, input().split())
front = defaultdict(lambda: -1)
back = defaultdict(lambda: -1)
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, y = query[1], query[2]
        back[x] = y
        front[y] = x
    elif query[0] == 2:
        x, y = query[1], query[2]
        back[x] = -1
        front[y] = -1
    elif query[0] == 3:
        x = query[1]
        train = x
        ans = []
        while front[train] != -1:
            train = front[train]
        while back[train] != -1:
            ans.append(train)
            train = back[train]
        ans.append(train)
        print(len(ans), *ans)