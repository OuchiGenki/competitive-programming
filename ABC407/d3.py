import sys
sys.setrecursionlimit(10**8)

def dfs(domino):
    global ans
    visited[domino] = True

    now = 0
    for i in range(H):
        for j in range(W):
            bit = i * W + j
            if not domino & (1 << bit):
                now ^= A[i][j]
    ans = max(ans, now)

    horizontal_domino = 3
    vertical_domino = 1 | (1 << W)

    for i in range(H):
        for j in range(W):
            bit = i * W + j
            if j < W-1 and not (domino & (horizontal_domino << bit)):
                if visited[domino | (horizontal_domino << bit)]:
                    continue
                dfs(domino | (horizontal_domino << bit))
            if i < H-1 and not (domino & (vertical_domino << bit)):
                if visited[domino | (vertical_domino << bit)]:
                    continue
                dfs(domino | (vertical_domino << bit))


H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

ans = 0
visited = [False] * 2**(H*W)
dfs(0)

print(ans)