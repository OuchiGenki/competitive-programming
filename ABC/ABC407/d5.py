import sys
sys.setrecursionlimit(10**8)

def dfs(domino):
    global ans
    visited[domino] = True
    h_domino = 3
    v_domino = 1 | (1 << W)

    now = 0
    for i in range(H):
        for j in range(W):
            bit = i*W + j
            if not domino & (1 << bit):
                now ^= A[i][j]
    ans = max(ans, now)

    for i in range(H):
        for j in range(W):
            bit = i*W + j
            if j < W - 1 and not (domino & (h_domino << bit)) and not visited[domino | (h_domino << bit)]:
                dfs(domino | (h_domino << bit))
            if i < H - 1 and not (domino & (v_domino << bit)) and not visited[domino | (v_domino << bit)]:
                dfs(domino | (v_domino << bit))




H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
visited = [False] * (2**(H*W))
ans = 0

dfs(0)

print(ans)