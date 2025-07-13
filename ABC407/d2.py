from collections import deque, defaultdict

H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

horizontal_domino = 3
vertical_domino = 1 | (1 << W)
queue = deque()
queue.append(0)
visited = defaultdict(bool)
visited[0] = True
ans = 0

while queue:
    v = queue.popleft()
    now = 0
    for i in range(H):
        for j in range(W):
            bit = i*W + j
            if not v & (1 << bit):
                now ^= A[i][j]
    ans = max(ans, now)


    for i in range(H):
        for j in range(W):
            bit = i*W + j
            if j < W-1 and not (v & (horizontal_domino << bit)) and not visited[v | (horizontal_domino << bit)]:
                visited[v | (horizontal_domino << bit)] = True
                queue.append(v | (horizontal_domino << bit))
            if i < H-1 and not (v & (vertical_domino << bit)) and not visited[v | (vertical_domino << bit)]:
                queue.append(v | (vertical_domino << bit))
                visited[v | (vertical_domino << bit)] = True

print(ans)