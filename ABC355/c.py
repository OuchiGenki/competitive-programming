N, T = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))
g = [[-1 for i in range(N)] for j in range(N)]
for i in range(T):
    g[A[i]//N][A[i]%N] = i+1

res = float('inf')

for i in range(N):
    cnt = 0
    tmp = 0
    for j in range(N):
        if g[i][j] != -1:
            cnt += 1
            tmp = max(tmp, g[i][j])
    if cnt == N:
        res = min(res, tmp)

for i in range(N):
    cnt = 0
    tmp = 0
    for j in range(N):
        if g[j][i] != -1:
            cnt += 1
            tmp = max(tmp, g[j][i])
    if cnt == N:
        res = min(res, tmp)

cnt = 0
tmp = 0
for i in range(N):
    if g[i][i] != -1:
        cnt += 1
        tmp = max(tmp, g[i][i])
if cnt == N:
    res = min(res, tmp)

cnt = 0
tmp = 0
for i in range(N):
    if g[i][N-i-1] != -1:
        cnt += 1
        tmp = max(tmp, g[i][N-i-1])
if cnt == N:
    res = min(res, tmp)

if res != float('inf'):
    print(res)
else:
    print(-1)