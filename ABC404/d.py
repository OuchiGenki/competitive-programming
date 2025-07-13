from itertools import product

N, M = map(int, input().split())
C = list(map(int, input().split()))
K = []
A = []
for i in range(M):
    row = list(map(int, input().split()))
    K.append(row[0])
    A.append(row[1:])

zoo = [[] for i in range(N)]
for i in range(M):
    for j in range(K[i]):
        zoo[A[i][j]-1].append(i)

ans = float('inf')
for v in product([0, 1, 2], repeat=N):
    cnt = [0] * M
    cost = 0
    for i in range(N):
        cost += C[i] * v[i]
        for j in zoo[i]:
            cnt[j] += v[i]
    
    flag = True
    for i in range(M):
        if cnt[i] < 2:
            flag = False
    if flag:
        ans = min(ans, cost)

print(ans)