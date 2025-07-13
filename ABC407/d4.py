from collections import deque, defaultdict

H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

horizontal_domino = 3
vertical_domino = 1 | (1 << W)
queue = deque([0])
visited = set()
ans = 0

while queue:
    domino = queue.popleft()
    now = 0
    for i in range(H):
        for j in range(W):
            bit = i * W + j
            if domino & (1 << bit):
                continue
            now ^= A[i][j]
    ans = max(ans, now)

    for i in range(H):
        for j in range(W):
            bit = i * W + j
            if j < W - 1 and not (domino & (horizontal_domino << bit)) and (domino | (horizontal_domino << bit)) not in visited:
                queue.append(domino | (horizontal_domino << bit))
                visited.add(domino | (horizontal_domino << bit))
            if i < H - 1 and not (domino & (vertical_domino << bit)) and (domino | (vertical_domino << bit)) not in visited:
                queue.append(domino | (vertical_domino << bit))
                visited.add(domino | (vertical_domino << bit))

print(ans)