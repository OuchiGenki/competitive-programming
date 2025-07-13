from itertools import permutations

N, M = map(int, input().split())
edges1 = [[0] * N for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    edges1[a-1][b-1] = 1
ans = float('inf')

for lst in permutations([i for i in range(N)]):
    edges2 = [[0] * N for i in range(N)]
    for i in range(N):
        u, v = lst[i % N], lst[(i + 1) % N]
        if u > v:
            u, v = v, u
        edges2[u][v] = 1

    now = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if edges1[i][j] != edges2[i][j]:
                now += 1
    ans = min(ans, now)

for sz in range(3, N-3+1):
    for lst in permutations([i for i in range(N)]):
        edges2 = [[0] * N for i in range(N)]
        for i in range(sz):
            u, v = lst[i], lst[(i + 1) % sz]
            if u > v:
                u, v = v, u
            edges2[u][v] = 1
        for i in range(N-sz):
            u, v = lst[sz + i], lst[sz + ((i + 1) % (N - sz))]
            if u > v:
                u, v = v, u
            edges2[u][v] = 1
        
        now = 0
        for i in range(N-1):
            for j in range(i+1, N):
                if edges1[i][j] != edges2[i][j]:
                    now += 1
        ans = min(ans, now)

print(ans)