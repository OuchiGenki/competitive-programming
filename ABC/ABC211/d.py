from collections import deque

MOD = 10**9 + 7
n, m = map(int, input().split())
to = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    to[a-1].append(b-1)
    to[b-1].append(a-1)

dist = [-1] * n
dp = [0] * n
dp[0] = 1
que = deque()
que.append(0)
dist[0] = 0

while que:
    v = que.popleft()
    for nv in to[v]:
        if dist[nv] != -1:
            if dist[nv] == dist[v] + 1:
                dp[nv] += dp[v]
                dp[nv] %= MOD
            continue
        dist[nv] = dist[v] + 1
        dp[nv] += dp[v]
        dp[nv] %= MOD
        que.append(nv)

print(dp[n-1])