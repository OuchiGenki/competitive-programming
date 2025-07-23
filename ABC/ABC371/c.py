from itertools import permutations

n = int(input())
mg = int(input())
G = [[0] * n for _ in range(n)]
for _ in range(mg):
    u, v = map(int, input().split())
    G[u-1][v-1] = 1
    G[v-1][u-1] = 1
mh = int(input())
H = [[0] * n for _ in range(n)]
for _ in range(mh):
    a, b = map(int, input().split())
    H[a-1][b-1] = 1
    H[b-1][a-1] = 1
A = [[0] * n for _ in range(n)]
for i in range(n-1):
    lst = list(map(int, input().split()))
    for j in range(len(lst)):
        a = i
        b = i + j + 1
        A[a][b] = lst[j]
        A[b][a] = lst[j]

ans = float('inf')

for P in permutations(range(n)):
    now = 0
    for i in range(n):
        for j in range(i+1, n):
            if G[i][j] != H[P[i]][P[j]]:
                now += A[P[i]][P[j]]
    ans = min(ans, now)

print(ans)
