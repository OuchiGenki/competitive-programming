from itertools import permutations

N, M = map(int, input().split())
G = [[] for i in range(N)]
E = [[False]*N for i in range(N)]
W = [[-1]*N for i in range(N)]
for i in range(M):
    u, v, w = map(int, input().split())
    G[u-1].append((v-1, w))
    G[v-1].append((u-1, w))
    E[u-1][v-1] = True
    E[v-1][u-1] = True
    W[u-1][v-1] = w
    W[v-1][u-1] = w

answer = float('inf')
for i in range(2, N+1):
    for v in permutations(range(N), i):
        if v[0] != 0 or v[-1] != N-1:
            continue

        cnt = 0
        score = 0
        for j in range(i-1):
            if E[v[j]][v[j+1]]:
                cnt += 1
                score ^= W[v[j]][v[j+ 1]]
            else:
                break

        if cnt == i-1:
            answer = min(answer, score)

print(answer)

