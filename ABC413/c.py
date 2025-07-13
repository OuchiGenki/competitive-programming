from collections import deque

q = int(input())
d = deque()
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        c, x = query[1], query[2]
        d.append([x, c])
    elif query[0] == 2:
        k = query[1]
        if d[0][1] >= k:
            print(d[0][0] * k)
            d[0][1] -= k
            if d[0][1] == 0:
                d.popleft()
        else:
            ans = 0
            cnt = 0
            while d[0][1] < k:
                cnt += d[0][1]
                ans += d[0][0] * d[0][1]
                k -= d[0][1]
                d.popleft()
            d[0][1] -= k
            ans += d[0][0] * k
            if d[0][1] == 0:
                d.popleft()
            print(ans)