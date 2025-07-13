from collections import deque, defaultdict

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b, w = map(int ,input().split())
    G[a-1].append((b-1, w))

q = deque()
q.append((0, 0))
visited = defaultdict(bool)
visited[(0, 0)] = True

while q:
    v, now = q.popleft()
    for nv, nw in G[v]:
        if visited[(nv, now^nw)]:
            continue
        visited[(nv, now^nw)] = True
        q.append((nv, now^nw))

for i in range(1024):
    if visited[(N-1, i)]:
        print(i)
        exit()
print(-1)