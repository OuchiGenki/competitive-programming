from collections import deque

Q = int(input())
queue = deque()
day = 0
ans = []

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        queue.append(day)
    elif query[0] == 2:
        T = query[1]
        day += T
    elif query[0] == 3:
        H = query[1]
        cnt = 0
        while queue and day-queue[0] >= H:
            queue.popleft()
            cnt += 1
        ans.append(cnt)

for i in ans:
    print(i)