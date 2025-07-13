from collections import deque

Q = int(input())
queue = deque()

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        X = query[1]
        queue.append(X)
    else:
        num = queue.popleft()
        print(num)