from collections import deque

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    g = [[] for i in range(n)]
    c = list(map(int, input().split()))

    for j in range(m):
        u, v = map(int, input().split())
        g[u-1].append(v-1)
        g[v-1].append(u-1)

    dist = [[-1 for i in range(n)] for j in range(n)]
    dist[0][n-1] = 0
    q = deque()
    q.append((0, n-1))
    ans = -1
    skip = False

    while q:
        t, a = q.popleft()

        if t==n-1 and a==0:
            print(dist[n-1][0])
            skip = True
            break

        for nt in g[t]:
            for na in g[a]:
                if c[nt] == c[na]:
                    continue
                if dist[nt][na] != -1:
                    continue
                dist[nt][na] = dist[t][a] + 1
                q.append((nt, na))
        
    if not skip:
        print(-1)