from collections import deque, defaultdict

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b, w = map(int, input().split())
    G[a-1].append((w, b-1))

queue = deque([(0, 0)])
visited = defaultdict(bool)
visited[(0, 0)] = True

while queue:
    now, v = queue.popleft()
    for weight, next_v in G[v]:
        if visited[(next_v, now^weight)]:
            continue
        visited[(next_v, now^weight)] = True
        queue.append((now^weight, next_v))

for i in range(2**10):
    if visited[(N-1, i)]:
        print(i)
        exit()

print(-1)